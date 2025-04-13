
# 🧠 AskPy RAG – Your Personal Python Tutor (RAG-Based)

This project is a **Retrieval-Augmented Generation (RAG)** pipeline that allows you to upload Python learning PDFs and then ask questions using OpenAI’s GPT-3.5. It extracts knowledge from your documents, embeds them into a vector database (ChromaDB), and lets you interact with them via natural language queries.

---

## 🔧 Features

- Upload and parse PDF Python tutorials/books
- Embed text chunks using OpenAI Embeddings
- Store and retrieve chunks with ChromaDB
- Ask questions with GPT-3.5 powered answers
- 100% local processing of your PDFs
- Lightweight setup using `venv`

---

## 📂 Project Structure

```
askpy-rag/
├── data/                  # Your uploaded Python PDFs
├── db/                    # Vector database storage (Chroma)
├── notebooks/
│   ├── 01_ingest_and_embed.ipynb   # Loads, chunks, and embeds PDFs
│   └── 02_rag_qa_openai.ipynb      # Question-answering notebook
├── .env                   # Your OpenAI API key (not tracked in Git)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/homadb/askpy-rag.git
cd askpy-rag
```

### 2. Create and Activate Virtual Environment

```bash
python3 -m venv ragenv
source ragenv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add PDF Files

Place your Python tutorial PDFs in the `data/` folder.

### 5. Add Your OpenAI API Key

Create a `.env` file in the project root:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

> ⚠️ Do not share or commit this file.

---

## 🧪 Usage

### Step 1: Ingest and Embed PDFs

Run:

```bash
python notebooks/01_ingest_and_embed.py
```

or open the notebook in Jupyter.

### Step 2: Ask Questions

Run:

```bash
python notebooks/02_rag_qa_openai.py
```

You'll be prompted to enter Python questions like:

- “How do I define a function in Python?”
- “What is a for loop?”
- “Difference between list and tuple?”

---

## ✅ Example Questions to Try

- How do I open a file in Python?
- What is the use of the `def` keyword?
- Explain how loops work in Python.

---

## ✨ Future Ideas

- Add Streamlit UI for a simple web interface
- Improve chunking using Markdown headers
- Add PDF titles as metadata for better traceability

---

## 📜 License

This project is open-source and made for educational purposes.

---

Made with 💡 by Homi.
