from dotenv import load_dotenv
from langchain_mistralai import MistralAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

load_dotenv()

embedding_model =MistralAIEmbeddings (
    model = "mistral-embed" )

vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding_model
)

retriever = vectorstore.as_retriever(
    search_type = "mmr",
    search_kwargs = {
        "k" : 4 ,
        "fetch_k" : 10 , 
         "lambda_multi" :0.5   
     }
)

llm = ChatMistralAI( model= "mistral-small-2506")


prompt = ChatPromptTemplate.from_messages(
    [
        ("system",
         """ you are a great helpful ai assistent
         use only a provided context the questions 
         
         if the answer is not then , 
         say : i could'nt answer """

        ),
        ("human",
         """ context:
              {context}
         
         Question:
         
         {Question}
         """

        )
    ]
)

print("rag system created")

print("print 0 to exist")

while True:
     query=input("you:")
     if query =="0":
          break
     
     docs=retriever.invoke(query)

     context = "\n\n".join(
          [doc.page_content for doc in docs]
     )
     final_prompt = prompt.invoke({
         "context" : context,
         "Question": query
    })
     response = llm.invoke(final_prompt)

     print(f"\n AI: {response.content}")