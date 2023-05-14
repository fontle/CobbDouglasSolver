import streamlit as st
import plotly.graph_objects as go 
import pandas as pd 
import numpy as np


# Coefficiant values
alpha = 1
beta = 1

# Power values 
px = 0.5
py = 0.5

x = np.linspace(0, 100, 1000)
y = np.linspace(0, 100, 1000)


z = [[(alpha*x_**px)*(beta*y_**py) for x_ in x] for y_ in y]

fig = go.Figure(go.Surface(x=x,y=y,z=z))
st.plotly_chart(fig)



