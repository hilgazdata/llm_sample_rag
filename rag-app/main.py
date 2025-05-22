from rag.ingest import ingest_data
from rag.qa import build_qa
from monitor import log_query_and_check_drift

if __name__ == "__main__":
    print("🔍 Ingesting and building QA system...")
    ingest_data()
    qa = build_qa()

    while True:
        query = input("You: ")
        if query.lower() in ("exit", "quit"):
            break

        # Log query and check for drift before answering
        log_query_and_check_drift(query)

        result = qa.invoke(query)
        print(f"AI: {result}")
