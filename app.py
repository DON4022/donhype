import streamlit as st

st.set_page_config(layout="wide")

# This opens your HTML file and reads it
with open("site.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# This displays it on the screen
st.markdown(html_content, unsafe_allow_html=True)
