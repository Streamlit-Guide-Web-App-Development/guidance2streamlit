import streamlit as st

check = st.checkbox("체크박스를 선택하세요!!")

if check:
    st.write("체크박스가 선택되었습니다!!")
else:
    st.write("체크박스가 선택되지 않았습니다.")