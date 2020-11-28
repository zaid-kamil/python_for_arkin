import streamlit as st

st.title("Python Program")

name = st.text_input('Enter you name')
btn = st.button('split the name')
if name and btn: # name is given and btn is clicked
    words = name.split()
    st.write(f'got {len(words)} words in your name')
