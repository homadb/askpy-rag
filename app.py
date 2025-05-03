import os
import sys
from dotenv import load_dotenv
import streamlit as st

from langchain_chroma import Chroma
from langchain_ollama import Ollama
from langchain_huggingface import HuggingFaceEmbeddings

from langchain.chains import ConversationalRetrievalChain

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
model_kwargs={"device": "cpu"}  # 👈 Force CPU

# Check if the vector database directory exists
if not os.path.exists(persist_dir):
    st.error(f"❌ Vector database directory '{persist_dir}' not found. Please ensure the directory exists and contains the necessary data.")
    sys.exit(1)


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# ✅ Create retrieval QA chain
retriever = vectordb.as_retriever(search_kwargs={"k": 3})
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)


# ✅ Streamlit UI
st.set_page_config(page_title="AskPy Chat", layout="centered", page_icon="📚")
st.title("📚 AskPy Chat – Ask about Python!")

for i, (q, a) in enumerate(st.session_state.chat_history):
    st.markdown(f"**🧠 Q{i+1}:** {q}")
    st.markdown(f"**💡 A{i+1}:** {a}")

query = st.text_input("Ask a question:")

if query:
    st.markdown("⏳ **Processing your question... please wait.**")

    with st.spinner("💡 Thinking hard..."):
        try:
            docs = retriever.get_relevant_documents(query)

            # Truncate long context chunks
            MAX_CHARS = st.sidebar.slider("Max Characters per Source", 100, 1000, 500)
            short_docs = [doc.copy(update={"page_content": doc.page_content[:MAX_CHARS]}) for doc in docs]

            # Run the QA chain
            result = qa_chain({
                "question": query,
                "chat_history": st.session_state.chat_history
            })  


            st.session_state.chat_history.append((query, result["answer"]))



            # ✅ Show result
            st.success("✅ Done!")
            st.markdown(f"### 📖 Answer:\n{result['answer']}")

            # ✅ Show sources
            st.markdown("---")
            st.markdown("#### 🔍 Sources")
            for doc in short_docs:
                source = doc.metadata.get("source", "Unknown")
                content = doc.page_content.strip()

                if len(content) < 30 or not content.replace(" ", "").isalnum():
                    continue  # Skip empty/garbage chunks

                st.markdown(f"• `{source}`")
                st.markdown(f"> {content[:200]}...")

        except ValueError as e:
            st.error("❌ Error while generating response.")
            st.code(str(e))
            st.info("Try a shorter or simpler question.")

        except Exception as e:
            st.error("❌ An unexpected error occurred.")
            st.code(str(e))


if st.button("🗑️ Clear Chat"):
    if st.confirm("Are you sure you want to clear the chat history?"):
        st.session_state.chat_history = []
        st.experimental_rerun()  # Refresh the app
