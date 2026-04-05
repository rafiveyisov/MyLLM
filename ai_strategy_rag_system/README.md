# Advanced RAG Pipeline with Reranking
## Azerbaijan National AI Strategy 2025–2028 Analysis

This project implements a sophisticated **Retrieval-Augmented Generation (RAG)** pipeline designed to answer questions based on the official *Azerbaijan National Strategy for Artificial Intelligence 2025–2028*.

### 🚀 Features
* **Data Ingestion:** Extracts text from legal PDF documents using `pdfplumber`.
* **Semantic Chunking:** Splits text into 500-character segments with overlap to preserve context.
* **Vector Search:** Uses `FAISS` and `sentence-transformers` (`paraphrase-multilingual-MiniLM-L12-v2`) for efficient multilingual similarity search.
* **Reranking:** Implements a **Cross-Encoder** (`ms-marco-MiniLM-L-6-v2`) to refine search results for higher accuracy.
* **LLM Generation:** Integrates with **Groq API** (Llama-3.3-70B) to generate precise answers in Azerbaijani.

### 🛠️ Tech Stack
* **Language:** Python
* **Vector DB:** FAISS
* **Models:** Sentence-Transformers (Bi-Encoder & Cross-Encoder)
* **Inference:** Groq Cloud API
* **Interface:** IPython Widgets

### 📋 Prerequisites
1. Get a free API Key from [Groq Cloud Console](https://console.groq.com).
2. Install the required dependencies:
   ```bash
   pip install numpy<2.0 pdfplumber faiss-cpu sentence-transformers groq ipywidgets
