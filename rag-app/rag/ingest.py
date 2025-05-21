import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

def load_pdfs_from_folder(folder_path):
    docs = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)
            loader = PyPDFLoader(file_path)
            docs.extend(loader.load())
    return docs

def ingest_data(data_path="data/"):
    documents = load_pdfs_from_folder(data_path)
    if not documents:
        raise ValueError("No PDF documents found in the specified directory.")
    
    embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = Chroma.from_documents(documents, embedding, persist_directory="db/")
    vectordb.persist()
    return vectordb
