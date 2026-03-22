from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

# Load PDF
loader = PyPDFLoader("data/sample_notes.pdf")
documents = loader.load()

# Split into chunks
text_splitter = CharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
texts = text_splitter.split_documents(documents)

print("Text split into chunks")

# Create embeddings
embeddings = HuggingFaceEmbeddings()

# Store in FAISS
vectorstore = FAISS.from_documents(texts, embeddings)

print("Embeddings stored in FAISS")

# Ask a question
query = "What is machine learning?"

docs = vectorstore.similarity_search(query, k=3)

print("\nTop relevant answers:\n")

for i, doc in enumerate(docs):
    print(f"{i+1}. {doc.page_content}\n")
