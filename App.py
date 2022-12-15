import streamlit as st
from PIL import Image
import os
import matplotlib.pyplot as pt

# Learning the below topics
# 1. Streamlit Basics
# 2. Streamlit Layouts
# 3. Streamlit Widgets


# Use for display text, dataframe, graph, images
# st.write("Hello World!")

# text formatting
# st.header("This is Header")
# st.subheader("This is SubHeader")
# st.caption("This is captions")
# st.text("This is simple text")

# Markdown in streamlit

# st.markdown("""
# # This is title
# ## This is header
# ### This is subheader 1
# #### This is subheader 2
# [Marklist](https://www.Google.com)
# """)

# Status Elements
# st.success("This is green color text displayer")
# st.warning("This is yellow color text displayer")
# st.error("This is red color text displayer")

dir = "D:\Projects\Streamlit\media/"
val = 0
filename = os.listdir(dir)


def displayImage(Val, file, dir_name):
    # Displaying media (images and Video)
    path = dir_name + file[Val]
    st.subheader("Displaying Image")
    img = Image.open(path)
    st.image(img, width=300)


# Making a function to use next and previous button for changing images and viewing it.


#     val = val + 1
#     if val == len(filename):
#         val = 0
# elif st.button("Prev"):
#     if val == 0:
#         pass
#     else:
#         val = val - 1

# def move_forward(val, filename):
#     val = val + 1
#     if val == len(filename):
#         val = 0
#     return val
#
# if st.button('Next', on_click=move_forward, args=([val, filename])):
#     displayImage(val, filename, dir)

st.subheader("Displaying Video")
video_file = open("D:\Projects\Streamlit\media\star.mp4", mode='rb').read()
st.video(video_file)
