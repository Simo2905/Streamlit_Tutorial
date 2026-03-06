import streamlit as st

# Session State is something that we can use to store values within the same user session
st.title("Session State")

if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment Counter"):
    st.session_state.counter += 1
    st.write(f"Counter incremented to {st.session_state.counter}")
    
if st.button("Reset"):
    st.session_state.counter = 0
else:
    st.write(f"Counter did not reset")
    
st.write(f"Counter value: {st.session_state.counter}")

# In questo caso ho messo .counter ma potevo mettere qualsiasi cosa, 'step', 'point' , quello che voglio

