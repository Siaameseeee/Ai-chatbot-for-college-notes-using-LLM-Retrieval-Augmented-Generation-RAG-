from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

text = "Machine learning is a subset of AI"
embedding = model.encode(text)

print("Embedding created successfully")
