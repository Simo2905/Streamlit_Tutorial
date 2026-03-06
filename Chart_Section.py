import streamlit as st 
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

# Title
st.title("Streamlit Chart Section")

# Generate a random DataFrame
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns = ['A', 'B', 'C']
) 

# .rand ==> sempre positivi e compresi tra 0 e 1
# .randn ==> distribuzione Gaussiana con media = 0 e std = 1, possono essere sia negativi che positivi
# .randint ==> interi e si può definire il range (0,10, size(2,3)), 2 righe 3 colonne numeri da 0 a 10


# Area Chart Section
st.subheader("Area Chart Section")
st.area_chart(chart_data)

# Bar Chart Section
st.subheader("Bar Chart Section")
st.bar_chart(chart_data)

# Line Chart Section
st.subheader("Line Chart Section")
st.line_chart(chart_data)

# Scatter Chart Section
st.subheader("Scatter Chart Section")
st.scatter_chart(chart_data)

# Map Section 
st.subheader("Map Section")
map_data = pd.DataFrame(
    np.random.randn(100,2)/[50,50] + [43.71, 13.22], # Coordinate of SF
    columns = ['lat', 'lon']
)
st.map(map_data)