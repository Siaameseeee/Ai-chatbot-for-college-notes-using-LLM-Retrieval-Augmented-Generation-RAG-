from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader("data/sample_notes.pdf")
documents = loader.load()

print("Document loaded successfully")
