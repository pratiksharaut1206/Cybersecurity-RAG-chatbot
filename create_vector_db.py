from src.document_loader import load_documents
from src.chunking import split_documents
from src.embeddings import get_embedding_model
from src.vector_store import create_vectorstore


print("Loading documents...")
documents = load_documents()

print("Splitting documents...")
chunks = split_documents(documents)

print(f"Total chunks created: {len(chunks)}")

print("Loading embedding model...")
embeddings = get_embedding_model()

print("Creating FAISS vector database...")
create_vectorstore(chunks, embeddings)

print("Vector database created successfully!")