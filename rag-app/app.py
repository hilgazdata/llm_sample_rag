import streamlit as st
from rag.qa import build_qa
from rag.ingest import ingest_data
from monitor import log_query_and_check_drift

st.title("RAG App — Ask your PDFs")

# Re-ingest PDFs
if st.button("Re-ingest PDFs"):
    with st.spinner("Ingesting PDFs..."):
        ingest_data()

# Build QA chain
qa = build_qa()

# Initialize session history
if "query_history" not in st.session_state:
    st.session_state.query_history = []

# Input box for question
query = st.text_input("Enter your question:")

if query:
    with st.spinner("Getting answer..."):
        result = qa.invoke(query)
        st.markdown("### Answer:")
        st.write(result)

        # Store query and log for drift
        st.session_state.query_history.append(query)
        log_query_and_check_drift(query)

