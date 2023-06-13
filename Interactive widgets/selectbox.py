import streamlit as st

sports = ['야구','축구','농구','배드민턴']

selected_sports = st.selectbox('좋아하는 운동을 선택하세요', sports)

if selected_sports:
    st.write(f'좋아하는 운동 : {selected_sports}')