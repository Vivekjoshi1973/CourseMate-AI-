
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import TextLoader 
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader




load_dotenv()

# data=TextLoader("./document loaders/neural_networks_overview.txt") # loading data using text loader ( loading a .txt file)
data=PyPDFLoader("./document loaders/Technical Study Guide - Neural Networks & Backend Fundamentals.pdf")  # loading a .pdf file using pypdfloader 
docs=data.load() # making a object of our file
template=ChatPromptTemplate.from_messages(
    [("system","you are a AI that summarizes the text"),
     ("human","{data}")] # human is sending text to system
)

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3
)

prompt = template.format_messages(data=docs[0].page_content) # fetching pagecontent from file and giving it to chat prompt tempalte 
# we are only semding a part of pdf one document only due the size of context window it means we cant send a lot of data at once 

result = model.invoke(prompt)

print(result.content)
