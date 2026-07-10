import os
import subprocess

import streamlit as st

st.set_page_config(
    page_title="RAG PDF Chatbot",
    page_icon="📚",
    layout="wide"
)

st.title("📚 RAG PDF Chatbot")

st.sidebar.title("Upload PDF")

uploaded_file = st.sidebar.file_uploader(
    "Choose a PDF",
    type="pdf"
)

if uploaded_file is not None:

    os.makedirs("documents", exist_ok=True)

    pdf_path = os.path.join("documents", uploaded_file.name)

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.sidebar.success("PDF Uploaded Successfully")

    if st.sidebar.button("Build Database"):

        with st.spinner("Creating Embeddings..."):

            subprocess.run(
                ["python", "create_database.py"],
                check=True
            )

        st.sidebar.success("Database Created Successfully!")

st.divider()

question = st.chat_input("Ask anything about your PDF")

if question:

    with st.chat_message("user"):
        st.write(question)

    result = subprocess.run(
        ["python", "main.py"],
        input=question + "\n0\n",
        text=True,
        capture_output=True
    )

    answer = result.stdout

    with st.chat_message("assistant"):
        st.write(answer)