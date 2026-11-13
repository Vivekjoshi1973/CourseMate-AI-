from langchain_community.document_loaders import PyPDFLoader

data=PyPDFLoader("./document loaders/Technical Study Guide - Neural Networks & Backend Fundamentals.pdf")
docs =data.load()
print(len(docs)) # lenght of list is equal to number of documents in the list every page in a pdf is a document 