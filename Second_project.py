import streamlit as st 
import time
import random 

st.title("Simple chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            'Hello! how are you?',
            'Hi human, how can I help you?',
            'Do you need help?'
        ]
    ) 
    for word in response.split():
        yield word + " "
        time.sleep(0.05)
 
         
# Accept user input
if prompt := st.chat_input("What's up?"):
    # Add input to chat history
    st.session_state.messages.append({"role":"user","content":prompt})
    # Diplay the user message in the chat
    with st.chat_message("user"):
        st.markdown(prompt)
    
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    # Add response to chat history
    st.session_state.messages.append({"role":"assistant","content":response})
    
    