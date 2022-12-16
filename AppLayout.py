import streamlit as st
from PIL import Image

# Making Layouts of the pages

# Two types of Layouts
#
# """
# 1. Wide Layout
# 2. Center Layout: Default
# """

st.set_page_config(page_title="Layouts", layout="wide")
st.title("Streamlit Layouts")

# Making Sidebar

# Sidebar is an object of class st. You can call any method as in class st.
sidebar = st.sidebar
sidebar.write("This is my sidebar")
sidebar.header("Header in Sidebar")

# Columns

col1, col2, col3 = st.columns(3)

with col1:
    cat = Image.open("D:\Projects\Streamlit\media\cat.jpg")
    st.image(cat)
with col2:
    owl = Image.open("D:\Projects\Streamlit\media\owl.jpg")
    st.image(owl)
with col3:
    dog = Image.open("D:\Projects\Streamlit\media\dog.jpg")
    st.image(dog)

# Making tabs in streamlit

st.header("Display the Tabs Section")

tab1, tab2, tab3 = st.tabs(["Cat", "Owl", "Dog"])

with tab1:
    cat = Image.open("D:\Projects\Streamlit\media\cat.jpg")
    st.image(cat)
with tab2:
    owl = Image.open("D:\Projects\Streamlit\media\owl.jpg")
    st.image(owl)
with tab3:
    dog = Image.open("D:\Projects\Streamlit\media\dog.jpg")
    st.image(dog)







