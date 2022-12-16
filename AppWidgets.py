import streamlit as st
from PIL import Image
import os

# Button
st.header("Input Widgets")

button = st.button("Button")

if button:
    st.write("You press the Button")


# Checkbox - Toggle Button

st.header("Checkbox")
ch_box = st.checkbox("Do You want to agree?")

if ch_box:
    st.title("You check the box")
else:
    st.write("Please check the box")

# Radio Buttons

opt = ("India", "USA", "UK", "Austrailia", "None")
opt_select = st.radio("What is your fav conditions", opt, index=4)

if opt_select:
    st.write(f"You favorite country is {opt_select}")

# Select Box

options = ("Email", "Phone", "WhatsApp", "Telegram")
select_box = st.selectbox("How would you like to contact us?", options, index=1)

if select_box == "Email":
    st.write("Please input your email")

# Slider

slider = st.slider("What is your age?",
                   min_value=18,
                   max_value=100,
                   step=1,
                   value=20)
st.write(f"Your age is {slider}")

# Text input

name = st.text_input("What is your name")
st.write(name)
age = st.number_input("Enter your age: ",
                      min_value=1,
                      max_value=100,
                      step=1,
                      value=25)
st.write("Your age is: ", age)

# Uploading files:

file_upload = st.file_uploader('Choose a file')

if file_upload is not None:
    st.success("File Uploaded sucessfully")
    details = {'filename': file_upload.name,
               'filetype': file_upload.type,
               'filesize': file_upload.size}

    st.json(details)

    # Targeting file to be save in particular directory

    path = os.path.join("./upload", file_upload.name)

    with open(path, mode="wb") as f:
        f.write(file_upload.getbuffer())
        st.success("File Saved Sucessfully")



