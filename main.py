from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
load_dotenv()

data = TextLoader("documents/deepl.pdf")
docs = data.load()

splitter = RecursiveCharacterTextSplitter(
    chunks_size= 1000,
    chunk_overlap= 200,
)

chunks = splitter.split_documents(docs)
template = ChatPromptTemplate.from_messages(
    [("system","you are a ai that summarizes the text"),
     "human","{data}"]
)
 
model = ChatMistralAI(model = "mistral-small-2603")

prompt = template.format_messages(data = docs[0].page_content)

result = model.invoke(prompt)

print(result.content)
