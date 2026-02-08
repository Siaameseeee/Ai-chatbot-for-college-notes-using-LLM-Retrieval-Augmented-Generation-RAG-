Root Repository (rag-chatbot/)
Acts as the main container for the entire project

Organizes data, logic, backend, and UI separately

This top-level directory ensures the project remains modular and easy to maintain. By separating concerns at the root level, the repository follows a professional structure suitable for academic evaluation and future scalability.

data/docs/
Stores all college notes in PDF format

Supports lecture notes, scanned handwritten notes, and slides

This folder represents the raw academic input of the system. Notes stored here are loaded by the application using a PDF loader (conceptually like PyPDFLoader("data/docs/file.pdf")) and can be updated without modifying any code.

embeddings/faiss_index/
Contains vectorized representations of notes

Acts as the chatbot’s long-term memory

Once notes are processed, they are converted into embeddings and stored locally in FAISS using logic similar to FAISS.save_local(...). This allows fast semantic retrieval and avoids reprocessing documents every time the system runs.

app/ingest.py
Loads PDF notes

Splits text into overlapping chunks

Generates embeddings and stores them in FAISS

This file performs the one-time knowledge creation process. Text is split using a strategy like chunk_size=1000 with overlap to preserve context, ensuring that academic explanations remain complete and accurate during retrieval.

app/rag_chain.py
Loads the vector database

Retrieves relevant note sections

Connects retrieval with the language model

This module is the core reasoning engine of the chatbot. When a question is asked, it retrieves the most relevant chunks (for example, k=3) and passes them to the LLM with deterministic settings such as temperature=0, ensuring syllabus-bound and hallucination-free answers.

app/api.py
Exposes chatbot functionality via REST API

Accepts questions and returns answers

The API acts as a bridge between the user interface and the AI logic. Requests like /chat send the student’s question to the RAG pipeline and return a structured response, enabling easy integration with web or mobile interfaces.

ui/streamlit_app.py
Provides a simple chat interface

Sends questions to the backend API

This file handles user interaction only. Using Streamlit elements such as st.text_input(), it allows students to ask questions in natural language and view responses without dealing with backend complexity.

.env
Stores API keys securely

Prevents hardcoding sensitive information

The environment file keeps credentials like the LLM API key separate from the codebase, improving security and making the repository safe for public sharing.

requirements.txt
Lists all required Python libraries

Ensures reproducible setup

This file allows anyone to recreate the project environment using a single installation command, ensuring consistency across different systems.

.gitignore
Excludes sensitive and generated files

Keeps the repository clean

Files such as .env, cached data, and vector indexes are ignored to avoid security risks and unnecessary clutter in version control.

README.md
Explains project purpose and usage

Guides setup and execution

The README serves as the first point of reference for evaluators, developers, or contributors, clearly describing how the chatbot works and how it can be run.

One-Line Summary (Exam Friendly)
This repository is structured to cleanly separate data ingestion, vector storage, retrieval-based reasoning, backend communication, and user interaction, enabling an accurate and scalable AI chatbot for querying college notes using Retrieval-Augmented Generation.
