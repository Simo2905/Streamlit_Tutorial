import streamlit as st
import os

# STREAMLIT RUN nomeFile.py per runnare il programma

# This command is used to add anything to the web
st.write("Hello World!") # Stampa direttamente in local host in rete LAN
st.write({"key":"value"})
st.write(True)

# STREAMLIT DATAFLOW

firstButton = st.button("firstButton")
print(f"firstButton: {firstButton}")

secondButton = st.button("secondButton")
print(f"secondButton: {secondButton}")

# Nel terminale comparirà un False finchè il "button" non verrà premuto, a quel punto comparirà un True
# IMPORTANTE! Ogni volta che si preme un button Streamlit rerun la pagina e resetta ad esempio lo stato dell'altro button a False


# TEXT ELEMENTS

st.title("Simple Title")
st.header("SImple header")
st.subheader("Simple subheader")
st.markdown("Different type of markdown like **this** or _this_")
st.caption("Simple caption small")
code_example = """
def name_function(name):
    print("Goodmorning", name)
    """
st.code(code_example, language = "python")
st.divider() # Straigh line to divide the page


st.image(os.path.join(os.getcwd(),"images", "BG.jpg"))
# getcwd ==> get current working directory 

