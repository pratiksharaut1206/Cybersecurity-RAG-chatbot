import streamlit as st
from dotenv import load_dotenv

from src.rag_pipeline import load_rag_pipeline


load_dotenv()

st.set_page_config(
    page_title="Cybersecurity AI Assistant",
    page_icon="🛡️",
    layout="centered"
)


st.markdown(
    """
    <style>

    .stApp {
        background-color: #f8fafc;
        color: #0f172a;
        font-family: 'Segoe UI', sans-serif;
    }

    h1 {
        text-align: center;
        color: #0f172a;
    }

    .subtitle {
        text-align: center;
        color: #64748b;
        margin-bottom: 30px;
    }

    [data-testid="stChatMessage"] {
        background-color: white;
        border-radius: 14px;
        padding: 14px;
        margin-bottom: 12px;
        border: 1px solid #e2e8f0;
    }

    section[data-testid="stSidebar"] {
        background-color: white;
    }

    </style>
    """,
    unsafe_allow_html=True
)


st.title("🛡️ Cybersecurity AI Assistant")

st.markdown(
    """
    <div class='subtitle'>
    AI-powered cybersecurity knowledge assistant
    </div>
    """,
    unsafe_allow_html=True
)





@st.cache_resource
def initialize_rag():
    return load_rag_pipeline()


qa_chain = initialize_rag()


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


query = st.chat_input("Ask cybersecurity question")


if query:

    st.session_state.messages.append(
        {"role": "user", "content": query}
    )

    with st.chat_message("user"):
        st.markdown(query)

    response = qa_chain.invoke(
        {"question": query}
    )

    answer = response["answer"]

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    with st.chat_message("assistant"):
        st.markdown(answer)