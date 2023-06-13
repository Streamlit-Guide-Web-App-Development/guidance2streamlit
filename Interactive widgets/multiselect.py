import streamlit as st

hobbies = ['음악 듣기', '운동하기', '책 읽기', '그림 그리기', '글쓰기','요리하기']

selected_hobbies = st.multiselect('당신의 취미를 선택해주세요', hobbies)

if selected_hobbies:
    st.write('선택한 취미들:',selected_hobbies)
else:
    st.write('취미를 선택하지 않았습니다.')