📚 AskPy RAG — Chat with Your Python PDFs!
Build your own offline RAG (Retrieval-Augmented Generation) app to chat with your personal books and tutorials! 🚀

🛠 Tech Stack

Part	Technology
Frontend	Streamlit
Embedding Model	HuggingFace sentence-transformers/all-MiniLM-L6-v2
Vector Database	ChromaDB
LLM (Local Model)	Ollama (e.g., Llama3, Mistral, Phi3)
Framework	LangChain
Environment	Python 3.12 + venv
🏗️ Project Structure
bash
Copy
Edit
askpy-rag/
│
├── app.py                  # Main Streamlit app (chat interface)
├── notebooks/               # Helper notebooks
│    ├── 01_pdf_to_db.ipynb     # Process PDFs ➔ Chunks ➔ Embeddings ➔ Vector DB
│    └── 02_chat_with_rag.ipynb # Optional: manual chat testing notebook
│
├── data/                    # Data folder
│    └── tutorials/           # (Important!) Place your PDFs here
│
├── db/                      # Chroma vector DB (auto-created after embedding)
│
├── .env                     # Your API keys and environment configs
├── .gitignore               # Exclude venv/, db/, etc.
├── requirements.txt         # Project dependencies
└── README.md                # This file
🚀 How to Run the Project
1. Install Ollama
Download and install from: ollama.ai

Then pull a local LLM model (example: Llama3):

bash
Copy
Edit
ollama pull llama3
(You can also pull lighter models like phi3, mistral, etc.)

2. Set up the Environment
bash
Copy
Edit
python -m venv venv
# activate venv
# (Linux/macOS)
source venv/bin/activate
# (Windows)
venv\Scripts\activate

# install Python libraries
pip install -r requirements.txt
3. Prepare the Vector Database
⚡ Important Step:

Create a data/tutorials/ folder manually inside your project (if not already created).

Upload your PDFs into the data/tutorials/ folder.

bash
Copy
Edit
data/
└── tutorials/
     ├── python_book.pdf
     ├── python_advanced_guide.pdf
     └── ...
Then:

Run the notebook notebooks/01_pdf_to_db.ipynb

It will:

Extract text

Split into chunks

Embed chunks

Save into ChromaDB (db/ folder)

4. Launch the Chat App
bash
Copy
Edit
streamlit run app.py
✅ The app will open at: http://localhost:8501

🧠 How It Works
PDFs ➔ Split into small readable chunks.

Chunks ➔ Embedded into dense vectors (meaning-based representations).

Saved into Chroma Vector Database.

When you ask a question:

Query ➔ Embedded ➔ Best matching chunks retrieved.

Context ➔ Sent to Ollama (local LLM) ➔ Answer generated.

💬 Result: You can "talk" to your books easily!

📈 Future Improvements
Fine-tune chunk size for better performance

Optimize retrieval settings (k, similarity_score_threshold)

Support multi-document answers

Improve UI/UX with chat history and reset button

Deploy on private server / LAN network

📜 License
This project is licensed under the MIT License.
Feel free to use, modify, and build upon it! ❤️

🚀 Ready to Build Your Own Local RAG Assistant?
Let's do it together! 🌟

⭐️ Star the Repo If You Like It!