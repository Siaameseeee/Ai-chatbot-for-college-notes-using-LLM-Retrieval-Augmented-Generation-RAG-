from fastapi import FastAPI
from pydantic import BaseModel
from rag_chain import load_rag_chain

app = FastAPI()
qa_chain = load_rag_chain()

class QueryRequest(BaseModel):
    question: str

@app.post("/chat")
def chat(request: QueryRequest):
    result = qa_chain(request.question)
    return {
        "answer": result["result"]
    }
