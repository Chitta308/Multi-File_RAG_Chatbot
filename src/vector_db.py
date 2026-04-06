from langchain.vectorstores import FAISS
import os


def create_vector_store(docs, embedding):
    db = FAISS.from_documents(docs, embedding)

    if not os.path.exists("vector_store"):
        os.makedirs("vector_store")

    db.save_local("vector_store")
    return db


def load_vector_store(embedding):
    return FAISS.load_local("vector_store", embedding, allow_dangerous_deserialization=True)