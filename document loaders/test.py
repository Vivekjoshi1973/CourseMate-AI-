from langchain_community.document_loaders import TextLoader
data=TextLoader("./document loaders/neural_networks_overview.txt")
docs=data.load()
print(docs[0]) # to se very first document inside list 
print(docs[0].page_content) # to see only page content 
print(len(docs)) #print length



