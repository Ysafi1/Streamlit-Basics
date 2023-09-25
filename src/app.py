import streamlit as st
import pandas as pd

st.write("""# My interface
         This is my first interface using streamlit.
         """)

sepal_height =st.number_input("Enter sepal height")
sepal_width = st.number_input("Enter sepal width")

petal_height = st.number_input("Enter petal height")
petal_width = st.number_input("Enter petal width")

if st.button("predict"):
    st.text(f"The iris has been classified as : '{''}' .")