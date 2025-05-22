import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

def get_project_root():
    # Go up one level from the current file (rag/ -> rag-app/)
    return os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def load_pdfs_from_folder(folder_path):
    docs = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)
            print(f"Loading: {file_path}")  # Debug
            loader = PyPDFLoader(file_path)
            docs.extend(loader.load())
    return docs

def ingest_data(data_path="data/", persist_path="db/"):
    root_dir = get_project_root()
    data_path = os.path.join(root_dir, data_path)
    persist_path = os.path.join(root_dir, persist_path)

    print("Resolved data path:", data_path)
    print("Resolved persist path:", persist_path)
    print("Files in data path:", os.listdir(data_path))

    documents = load_pdfs_from_folder(data_path)
    if not documents:
        raise ValueError("No PDF documents found in the specified directory.")

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)

    embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = Chroma.from_documents(chunks, embedding, persist_directory=persist_path)
    vectordb.persist()
    return vectordb



