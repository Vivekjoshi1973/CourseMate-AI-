from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter 
# character based splitting 
splitter=CharacterTextSplitter( # see sepearator and decide chunk size based on that 
    separator="",
    chunk_size=500,
    chunk_overlap=1

)

data=TextLoader("./document loaders/neural_networks_overview.txt")
docs=data.load()
# print(docs[0]) # to se very first document inside list 
# print(docs[0].page_content) # to see only page content 
# print(len(docs)) #print length

chunks=splitter.split_documents(docs)
print(len(chunks))


for i in chunks:
    print(i.page_content)
    print()



