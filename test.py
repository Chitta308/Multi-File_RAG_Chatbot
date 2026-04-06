from src.loader import load_documents
from src.chunking import chunk_data
from src.embedding import get_embedding
from src.vector_db import create_vector_store, load_vector_store
from src.rag_pipeline import generate_answer


def main():
    print("🔹 Loading documents...")
    documents = load_documents("data")

    print("🔹 Chunking data...")
    chunks = chunk_data(documents)

    print("🔹 Creating embeddings...")
    embedding = get_embedding()

    print("🔹 Creating vector DB...")
    db = create_vector_store(chunks, embedding)

    print("✅ Setup complete!\n")

    while True:
        query = input("\n💬 Ask a question (type 'exit' to quit): ")

        if query.lower() == "exit":
            break

        answer = generate_answer(query, db)

        print("\n🤖 Answer:\n", answer)


if __name__ == "__main__":
    main()