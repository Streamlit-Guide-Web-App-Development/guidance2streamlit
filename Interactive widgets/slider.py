import streamlit as st

st.header('Slider')
age = st.slider('나이가 어떻게 되세요?', 0, 130, 25)
st.write('저는 ', age, '살 입니다.')

st.header('Range slider')
values = st.slider(
    '소득의 퍼센트를 보통 저축하시나요?',
    0.0, 100.0, (25.0, 75.0))
st.write('소득 대비 저축 비율(%):', values)

from datetime import time

st.header('Time slider')
appointment = st.slider(
    "오늘 점심식사 시간이 몇 시부터 몇 시까지 였나요?",
    value=(time(11, 30), time(12, 45)))
st.write("오늘의 점심식사 시간:", appointment)

from datetime import datetime

st.header('Datetime slider')
start_time = st.slider(
    "언제 시작하시나요?",
    value=datetime(2023, 8, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)