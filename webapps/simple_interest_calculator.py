import streamlit as st

st.header('Simple Interest Calculator')
principal = st.number_input('Enter the principal amount',
                            value=1000,
                            min_value = 0,
                            max_value=9999999)
rate_of_interest = st.number_input("Rate of interest in %",
                            value=7.9,
                            min_value = 0.1,
                            max_value=100.00)
time = st.number_input('Time duration in years',
                        value=2,
                        min_value = 0,
                        max_value=99)

si = (principal*rate_of_interest*time) / 100
btn = st.button('calculate')
if btn:
    st.success(f'principal = {principal}')
    st.success(f'rate of interest = {rate_of_interest}')
    st.success(f'time period = {time}')
    st.success(f'the simple interest is {si:.2f}')
    amount = si +principal
    st.warning(f'the total amount will be {amount:.2f}')


# streamlit run  