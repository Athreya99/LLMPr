from langchain.llms import OpenAI 
import os
from dotenv import load_dotenv
from langchain.chains import LLMChain

load_dotenv()

import streamlit as st

##Function to load OpenAI MOdel and get response

def get_openai_response(question):
    llm=OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
    response=llm.invoke(question)
    
    return response
#Streamlit
    
st.set_page_config(page_title='Q&A demo')
st.header("Langchain APP")


input=st.text_input("Input: ",key=input)

response=get_openai_response(input)
submit=st.button("Generate")

if submit:
    st.subheader("The response is")
    st.write(response)