import streamlit as st 
from langchain_openai.chat_models import ChatOpenAI

st.title("Simple Chat bot with Langchain, OpenAI and Streamlit")

openai_api_key = st.sidebar.text_input("OpenAI API Key: ", type = "password")

def generate_response(input_text):
    model = ChatOpenAI(model = "gpt-5-mini", temperature = 0.7, api_key = openai_api_key)
    st.info(model.invoke(input_text).content)
    
with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "What are the most relevant advices for learning Machine Learning?"
    )
    submitted = st.form_submit_button("Submit!")
    if not openai_api_key.startswith("sk-"):
        st.warning("Please enter your OpenAI API key", icon = ":material/block:")
    if submitted and openai_api_key.startswith("sk-"):
        generate_response(text)
        
