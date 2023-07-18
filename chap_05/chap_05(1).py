import streamlit as st
import datetime

st.title('5.1 사용자 입력 받기: 입력과 출력')

st.divider()
# text_input 예시
st.markdown("#### *st.text_input 예시 1*")
name = st.text_input(label="이름을 입력해주세요 🙌")
st.write(f"입력된 이름은 {name}입니다")

st.markdown("#### *st.text_input 예시 2*")
def dup_check():
    if "email_lst" not in st.session_state:
        st.session_state.email_lst  = ["weniv@example.com"]
    
    if st.session_state.email in st.session_state.email_lst:
        st.session_state.email = ""
        return display_warning()
    else:
        st.session_state.email_lst.append(st.session_state.email)

st.text_input(label="이메일 주소를 입력해주세요",
              placeholder="weniv@example.com",
              max_chars=30,
              key="email",
              on_change=dup_check
              )

def display_warning():
    col.markdown(":red[이미 사용중인 이메일 주소입니다]")
    
col, _ = st.columns(2)
st.markdown(f"입력된 이메일 주소는 {st.session_state.email}입니다")

st.markdown("#### *st.text_input 예시 3*")
pw = st.text_input(label="비밀번호를 입력해주세요",
                   max_chars=16,
                   type="password")
st.caption("영문, 한글, 특수문자 조합 16자 이하로 입력해주세요.")
st.write(f"입력된 비밀번호는 {pw}입니다")


st.divider()
# text_area 예시
st.markdown("#### *st.text_area 예시 1*")
st.text_area(label="문의 내용을 입력해주세요", help="영업시간 외 작성된 문의에 대한 답변은 익일 영업시간에 등록될 예정입니다.", key="1")

st.markdown("#### *st.text_area 예시 2*")
st.text_area(label="문의 내용을 입력해주세요", height=200, max_chars=1000, key="2")

st.markdown("#### *st.text_area 예시 3*")
st.text_area(label="문의 내용을 입력해주세요", height=200, max_chars=1000,
						 disabled=True, placeholder="서비스 점검중입니다.",
						 label_visibility="collapsed", key="3")


st.divider()
# number_input 예시
st.markdown("#### *st.number_input 예시 1*")
st.number_input("나이를 입력해주세요.", min_value=0, value=20, step=1, key="4")

st.markdown("#### *st.number_input 예시 2*")
st.number_input("몸무게를 입력해주세요.", min_value=0.0, step=0.1, format="%.2f", key="5")


st.divider()
# date_input 예시
st.markdown("#### *st.date_input 예시 1*")
birth = st.date_input("생일을 선택해주세요", help="회색 박스를 눌러 날짜를 클릭해주세요.")
st.write("당신의 생일은 :", birth)

st.markdown("#### *st.date_input 예시 2*")
st.date_input("태어난 연도, 월,일을 선택해주세요",datetime.date(2023, 1, 1))

st.markdown("#### *st.date_input 예시 3*")
st.date_input("여행 시작/종료일을 선택해주세요",[], key="6")
st.date_input("여행 시작/종료일을 선택해주세요",(), key="7")
st.date_input("여행 시작/종료일을 선택해주세요",[datetime.date(2023, 1, 1),datetime.date(2023, 1, 7)], key="8")
st.date_input("여행 시작/종료일을 선택해주세요",(datetime.date(2023, 1, 1),), key="9")

st.markdown("#### *st.date_input 예시 4*")
st.date_input("여행 시작/종료일을 선택해주세요", min_value=(datetime.date(2023, 1, 4)), key="10")
st.date_input("여행 시작/종료일을 선택해주세요", value =(datetime.date(2023, 6, 30)), max_value=(datetime.date(2023, 6, 30)), key="11")


st.divider()
# time_input 예시
st.markdown("#### *st.time_input 예시 1*")
st.time_input("알람 시간을 설정해주세요.")

st.markdown("#### *st.time_input 예시 2*")
st.time_input("알람 시간을 설정해주세요.", datetime.time(9, 00), key="12")

st.markdown("#### *st.time_input 예시 3*")
st.time_input("알람 시간을 설정해주세요.", key="13", label_visibility="visible", help="알람 시간을 설정해주세요.")
st.time_input("알람 시간을 설정해주세요.", key="14", label_visibility="hidden")
st.time_input("알람 시간을 설정해주세요.", key="15", label_visibility="collapsed")
st.date_input("알람 시간을 설정해주세요.", key="16", disabled=True)

from tqdm import tqdm
from datetime import datetime
import time
import pandas as pd

date = st.date_input("Choose a date", datetime.now().date())
def get_data(date):
    for i in tqdm(range(10)):
        time.sleep(0.1)
    return pd.DataFrame(
        {"date": pd.date_range(date, periods=3), "c": [7, 8, 5], "d": [10, 11, 7]}
    ).set_index("date")

df = get_data(date)
st.write(df)