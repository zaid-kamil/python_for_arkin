import streamlit as st
from PIL import Image

st.title("Image Uploader")

imagetypes = ['png','jpg','gif','JPEG']
file = st.file_uploader(label = 'upload images',type=imagetypes)
if file:
    st.image(file.read(),use_column_width=True)