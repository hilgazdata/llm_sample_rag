from rag.ingest import ingest_data
from rag.qa import build_qa

if __name__ == "__main__":
    print("🔍 Ingesting and building QA system...")
    ingest_data()
    qa = build_qa()

    while True:
        query = input("You: ")
        if query.lower() in ("exit", "quit"): break
        result = qa.invoke(query)
        print(f"AI: {result}")
