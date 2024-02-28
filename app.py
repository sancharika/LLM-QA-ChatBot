from langchain_community.llms import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os
api_key = os.getenv('OPENAI_API_KEY')
load_dotenv()

def get_openai_response(question):
    llm=OpenAI(openai_api_key=api_key,
    temperature=0.6)
    response=llm(question)
    return response

st.set_page_config(page_title="Q&A")
st.header("Langchain Application")

input = st.text_input("Input: ", key="input")
response= get_openai_response(input)

submit=st.button("Ask the question")

if submit:
    st.subheader("The Respose is:")
    st.write(response)