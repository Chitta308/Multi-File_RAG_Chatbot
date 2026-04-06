from src.retriever import retrieve_docs
from src.llm import get_llm


def generate_answer(query, db):
    docs = retrieve_docs(query, db)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are a helpful AI assistant.

Answer ONLY from the given context.
If the answer is not present, say "I don't know".

Context:
{context}

Question:
{query}
"""

    model = get_llm()
    response = model.generate_content(prompt)

    return response.text