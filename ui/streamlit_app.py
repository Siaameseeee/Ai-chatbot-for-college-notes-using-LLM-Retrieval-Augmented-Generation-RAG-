import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(page_title="RAG Chatbot")
st.title("📄 AI RAG Chatbot")

query = st.text_input("Ask a question:")

if st.button("Ask") and query:
    response = requests.post(API_URL, json={"question": query})
    st.write("### Answer:")
    st.write(response.json()["answer"])
