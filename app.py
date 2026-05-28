import streamlit as st
import streamlit.components.v1 as components

# 1. Expand the workspace layout to full-screen width
st.set_page_config(layout="wide")

# 2. Open and read your HTML file code layout
with open("site.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# 3. Force render the HTML inside a structural component iframe wrapper
# Adjust height=1000 if your web page design is very long!
components.html(html_content, height=1200, scrolling=True)
