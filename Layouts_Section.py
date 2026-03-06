import streamlit as st 

# Sidebar layout
st.sidebar.title("This is the sidebar")
st.sidebar.write("You can fill this space with important news")
sidebar_input = st.sidebar.text_input("Enter something in the sidebar")

# Tabs layout
tab1, tab2, tab3 = st.tabs(['Tab1', 'Tab2', 'Tab3'])

with tab1:
    st.write("You are in tab1")
with tab2:
    st.write("You are in tab2")
with tab3:
    st.write("You are in tab3")

# Columns layout
col1, col2 = st.columns(2)
with col1:
    st.header("Column 1")
    st.write("Content in column 1")
with col2:
    st.header("Column 2")
    st.write("Content in column 2")

# Containers layput
with st.container(border = True):
    st.write("Something inside the container")
    st.write("Again...something other inside the same container")
    
# Expander
with st.expander("Expande for more details"):
    st.write("Othe information hide")
    
