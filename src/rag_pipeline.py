from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM

from src.embeddings import get_embedding_model
from src.prompt_template import custom_prompt


memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)


def load_rag_pipeline():

    embeddings = get_embedding_model()

    vectorstore = FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 1}
    )

    llm = OllamaLLM(
    model="tinyllama",
    temperature=0.3

    )

    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        combine_docs_chain_kwargs={
            "prompt": custom_prompt
        }
    )

    return qa_chain