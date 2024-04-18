import streamlit as st

content = st.text_input("content")

st.html(content)