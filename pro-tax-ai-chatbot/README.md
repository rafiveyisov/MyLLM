# ⚖️ Tax Code of the Republic of Azerbaijan - RAG Assistant

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline on the Tax Code PDF of the Republic of Azerbaijan.

## 🚀 Features

* **Smart Parsing:** Splits the PDF into articles and clauses with metadata.
* **Hybrid Search:** Supports both exact article lookup (via Regex) and semantic search.
* **LLM:** Uses the `Llama 3.3 70B` model via the Groq API for high-speed responses.
* **UI:** Simple and efficient chat interface built with Streamlit.

## 🛠 Installation

1. Install the required libraries:

   ```bash
   pip install streamlit pdfplumber faiss-cpu sentence-transformers python-dotenv groq
   ```

2. Create a `.env` file and add your Groq API key:

   ```
   GROQ_API_KEY=your_api_key
   ```

3. Place the PDF file at:

   ```
   data/your_file.pdf
   ```

4. Run the application:

   ```bash
   streamlit run app.py
   ```
