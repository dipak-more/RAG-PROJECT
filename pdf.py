from langchain_community.document_loaders import PyPDFLoader
data = PyPDFLoader("documents/full_llm.pdf")

docs = data.load()

print(len(docs))
