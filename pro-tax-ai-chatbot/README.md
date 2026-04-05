---

# 🤖 Dynamic PDF RAG Assistant - Multilingual Analysis

This project implements a flexible and high-performance **Retrieval-Augmented Generation (RAG)** pipeline. Unlike static systems, this assistant dynamically processes provided PDF documents (such as the Azerbaijan National AI Strategy or legal codes) to provide context-aware, accurate answers.

**App Link:** [https://pro-tax-ai-chatbot.streamlit.app/](https://pro-tax-ai-chatbot.streamlit.app/)

## 🚀 Key Features

* **Dynamic Content Parsing:** Automatically extracts, cleans, and structures text from any uploaded or provided PDF document.
* **Intelligent Chunking:** Implements semantic segmenting (500-character blocks with overlap) to ensure no context is lost between sections.
* **Multilingual Vector Search:** Powered by `FAISS` and `sentence-transformers`, enabling the system to understand and retrieve information in **Azerbaijani**, English, and 50+ other languages.
* **Precision Reranking:** Uses a **Cross-Encoder** (`ms-marco-MiniLM-L-6-v2`) to re-evaluate the top 10 search results, ensuring the LLM receives only the most relevant context.
* **Llama 3.3 70B Integration:** Connects via **Groq API** for ultra-fast response generation while strictly adhering to the provided document's context.
* **User-Centric UI:** A streamlined **Streamlit** interface featuring an interactive chat environment.

## 🛠️ Technical Stack

* **Core Logic:** Python
* **Vector Engine:** FAISS (Facebook AI Similarity Search)
* **Embeddings:** paraphrase-multilingual-MiniLM-L12-v2
* **Inference:** Groq Cloud API
* **Front-end:** Streamlit

## 📋 Installation & Setup

1.  **Clone the Repo:**
    ```bash
    git clone https://github.com/rafiveyisov/MyLLM.git
    cd MyLLM/pro-tax-ai-chatbot
    ```

2.  **Install Requirements:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure API Keys:**
    Add your `GROQ_API_KEY` to your system environment variables or a `.env` file.

4.  **Launch:**
    ```bash
    streamlit run app.py
    ```

## 🌐 Deployment Note
For **Streamlit Cloud** deployment, remember to add your `GROQ_API_KEY` in the **Secrets** section of the Streamlit dashboard to ensure the backend can communicate with the Groq API.
