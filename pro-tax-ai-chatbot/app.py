import os
import re
import pickle
import faiss
import streamlit as st
import numpy as np
from dotenv import load_dotenv
from groq import Groq
from sentence_transformers import SentenceTransformer, CrossEncoder
import pdfplumber

# -----------------------------
# CONFIG
# -----------------------------
load_dotenv()
st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="wide")

DATA_PATH = "./data/Cinayet_mecellesi.pdf"  # PDF faylın yolu
INDEX_PATH = "faiss.index"
CHUNKS_PATH = "chunks.pkl"
META_PATH = "meta.pkl"

USE_HYDE = False
USE_RERANK = True
TOP_K = 8

# -----------------------------
# SESSION MEMORY
# -----------------------------
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# -----------------------------
# LOAD MODELS
# -----------------------------
@st.cache_resource
def load_models():
    bi_encoder = SentenceTransformer("intfloat/multilingual-e5-base")
    cross_encoder = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    return bi_encoder, cross_encoder, client

bi_encoder, cross_encoder, client = load_models()

# -----------------------------
# CHUNKING
# -----------------------------
def advanced_chunking(text):
    pattern = r"(?=\n\d+(\.\d+)+)"
    parts = re.split(pattern, text)
    chunks = []

    for part in parts:
        match = re.search(r"(\d+(\.\d+)+)", part)
        if not match:
            continue

        full_id = match.group(1)
        madde = full_id.split(".")[0]
        header = f"Section {madde} / {full_id}: "
        chunks.append({
            "content": header + part.strip(),
            "metadata": {"madde": madde, "full_id": full_id}
        })

    return chunks

# -----------------------------
# TOPIC DETECTION
# -----------------------------
def detect_topic(text):
    sample = text[:2000]  # ilk 2k simvol
    prompt = f"""
Bu mətn hansı sahəyə aiddir?
Variantlar: Hüquq, Vergi, Tarix, Biologiya, Tibb, Texnologiya, Digər
Sadəcə 1 söz cavab verin.

Mətn: {sample}
"""
    res = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return res.choices[0].message.content.strip()

# -----------------------------
# BUILD & SAVE INDEX
# -----------------------------
def build_and_save_index():
    with st.spinner("PDF oxunur və index qurulur..."):
        text = ""
        with pdfplumber.open(DATA_PATH) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

        chunks = advanced_chunking(text)

        texts = [f"passage: {c['content']}" for c in chunks]
        embeddings = bi_encoder.encode(texts, batch_size=32, convert_to_numpy=True)
        faiss.normalize_L2(embeddings)

        index = faiss.IndexFlatIP(embeddings.shape[1])
        index.add(embeddings.astype("float32"))

        faiss.write_index(index, INDEX_PATH)
        with open(CHUNKS_PATH, "wb") as f:
            pickle.dump(chunks, f)

        # topic
        topic = detect_topic(text)
        with open(META_PATH, "wb") as f:
            pickle.dump({"topic": topic}, f)

        return chunks, index, topic

# -----------------------------
# LOAD INDEX
# -----------------------------
@st.cache_resource
def load_index():
    if not os.path.exists(INDEX_PATH):
        return build_and_save_index()
    index = faiss.read_index(INDEX_PATH)
    with open(CHUNKS_PATH, "rb") as f:
        chunks = pickle.load(f)
    if os.path.exists(META_PATH):
        with open(META_PATH, "rb") as f:
            topic = pickle.load(f)["topic"]
    else:
        topic = "General"
    return chunks, index, topic

chunks, index, topic = load_index()

# -----------------------------
# DYNAMIC TITLE
# -----------------------------
st.title(f"{topic} AI Chatbot")

# -----------------------------
# EXACT MATCH
# -----------------------------
def find_exact_match(query, chunks):
    pattern = re.search(r"\d+(\.\d+)+", query)
    if not pattern:
        return None
    target = pattern.group(0)
    for c in chunks:
        if c["metadata"].get("full_id") == target:
            return [c]
    return None

# -----------------------------
# CONTEXTUAL QUERY
# -----------------------------
def build_contextual_query(query):
    if len(st.session_state.chat_history) == 0:
        return query
    last_turns = st.session_state.chat_history[-2:]
    history_text = ""
    for h in last_turns:
        history_text += f"Sual: {h['user']}\nCavab: {h['assistant']}\n"
    return f"{history_text}\nYeni sual: {query}"

# -----------------------------
# RETRIEVAL
# -----------------------------
def retrieve(query):
    exact = find_exact_match(query, chunks)
    if exact:
        return exact
    query_text = build_contextual_query(query)
    q_emb = bi_encoder.encode([query_text]).astype("float32")
    faiss.normalize_L2(q_emb)
    distances, indices = index.search(q_emb, TOP_K)
    candidates = [chunks[i] for i in indices[0]]
    if USE_RERANK and len(candidates) > 3:
        pairs = [[query, c["content"]] for c in candidates]
        scores = cross_encoder.predict(pairs)
        for i in range(len(candidates)):
            candidates[i]["score"] = scores[i]
        candidates = sorted(candidates, key=lambda x: x["score"], reverse=True)
    return candidates[:5]

# -----------------------------
# GENERATE ANSWER
# -----------------------------
def generate_answer(query, contexts):
    if not contexts:
        return "Bu suala uyğun maddə tapılmadı."
    context_text = "\n\n".join([f"[{c['metadata']['full_id']}]\n{c['content']}" for c in contexts])
    history = ""
    for h in st.session_state.chat_history[-3:]:
        history += f"User: {h['user']}\nAssistant: {h['assistant']}\n"
    system_prompt = """Sən hüquqi / mövzu üzrə ekspert botsan.
- Kontekstdən istifadə et
- Əvvəlki sualları nəzərə al
- Follow-up sualları düzgün başa düş"""
    res = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"{history}\n{context_text}\n\nSUAL: {query}"}
        ],
        temperature=0
    )
    return res.choices[0].message.content

# -----------------------------
# UI CHAT
# -----------------------------
# show previous chat
for chat in st.session_state["chat_history"]:
    with st.chat_message("user"):
        st.write(chat["user"])
    with st.chat_message("assistant"):
        st.write(chat["assistant"])

# chat input
user_input = st.chat_input("Sualınızı yazın...")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)
    with st.chat_message("assistant"):
        with st.spinner("Düşünür..."):
            docs = retrieve(user_input)
            answer = generate_answer(user_input, docs)
            st.write(answer)
    st.session_state["chat_history"].append({"user": user_input, "assistant": answer})