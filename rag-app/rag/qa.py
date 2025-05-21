from langchain.chains import RetrievalQA
from langchain.llms import Ollama
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

def build_qa():
    embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = Chroma(persist_directory="db/", embedding_function=embedding)
    retriever = vectordb.as_retriever()

    llm = Ollama(model="llama3")
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa
