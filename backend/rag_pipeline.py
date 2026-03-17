from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter

# Load PDF
loader = PyPDFLoader("data/sample_notes.pdf")
documents = loader.load()

print("Document loaded successfully")

# Split text into chunks
text_splitter = CharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

texts = text_splitter.split_documents(documents)

print(f"Total chunks created: {len(texts)}")
