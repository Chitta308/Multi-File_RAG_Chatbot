import os
import pandas as pd
from docx import Document
from pypdf import PdfReader


def load_documents(data_path="data"):
    documents = []

    for file in os.listdir(data_path):
        file_path = os.path.join(data_path, file)

        try:
            if file.endswith(".pdf"):
                reader = PdfReader(file_path)
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        documents.append(text)

            elif file.endswith(".csv"):
                df = pd.read_csv(file_path)
                documents.append(df.to_string())

            elif file.endswith(".xlsx"):
                df = pd.read_excel(file_path)
                documents.append(df.to_string())

            elif file.endswith(".docx"):
                doc = Document(file_path)
                text = "\n".join([p.text for p in doc.paragraphs])
                documents.append(text)

        except Exception as e:
            print(f"Error reading {file}: {e}")

    return documents