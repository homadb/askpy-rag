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
    model="mistralai/Mistral-7B-Instruct-v0.1",
    temperature=0.7,
    top_k=50,
    top_p=0.95,
    repetition_penalty=1.1,
    together_api_key=together_api_key,
)

# ✅ Load vector DB
persist_dir = "db"
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectordb = Chroma(persist_directory=persist_dir, embedding_function=embedding)

# ✅ Create retrieval QA chain
retriever = vectordb.as_retriever(search_kwargs={"k": 3})
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
        result = qa_chain(query)
        st.markdown(f"### 📖 Answer:\n{result['result']}")

        # Show sources (optional)
        st.markdown("---")
        st.markdown("#### 🔍 Sources")
        for doc in result['source_documents']:
            st.markdown(f"• `{doc.metadata.get('source', 'Unknown')}`")
            st.markdown(f"> {doc.page_content[:200]}...")
