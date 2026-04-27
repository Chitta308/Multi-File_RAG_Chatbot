# from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain.schema import Document
from langchain_core.documents import Document


def chunk_data(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=10000,
        chunk_overlap=1000
    )

    docs = [Document(page_content=text) for text in documents]

    return splitter.split_documents(docs)
