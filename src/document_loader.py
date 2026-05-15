from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader


def load_documents():

    text_loader = DirectoryLoader(
        "data",
        glob="**/*.txt",
        loader_cls=TextLoader
    )

    pdf_loader = DirectoryLoader(
        "data",
        glob="**/*.pdf",
        loader_cls=PyPDFLoader
    )

    text_documents = text_loader.load()

    pdf_documents = pdf_loader.load()

    documents = text_documents + pdf_documents

    return documents