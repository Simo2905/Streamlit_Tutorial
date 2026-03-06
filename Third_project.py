import streamlit as st 
from openai import OpenAI 
from dotenv import load_dotenv
import os

load_dotenv()

secret_key = os.getenv("OPENAI_API_KEY2")


if secret_key:
    secret_key = os.getenv("OPENAI_API_KEY2")
    print("Secret key done!")
    print(f"The last 4 characters of secret key are: {secret_key[-4:]}")
else:
    print("Error, key not present")
  

st.title("Chat-GPT-like clone Chat bot")

# Initialize the LLM model and create a session_state
client = OpenAI(api_key = secret_key)

if "openai_model" not in st.session_state:
    st.session_state.openai_model = "gpt-5-mini"

st.write(st.session_state)   

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
# Accept user input
if prompt := st.chat_input("Ask me something..."):
    # Add user input to chat history
    st.session_state.messages.append({"role":"user","content":prompt})
    # Display the user input in messages container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Display the assistant output in message container
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model = st.session_state.openai_model,
            messages = [
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream = True,
            #max_tokens = 50
        )
        response = st.write(stream)
    st.session_state.messages.append({"role": "assistant","content": response})

    

 
    



