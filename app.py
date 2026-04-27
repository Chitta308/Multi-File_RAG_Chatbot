import streamlit as st
import os
import tempfile

from src.loader import load_documents
from src.chunking import chunk_data
from src.embedding import get_embedding
# from src.vector_db import create_vector_store, load_vector_store
# from src.vector_store_db import create_vector_store, load_vector_store
from src.vector_db import create_vector_store, load_vector_store
from src.rag_pipeline import generate_answer


st.set_page_config(page_title="RAG Chatbot", layout="wide")

st.title("📚 Multi-File RAG Chatbot (Gemini + FAISS)")

# -------------------------
# Upload Section
# -------------------------
uploaded_files = st.file_uploader(
    "Upload your files (PDF, CSV, Excel, Word)",
    type=["pdf", "csv", "xlsx", "docx"],
    accept_multiple_files=True
)

# -------------------------
# Process Button
# -------------------------
if st.button("🔄 Process Files"):
    if uploaded_files:
        with tempfile.TemporaryDirectory() as temp_dir:

            # Save uploaded files
            for file in uploaded_files:
                file_path = os.path.join(temp_dir, file.name)
                with open(file_path, "wb") as f:
                    f.write(file.getbuffer())

            st.info("📥 Loading documents...")
            documents = load_documents(temp_dir)

            st.info("✂️ Chunking...")
            chunks = chunk_data(documents)

            st.info("🧠 Creating embeddings...")
            embedding = get_embedding()

            st.info("📦 Creating vector DB...")
            db = create_vector_store(chunks, embedding)

            st.success("✅ Files processed successfully!")

    else:
        st.warning("Please upload at least one file.")

# -------------------------
# Chat Section
# -------------------------
st.subheader("💬 Ask Questions")

query = st.text_input("Enter your question:")

if query:
    try:
        embedding = get_embedding()
        db = load_vector_store(embedding)

        answer = generate_answer(query, db)

        st.markdown("### 🤖 Answer")
        st.write(answer)

    except Exception as e:
        st.error("⚠️ Please process files first!")
