import os
from dotenv import load_dotenv
import streamlit as st

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_ollama import OllamaLLM

import os

# Disable Streamlit file watcher on libraries
os.environ["STREAMLIT_WATCH_FILE_SYSTEM"] = "false"


# ✅ Set up LLM
llm = OllamaLLM(
    model="llama2",
    temperature=0.7
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
    chain_type="map_reduce",  # 🔥 safer for long contexts
    return_source_documents=True
)

# ✅ Streamlit UI
st.set_page_config(page_title="AskPy Chat", layout="centered")
st.title("📚 AskPy Chat – Ask about Python!")

query = st.text_input("Ask a question:")

if query:
    st.markdown("⏳ **Processing your question... please wait.**")

    with st.spinner("💡 Thinking hard..."):
        try:
            docs = retriever.get_relevant_documents(query)

            # Truncate long context chunks
            MAX_CHARS = 500
            short_docs = [doc.copy(update={"page_content": doc.page_content[:MAX_CHARS]}) for doc in docs]

            # Run the QA chain
            result = qa_chain.invoke({"query": query})


            # ✅ Show result
            st.success("✅ Done!")
            st.markdown(f"### 📖 Answer:\n{result['result']}")

            # ✅ Show sources
            st.markdown("---")
            st.markdown("#### 🔍 Sources")
            for doc in short_docs:
                st.markdown(f"• `{doc.metadata.get('source', 'Unknown')}`")
                st.markdown(f"> {doc.page_content[:200]}...")

        except ValueError as e:
            st.error("❌ Error while generating response.")
            st.code(str(e))
            st.info("Try a shorter or simpler question.")
