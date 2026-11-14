from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import TokenTextSplitter
# # using Token based text splitting

from langchain_text_splitters import RecursiveCharacterTextSplitter
# using recursive splitting 
data=PyPDFLoader("./document loaders/Technical Study Guide - Neural Networks & Backend Fundamentals.pdf")
docs =data.load()

# splitter=TokenTextSplitter(
#     chunk_size=1000,
#     chunk_overlap=10
# )

splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=10
)


# print(len(docs)) # lenght of list is equal to number of documents in the list every page in a pdf is a document 

chunks=splitter.split_documents(docs)
print(len(chunks))
print(chunks[0])
# print(chunks[0].page_content)
