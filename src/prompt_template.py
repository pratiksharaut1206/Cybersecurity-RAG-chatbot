from langchain.prompts import PromptTemplate


custom_prompt = PromptTemplate(
    input_variables=["context", "question"],

    template="""
You are a cybersecurity assistant.

Answer the question in a clear and professional way using the context below.

Context:
{context}

Question:
{question}

Answer:
"""
)