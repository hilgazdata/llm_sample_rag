import streamlit as st
from rag.qa import build_qa  

st.title("RAG App — Ask your PDFs")

query = st.text_input("Enter your question:")

qa = build_qa()

if query:
    with st.spinner("Getting answer..."):
        result = qa.invoke(query)  
    st.markdown("### Answer:")
    st.write(result)
