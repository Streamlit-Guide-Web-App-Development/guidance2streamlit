import streamlit as st
import datetime

st.title('Time input 사용법')

st.header('label')
st.time_input('알람 시간을 설정해주세요.',step=0:15:00)

st.header('value')
st.time_input('알람 시간을 설정해주세요.', datetime.time(9, 00))

st.header('label_visibility')
st.time_input("알람 시간을 설정해주세요.", key=1, label_visibility='visible')
st.time_input("알람 시간을 설정해주세요.", key=2, label_visibility='hidden')
st.time_input("알람 시간을 설정해주세요.", key=3, label_visibility='collapsed')

