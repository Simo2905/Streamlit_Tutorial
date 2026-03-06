import streamlit as st

# Inizializzazione variabili di stato
if "name" not in st.session_state:
    st.session_state.name = ""

if "counter" not in st.session_state:
    st.session_state.counter = 0

# Funzione callback
def increment_counter():
    st.session_state.counter += 1

# Widget collegato a session_state.name
st.text_input(
    "Inserisci il tuo nome",
    key="name",
    on_change=increment_counter
)

# Output
st.write("Nome attuale:", st.session_state.name)
st.write("Numero modifiche:", st.session_state.counter)