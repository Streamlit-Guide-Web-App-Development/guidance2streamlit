import streamlit as st

color = st.select_slider(
    '무지개의 색 중 하나를 골라주세요.',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('제가 가장 좋아하는 무지개색은 ', color,'입니다.')
    
start_color, end_color = st.select_slider(
    '무지개 색의 범위를 선택해주세요.',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value=('red', 'blue'))
st.write('당신이 선택한 무지개 색의 범위는', start_color, '그리고', end_color, '입니다.')