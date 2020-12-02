import streamlit as st
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os

def add_filter(filter):
    img = Image.open(file)
    img = img.filter(filter)
    d = ImageDraw.Draw(img)
    fnt = ImageFont.truetype('gilly.otf',40)
    d.text((20, img.height-60),text="created by : ZBK",fill=(255,0,0),font=fnt)
    st.image(img, use_column_width=True)
    btn = st.button('save image ?')
    if btn:
        img.save(file.name)
        st.success(f'file saved at {os.getcwd()} > {file.name}')

st.title("Image Uploader")

imagetypes = ['png','jpg','JPEG']
file = st.file_uploader(label = 'upload images',type=imagetypes)
if file:
    st.image(file.read(),use_column_width=True)
    options = ['Menu','Show outlines','Show outline dark','Blur',]

    choice = st.sidebar.selectbox('choose an option',options)
    
    if choice =='Show outlines':
        add_filter(ImageFilter.CONTOUR)
    elif choice =='Show outline dark':
        add_filter(ImageFilter.FIND_EDGES)
    elif choice =='Blur':
        add_filter(ImageFilter.BLUR)
    else:
        st.warning("Select an option for image")