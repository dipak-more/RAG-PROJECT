from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_mistralai import MistralAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()

import os

pdf_folder = "documents"

pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]

if not pdf_files:
    raise FileNotFoundError("No PDF found in the documents folder.")

pdf_path = os.path.join(pdf_folder, pdf_files[0])

data = PyPDFLoader(pdf_path)
docs = data.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size= 1000,
    chunk_overlap= 200,
)

chunks = splitter.split_documents(docs)

embedding_model = MistralAIEmbeddings(
    model="mistral-embed")

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="chroma_db"
)

