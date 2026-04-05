# 🚀 MyLLM: Advanced RAG Ecosystem

Welcome to the **MyLLM** repository. This project showcases a collection of high-performance **Retrieval-Augmented Generation (RAG)** systems specifically optimized for multilingual document analysis and complex legal/strategic frameworks.

## 📂 Repository Structure

This repository contains two main specialized projects:

| Project | Description | Tech Stack |
| :--- | :--- | :--- |
| [**Pro-Tax AI Chatbot**](https://www.google.com/search?q=./pro-tax-ai-chatbot) | Dynamic RAG system for legal/tax document analysis. | Streamlit, FAISS, Llama 3.3 |
| [**AI Strategy RAG System**](https://www.google.com/search?q=./ai_strategy_rag_system) | Deep analysis of Azerbaijan's National AI Strategy. | Jupyter, Cross-Encoders, Groq |

-----

## 🌟 Key Features Across Projects

  * **Multilingual Semantic Search:** Uses `paraphrase-multilingual-MiniLM-L12-v2` to understand queries in **Azerbaijani**, English, and Turkish with high precision.
  * **Two-Stage Retrieval:**
    1.  **Bi-Encoder (FAISS):** Fast candidate retrieval from large document sets.
    2.  **Cross-Encoder Reranking:** Precision filtering using `ms-marco-MiniLM-L-6-v2` to ensure the most relevant context reaches the LLM.
  * **High-Speed Inference:** Integration with **Groq API** utilizing **Llama 3.3 70B** for near-instant response generation.
  * **Intelligent Chunking:** Semantic text splitting with context overlap to preserve the integrity of legal clauses and technical paragraphs.

-----

## 🛠️ Global Tech Stack

  * **Language:** Python 3.9+
  * **Vector Engine:** FAISS (Facebook AI Similarity Search)
  * **Embeddings & Reranking:** Sentence-Transformers (Hugging Face)
  * **LLM Provider:** Groq Cloud (Llama 3.3 70B)
  * **Frontend:** Streamlit & IPython Widgets

-----

## 🚀 Quick Start

### 1\. Clone the entire ecosystem

```bash
git clone https://github.com/rafiveyisov/MyLLM.git
cd MyLLM
```

### 2\. Setup Environment

Create a `.env` file in the root directory or specific project folders:

```text
GROQ_API_KEY=your_groq_api_key_here
```

### 3\. Choose a Project to Run

#### Option A: Pro-Tax AI Chatbot (Web App)

```bash
cd pro-tax-ai-chatbot
pip install -r requirements.txt
streamlit run app.py
```

**Live Demo:** [pro-tax-ai-chatbot.streamlit.app](https://pro-tax-ai-chatbot.streamlit.app/)

#### Option B: AI Strategy Analysis (Jupyter Notebook)

```bash
cd ai_strategy_rag_system
pip install -r requirements.txt
jupyter notebook RAG_Pipeline.ipynb
```

-----

## 🌐 Deployment & Secrets

When deploying any of these modules to **Streamlit Cloud**, ensure you configure the `GROQ_API_KEY` within the **Secrets** management console of your Streamlit dashboard.

-----

## 👤 Author

**Rafi Veyisov** *Machine Learning & AI Engineer* [LinkedIn](https://www.google.com/search?q=https://www.linkedin.com/in/rafiveyisov/) | [GitHub](https://www.google.com/search?q=https://github.com/rafiveyisov)

-----

*Disclaimer: These tools are designed for informational purposes and should be used as assistants for document analysis, not as a substitute for professional legal advice.*
