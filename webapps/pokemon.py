import streamlit as st

st.header('Get a pokemon today')
poketype = st.selectbox('Select pokemon type',
                ['Fire','Water','Electric','Grass'])
btn = st.button('Confirm action')

if btn:
    if poketype == 'Fire':
        st.success("Charmander is yours")
    elif poketype == 'Water':
        st.success("Magikarp is yours")
    elif poketype == 'Electric':
        st.success("Pikachu is yours")
    elif poketype == 'Grass':
        st.success("Bulbasaur is yours")


# write a streamlit app that will 
# calculate the simple interest and compound interest
# and take input from user for pricipal , rateofinterest
# and time period