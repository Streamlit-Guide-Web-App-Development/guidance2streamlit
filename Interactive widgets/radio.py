import streamlit as st

treasure = st.radio(
    "우리나라 국보 1호는?",
    ('경복궁', '숭례문', '보신각종'))

if treasure == '숭례문':
    st.write('정답입니다!')
else:
    st.write('틀렸습니다. 다시 한번 풀어보세요.')