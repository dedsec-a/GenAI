import os
from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from fastapi import FastAPI
from langserve import add_routes

load_dotenv()
# Getting the Gorq Api key 
gorq_apikey = os.getenv("GROQ_APIKEY")


model = ChatGroq(model= "gemma2-9b-it",groq_api_key =gorq_apikey)

# Defining the ChatPrompt tempate 

genric_template = "Convert the Follwing into {language}"

genric_template = "Translate the Following into {language} :"
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", genric_template),
        ("user", "{text}")
    ]
)

parser = StrOutputParser()

chain = prompt | model | parser

app = FastAPI(title= "LangChain Server",
              version= "1.0",
              description= "A simple API server using Langchain runnable interfaces")


add_routes(
    app=app,
    runnable= chain,
    path= "/chain"


)

if __name__ == "__main__" :
    import uvicorn
    uvicorn.run(app=app , host= "localhost" , port= 8000)
