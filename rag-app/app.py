import time
import streamlit as st
from rag.qa import build_qa
from rag.ingest import ingest_data
from monitor import log_query_and_check_drift
import warnings
from langchain_core._api.deprecation import LangChainDeprecationWarning

# Suppress warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)
warnings.filterwarnings("ignore", category=LangChainDeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

# App title
st.set_page_config(page_title="RAG App", layout="centered")
st.markdown("## 📄 RAG App — Ask your PDFs")

# Ingest button
with st.sidebar:
    st.markdown("### ⚙️ Controls")
    if st.button("🔄 Re-ingest PDFs"):
        with st.spinner("Re-ingesting..."):
            ingest_data()
        st.success("PDFs re-ingested!")

# Build QA chain
qa = build_qa()

# Initialize history
if "query_history" not in st.session_state:
    st.session_state.query_history = []

# Input form
with st.form("query_form"):
    query = st.text_input("💬 Enter your question:", placeholder="e.g., What is the idea of rival theories")
    submit = st.form_submit_button("Get Answer")

# If query submitted
if submit and query:
    start_time = time.time()

    with st.spinner("🧠 Thinking..."):
        result = qa.invoke(query)

    # Safe result extraction
    response_text = (
        result.get("answer")
        if isinstance(result, dict) and "answer" in result
        else str(result)
    )

    elapsed = time.time() - start_time

    # Store and display full chat log
    st.session_state.query_history.append((query, response_text))

    st.markdown("### ✅ Answer")
    st.success(response_text)

    st.markdown(f"⏱️ **Response time:** {elapsed:.2f} seconds")

    log_query_and_check_drift(query)

# Display full chat history like ChatGPT
if st.session_state.query_history:
    st.markdown("### 🧾 Conversation History")
    for q, a in reversed(st.session_state.query_history):
        with st.chat_message("user"):
            st.markdown(q)
        with st.chat_message("assistant"):
            st.markdown(a)



