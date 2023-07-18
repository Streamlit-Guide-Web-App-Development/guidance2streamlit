import streamlit as st
import os
import pandas as pd
from datetime import datetime, time, timedelta

st.title("5.2 선택 위젯 사용하기")

st.divider()

# st.button 예시
st.markdown("#### *st.button 예시 1*")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

st.markdown("#### *st.button 예시 2*")
st.button("Button1",help = "클릭해주세요.")

st.markdown("#### *st.button 예시 3*")
st.button("Button",key=1) # 기본값 
st.button("Button",key=2,use_container_width = True) # 부모의 너비
st.button("Button",key=3,use_container_width = False) # 기본값
st.button("Button",key=4,disabled = True) # 비활성
st.button("Button",key=5,disabled = False) # 활성
st.button("Button",key=6,type = "secondary") # 기본값
st.button("Button",key=7,type = "primary") # 추가 강조

st.markdown("#### *st.button 예시 4*")
import streamlit as st

def handle_on_click():
    st.balloons()
    print("clicked on_click button")

def handle_on_click_args(*args):
    st.snow()
    print(f"clicked on_click args button with args={args}")

def handle_on_click_kwargs(**kwargs):
    st.snow()
    print(f"clicked on_click kwargs button with kwargs={kwargs}")

st.button("on_click", on_click=handle_on_click)
st.button("on_click args", on_click=handle_on_click_args, args=("123",))
st.button("on_click kwargs", on_click=handle_on_click_kwargs, kwargs={"one":1})

st.divider()


# st.file_uploader 예시
st.markdown("#### *st.file_uploader 예시 1*")
uploaded_files = st.file_uploader("파일을 선택해주세요", accept_multiple_files=True, type=["png","jpg","jpeg"])
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write(bytes_data)

st.markdown("#### *st.file_uploader 예시 2*")
uploaded_files = st.file_uploader("CSV파일을 선택해주세요", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write(bytes_data)

st.markdown("#### *st.file_uploader 예시 3*")
uploaded_file = st.file_uploader("파일을 선택해주세요", key=8)
if uploaded_file is not None:
    
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

st.divider()


# st.download_button 예시
st.markdown("#### *st.download_button 예시 1*")
st.download_button("파일 다운로드1", data="file1 1 a")

st.markdown("#### *st.download_button 예시 2*")
st.download_button("파일 다운로드2", data="file2 2 b", file_name="file2.csv")

st.markdown("#### *st.download_button 예시 3*")
st.download_button("파일 다운로드3", "file3 3 c", mime="text/csv")
st.download_button("파일 다운로드4", data="file4 4 d", file_name="file4.csv", mime="text/csv")

st.markdown("#### *st.download_button 예시 4*")
rawData = {
    "연차":[1, 2, 3, 4, 5, 6],
    "연도":[2015, 2016, 2017, 2018, 2019, 2020],
    "매출":[1000000, 2000000, 3000000, 4000000, 8000000, 16000000],
    "순익":[100001, 200001, 300001, 400001, 800001, 1600001],
    "직원수":[1, 2, 4, 8, 16, 32]
}

my_large_df = pd.DataFrame(rawData)

st.write("모든 재실행 시 계산을 방지하기 위해 캐시 변환") 
@st.cache_data
def convert_df(df):
    return df.to_csv().encode("utf-8")

csv = convert_df(my_large_df)

st.download_button(
    label="CSV 파일 다운로드",
    data=csv,
    file_name="large_df.csv",
    mime="text/csv",
)

st.markdown("#### *st.download_button 예시 5*")
st.download_button("binary 파일 다운로드", data=b"example content")
st.write("binary mime : \'application/octet-stream\'")

st.markdown("#### *st.download_button 예시 6*")
# github에서 이미지를 불러올 수 있도록 경로 지정
current_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(current_dir, "ali.jpg")
with open(img_path, "rb") as file:
    btn = st.download_button(
            label="이미지 다운로드",
            data=file,
            file_name="ali.jpg",
            mime="image/jpg"
          )

st.divider()


# st.slider 예시
st.markdown("#### *st.slider 예시 1*")
age = st.slider(label="나이가 어떻게 되세요?",
                min_value=0,
                max_value=130,
                value=25)
st.write("저는 ", age, "살 입니다.")

st.markdown("#### *st.slider 예시 2*")
values = st.slider(label="소득의 퍼센트를 보통 저축하시나요?",
                   min_value=0.0,
                   max_value=100.0,
                   value=(25.0, 75.0),
                     step=0.5)
st.write("소득 대비 저축 비율(%):", values)

st.markdown("#### *st.slider 예시 3*")
step = timedelta(minutes=15)  # 15분 간격으로 슬라이더 이동

appointment = st.slider(
    label="오늘 점심식사 시간이 몇 시부터 몇 시까지 였나요?",
    value=(time(11, 0), time(13, 0)),
    step=step)
st.write("오늘의 점심식사 시간:", appointment)

st.markdown("#### *st.slider 예시 4*")
step = timedelta(hours=1)  # 1시간 간격으로 슬라이더 이동

start_time = st.slider(
    label="언제 시작하시나요?",
		min_value=datetime(2023, 7, 1, 0, 0),
    max_value=datetime(2023, 7, 31, 23, 59),
    value=datetime(2023, 7, 15, 12, 0),
    format="MM/DD/YY - HH:mm",
    step=step)
st.write("Start time:", start_time)

st.divider()


# st.select_slider 예시
st.markdown("#### *st.select_slider 예시 1*")
color = st.select_slider(label="무지개의 색 중 하나를 골라주세요.",
    options=["red", "orange", "yellow", "green", "blue", "indigo", "violet"])
st.write("제가 가장 좋아하는 무지개색은 ", color,"입니다.")

st.markdown("#### *st.select_slider 예시 2*")
start_color, end_color = st.select_slider(label="무지개 색의 범위를 선택해주세요.",
                                          options=["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
                                          value=("yellow", "blue"))
st.write("당신이 선택한 무지개 색의 범위는", start_color, "그리고", end_color, "입니다.")


# st.radio 예시
st.markdown("#### *st.radio 예시 1*")
treasure = st.radio(label="우리나라 국보 1호는?",
                    options=["경복궁", "숭례문", "보신각종"])

if treasure == "숭례문":
    st.write("정답입니다!")
else:
    st.write("틀렸습니다. 다시 한번 풀어보세요.")

st.markdown("#### *st.radio 예시 2*")
# 위젯의 초기값을 세션 상태에 저장해주세요.
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible" # 활성화
    st.session_state.disabled = False       # 비활성화  
    st.session_state.horizontal = False     # 비활성화

col1, col2 = st.columns(2)

with col1:
    st.checkbox("라디오 위젯 비활성화", key="disabled")
    st.checkbox("라디오 옵션 수평 정렬", key="horizontal")

with col2:
    st.radio("라벨을 설정해보세요 👇",
        ["visible", "hidden", "collapsed"],
        key="visibility",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        horizontal=st.session_state.horizontal)

st.divider()


# st.checkbox 예시
st.markdown("#### *st.checkbox 예시 1*")
check = st.checkbox(label="체크박스를 선택하세요!!", value=False)
if check:
    st.write("체크박스가 선택되었습니다!!")
else:
    st.write("체크박스가 선택되지 않았습니다.")

st.markdown("#### *st.checkbox 예시 2*")
password = st.checkbox("비밀번호 변경", disabled=True)
if password:
	st.write("비밀번호가 변경되었습니다!")
else:
	st.write("비밀번호를 변경할 수 없습니다!")

st.divider()


# st.selectbox 예시
st.markdown("#### *st.selectbox 예시 1*")
sports = ["야구","축구","농구","배드민턴"]
selected_sports = st.selectbox("좋아하는 운동을 선택하세요", sports)
if selected_sports:
    st.write(f"좋아하는 운동 : {selected_sports}")

st.markdown("#### *st.selectbox 예시 2*")
option_1 = st.selectbox("당신은 무슨 색을 좋아하시나요?",["빨강","파랑","노랑","검정"],
                        label_visibility = "visible")
st.write(f"당신이 좋아하는 색은 {option_1}입니다!")

option_2 = st.selectbox("당신은 무슨 과일을 좋아하시나요?",["사과","바나나","딸기","메론"],
                        label_visibility = "hidden")
st.write(f"당신이 좋아하는 과일은 {option_2}입니다!")

option_3 = st.selectbox("당신이 좋아하는 동물은 무엇입니까",["고양이","개","곰","사자"],
                        label_visibility = "collapsed")
st.write(f"당신이 좋아하는 동물은 {option_3}입니다!")

st.divider()


# st.multiselect 예시
st.markdown("#### *st.multiselect 예시 1*")
hobbies = ["음악 듣기", "운동하기", "책 읽기", "그림 그리기", "글쓰기","요리하기"]
selected_hobbies = st.multiselect("당신의 취미를 선택해주세요", hobbies)
if selected_hobbies:
    st.write("선택한 취미들:",selected_hobbies)
else:
    st.write("취미를 선택하지 않았습니다.")

st.markdown("#### *st.multiselect 예시 2*")
destination = ["서초구","강남구","송파구","종로구","용산구","마포구","동작구","노원구"]
def format_option(option):
	return f"서울시 {option}"
selected_options = st.multiselect("서울에서 가보고 싶은 곳", destination,
																 format_func=format_option,
																 max_selections=5)
st.write(f"내가 가보고 싶은 서울 지역들 : {selected_options}")