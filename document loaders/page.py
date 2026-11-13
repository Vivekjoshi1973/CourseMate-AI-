from langchain_community.document_loaders import WebBaseLoader
url="https://www.netflix.com/in/title/80217863" # url of webpage we want to load 
data=WebBaseLoader(url)
docs=data.load()

print(len(docs))
print(docs[0].page_content)

# laoding data from a webpage 