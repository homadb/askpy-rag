# 🧠 AskPy RAG

AskPy RAG is a local Python application that lets you chat with your own PDF documents using Retrieval-Augmented Generation (RAG).

Built with Streamlit, LangChain, ChromaDB, HuggingFace embeddings, and Ollama.
Run everything locally on your laptop! 🚀

## 📦 Installation

Use the package manager pip to install all required libraries.

```bash
pip install -r requirements.txt
```

You also need to install Ollama locally and pull a model:

```bash
ollama pull llama3
```

## 🛠️ Usage

Prepare your project structure like this:

```bash
askpy-rag/
├── app.py
├── notebooks/
│    ├── 01_pdf_to_db.ipynb
│    └── 02_chat_with_rag.ipynb
├── data/
│    └── tutorials/
│        ├── your_pdf_file1.pdf
│        └── your_pdf_file2.pdf
├── db/
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## 📂 1. Upload PDFs
Create a folder:

```bash
data/tutorials/
```

Upload your PDF files inside it.

Example:

```bash
data/
└── tutorials/
    ├── python_guide.pdf
    ├── machine_learning_basics.pdf
```

## ⚙️ 2. Generate Vector Database

Run the following notebook to create your ChromaDB vector store:

```bash
cd notebooks/
# Open and run 01_pdf_to_db.ipynb
```
✅ This extracts text, chunks it, embeds it, and saves it into db/.

## 🚀 3. Launch the App
From the project root:

```bash
streamlit run app.py
```
Open your browser and visit:
http://localhost:8501
Now you can chat with your own PDFs! 🎯

## 📚 How It Works

PDFs are split into small text chunks.

Each chunk is converted into vector embeddings.

Vectors are stored in ChromaDB.

When you ask a question:

It is embedded.

Relevant chunks are retrieved.

Ollama generates an answer based on your documents.

## 🙌 Contributing

Pull requests are welcome!
For major changes, please open an issue first to discuss what you want to improve.

Make sure to update the docs and tests as needed.

## 📄 License

This project is licensed under the MIT License.

## ✨ Notes

You must manually create a data/tutorials/ folder and upload your PDFs before running.

Ollama must be running locally.

HuggingFace model (all-MiniLM-L6-v2) will be automatically downloaded on first run.