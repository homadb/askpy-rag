import os
import streamlit as st
from dotenv import load_dotenv

from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Set up OpenAI and Chroma
embedding = OpenAIEmbeddings(openai_api_key=openai_api_key)
db = Chroma(persist_directory="db", embedding_function=embedding)
retriever = db.as_retriever()
llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_api_key)

qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# Streamlit UI
st.set_page_config(page_title="AskPy - Python Tutor", page_icon="🐍")
st.title("🧠 AskPy: Your Python Tutor")

st.markdown("Ask a question based on your uploaded Python PDFs 📚")

query = st.text_input("💬 Enter your question:")
if query:
    with st.spinner("Thinking..."):
        response = qa_chain.run(query)
    st.markdown("### 💡 Answer:")
    st.write(response)
