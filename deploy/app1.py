import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage,SystemMessage,AIMessage
from dotenv import load_dotenv
import os

load_dotenv()
##Streamlit UI

st.set_page_config(page_title="Convo Q&A")
st.header("Type to chat")


chatllm=ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"),temperature=0.5)


if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages']=[
        SystemMessage(content="You are a comedian AI system")
    ]

def get_chatmodel_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer=chatllm(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))

    return answer.content


input=st.text_input("Input:",key="input")
response=get_chatmodel_response(input)

submit=st.button("Ask a question")

if submit:
    st.subheader("The response is ")
    st.write(response)