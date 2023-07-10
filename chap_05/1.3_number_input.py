import streamlit as st

st.title('Number Input')

st.number_input('나이를 입력해주세요.', min_value=0, value=20, step=1, key='4')
st.write('')
st.write('')

st.number_input('몸무게를 입력해주세요.', min_value=0.0, value=50.00, step=0.1, format='%.2f', key='6')