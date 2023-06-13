import streamlit as st
import datetime

st.title('Date input 사용법')

st.header('label')
st.date_input("태어난 연도, 월,일을 선택해주세요")

d = st.date_input("생일을 선택해주세요")
st.write('당신의 생일은 :', d)

st.header('value')
st.date_input("태어난 연도, 월,일을 선택해주세요",datetime.date(2023, 1, 1))
st.date_input("여행 시작/종료일을 선택해주세요",[datetime.date(2023, 1, 1),datetime.date(2023, 1, 7)])
st.date_input("여행 시작/종료일을 선택해주세요",(datetime.date(2023, 1, 1),))

st.header('min_value')
st.date_input("여행 시작/종료일을 선택해주세요", min_value=(datetime.date(2023, 1, 1)))

st.header('max_value')
st.date_input("여행 시작/종료일을 선택해주세요", max_value=(datetime.date(2023, 12, 31)))

st.header('label_visibility')
st.date_input("여행 시작/종료일을 선택해주세요", key=1, label_visibility='visible')
st.date_input("여행 시작/종료일을 선택해주세요", key=2, label_visibility='hidden')
st.date_input("여행 시작/종료일을 선택해주세요", key=3, label_visibility='collapsed')
