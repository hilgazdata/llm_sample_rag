from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

def build_qa_with_memory(retriever, llm):
    from langchain.chains.question_answering import load_qa_chain

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=False
    )
    return qa_chain
