import streamlit as st 
import pandas as pd

# Title
st.title("Streamlit using Pandas")

# Dataframe Section 
st.subheader("Dataframe")
df = pd.DataFrame({
    'Name': ['Simone', 'Luca', 'Francesco'],
    'Age': [30, 29, 33],
    'Occupation': ['PhD', 'Data Scientist', 'Engineer']
})

st.dataframe(df)

# Dataframe editable Section
st.subheader("Editable Dataframe")
editable_df = st.data_editor(df)

# Static Table Section
st.subheader("Static Dataframe")
st.table(df)

# Metrics Section
st.subheader("Metrics Section")
st.metric(label="Total Rows", value=len(df))
st.metric(label="Average Age", value=round(df['Age'].mean(),1))

# JSON and Dictionary
st.subheader("JSON and Dict Section")
sample_dict = {
    'Name': 'Simone',
    'Age': 30,
    'Skills': ['Python', 'SQL', 'Langchain']
}
st.json(sample_dict)

st.write("Dictionary View:", sample_dict)