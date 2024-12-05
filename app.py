import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# Loading the Environment Variables
load_dotenv()
os.environ["LANGCHAIN_APIKEY"] = os.getenv("LANGCHAIN_APIKEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_PROJECT="simple-gen-Ai app "

# Creating the ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        ("system" , "Hey you are a helpfull physicst who is good in answering questions please provide the answer based on the questions"),
        ("user", "Question{question}")
    ])


# StreamLit Framework
st.title("LangChain Demo With Google Gemma :2b")
input_text = st.text_input("Dive into Physics ask anything")

# Calling the Model 
llm = Ollama(model = 'gemma:2b')
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    response = chain.invoke({"question": input_text})  # Assuming this method exists
    st.write(response)  # Display the response

