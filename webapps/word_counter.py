import streamlit as st
import pandas as pd
import plotly.express as px

from string import punctuation

st.title("WORD counter")
user_inp = st.text_area("Put some text here",height=200)
btn = st.button('show graph')
choice = st.sidebar.checkbox('view data table')

if btn:
    clean_inp = ''
    for i in user_inp.lower():
        if i not in punctuation:
            clean_inp += i
        
    # count words
    words = clean_inp.split()
    count_data = {}
    for word in words:
        if word in count_data:
            count_data[word] += 1
        else:
            count_data[word] = 1
    # convert it into meaning table
    result = pd.DataFrame([count_data]).T
    result.columns=['count']
    result.sort_index(inplace=True)
    fig = px.bar(result,x=result.index, y='count')
    st.plotly_chart(fig)
    
    if choice:
        st.write(result)
