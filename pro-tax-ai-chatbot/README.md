# ⚖️ Tax Code of the Republic of Azerbaijan - RAG Assistant

This project implements a sophisticated **Retrieval-Augmented Generation (RAG)** pipeline applied to the official Tax Code PDF of the Republic of Azerbaijan. It combines semantic search with high-speed LLM generation to provide accurate legal answers.

**App Link:** [https://pro-tax-ai-chatbot.streamlit.app/](https://pro-tax-ai-chatbot.streamlit.app/)

## 🚀 Features

* **Advanced Data Ingestion:** Extracts and cleans text from complex legal PDF documents using `pdfplumber`.
* **Hybrid Retrieval:** Combines exact article lookup with semantic vector search using **FAISS**.
* **Reranking Pipeline:** Utilizes a **Cross-Encoder** (`ms-marco-MiniLM-L-6-v2`) to prioritize the most relevant legal clauses before generation.
* **Multilingual Embeddings:** Powered by `paraphrase-multilingual-MiniLM-L12-v2` for high accuracy in Azerbaijani technical text.
* **High-Performance LLM:** Integrates **Llama 3.3 70B** via the Groq API for near-instant, context-aware responses.
* **Interactive UI:** A clean, user-friendly chat interface built with **Streamlit**.

## 🛠️ Installation & Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rafiveyisov/MyLLM.git
   cd MyLLM/pro-tax-ai-chatbot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Variables:**
   Create a `.env` file in the `pro-tax-ai-chatbot` folder:
   ```text
   GROQ_API_KEY=your_actual_api_key_here
   ```

4. **Data Placement:**
   Ensure your Tax Code PDF is placed within the `pro-tax-ai-chatbot/` directory as specified in the source code.

5. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## 🌐 Deployment Note
When deploying to **Streamlit Cloud**, ensure that your `GROQ_API_KEY` is added to the **Secrets** management tool in the Streamlit dashboard to maintain security.
