def retrieve_docs(query, db, k=3):
    return db.similarity_search(query, k=k)