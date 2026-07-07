from langchain_chroma import Chroma
from langchain_mistralai import MistralAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

from langchain_core.documents import Document

docs = [
    Document(page_content="Python is a versatile, high-level programming language known for its simple, readable syntax that resembles everyday English")
]

embedding_model = MistralAIEmbeddings(
    model="mistral-embed")

vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embedding_model,
    persist_directory="chroma-db"
)