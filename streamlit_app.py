'''import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})

st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))'''

import streamlit as st


st.write("""Find the greatest among the three Numbers""")

#Get Input

st.header('User Input Parameters')

#cnt_children = st.number_input("CNT_CHILDREN",min_value=0,max_value=20,step=1)
#amt_income_total = st.number_input("AMT_INCOME_TOTAL",min_value=0.0,max_value=2000000.0)
#days_birth = st.number_input("DAYS_BIRTH",min_value=-30000,max_value=0,step=1)

num1 = st.number_input("Enter 1st Number",min_value=0.0,max_value=100000000.0)
num2 = st.number_input("Enter 2nd Number",min_value=0.0,max_value=100000000.0)
num3 = st.number_input("Enter 3rd Number",min_value=0.0,max_value=100000000.0)

st.subheader('Finding the greatest among the inputs provided above')

if num1>num2:
    if num1>num3:
        st.write('Greatest Number is:',num1)
    else:
        st.write('Greatest Number is:',num3)
else:
    if num2>num3:
        st.write('Greatest Number is:',num2)
    else:
        st.write('Greatest Number is:',num3)