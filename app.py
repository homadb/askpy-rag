import os
from dotenv import load_dotenv
import streamlit as st

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_community.llms import Together

# ✅ Load env variables
load_dotenv()
together_api_key = os.getenv("TOGETHER_API_KEY")

# ✅ Set up LLM
llm = Together(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",  # or "Qwen/Qwen1.5-14B-Chat"
    temperature=0.7,
    together_api_key=together_api_key
)

# ✅ Load vector DB
persist_dir = "db"
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectordb = Chroma(persist_directory=persist_dir, embedding_function=embedding)

# ✅ Create retrieval QA chain
retriever = vectordb.as_retriever(search_kwargs={"k": 2})
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

# ✅ Streamlit UI
st.set_page_config(page_title="AskPy Chat", layout="centered")
st.title("📚 AskPy Chat – Ask about Python!")

query = st.text_input("Ask a question:")

if query:
    with st.spinner("💬 Thinking..."):
        try:
            result = qa_chain(query)
            st.markdown(f"### 📖 Answer:\n{result['result']}")

            # Show sources (optional)
            st.markdown("---")
            st.markdown("#### 🔍 Sources")
            for doc in result['source_documents']:
                st.markdown(f"• `{doc.metadata.get('source', 'Unknown')}`")
                st.markdown(f"> {doc.page_content[:200]}...")

        except ValueError as e:
            st.error("❌ Error while generating response.")
            st.code(str(e))
            st.info("Try a shorter or simpler question — the context may be too long for the Together.ai model.")

