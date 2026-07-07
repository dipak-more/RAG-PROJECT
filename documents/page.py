from langchain_community.document_loaders import WebBaseLoader

url = "https://www.apple.com/in/store?afid=p240%7Cgo~cmp-11116556120~adg-109516736339~ad-799103628877_kwd-297832030443~dev-c~ext-~prd-~mca-~nt-search&cid=aos-in-kwgo-txt-brand-brand--"

data =WebBaseLoader(url)

docs=data.load()

print(docs[0].page_content)
