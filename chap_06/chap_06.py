#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import streamlit as st
import pandas as pd 
import numpy as np
from PIL import Image
import time 

current_dir = os.path.dirname(os.path.abspath(__file__))

st.title('6. 레이아웃')

st.divider()
# st.sidebar 예시 
st.markdown('#### *st.sidebar 예시*')

add_selectbox = st.sidebar.selectbox("어떤 차트를 조회할까요?",
                                     ("막대", "꺾은선", "히스토그램", "히트맵"))

with st.sidebar:
    st.checkbox("제목")
    st.checkbox("축제목")
    st.checkbox("눈금선")        
    st.checkbox("범례")

with st.sidebar:
    with st.echo():
        st.write("코드 블록 입니다.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("끝!")

st.write('st.sidebar의 예시는 좌측 사이드에 있습니다.')
st.divider()

# st.columns 예시 1
st.markdown('#### *st.columns 예시 1*')

col1, col2 = st.columns([3,1])

# 컬럼 영역 구분을 위한 css 코드 추가 (파란 가로선)
st.markdown(
    """
    <style>
    .custom-column {
        background-color: lightblue;
        padding: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

labels = ['남성', '여성']
values = [20, 30]

col1.subheader("column 1")
col1.markdown('<div class="custom-column">', unsafe_allow_html=True)
col1.bar_chart(values)

data = {'Label': labels, 'Value': values}
df = pd.DataFrame(data)

col2.subheader("column 2")
col2.markdown('<div class="custom-column">', unsafe_allow_html=True)
col2.table(df)

# st.columns 예시 2
st.markdown('#### *st.columns 예시 2*')

col1, col2 = st.columns(2, gap="large")

# 컬럼 영역 구분을 위한 css 코드 추가 (파란 가로선)
st.markdown(
    """
    <style>
    .custom-column {
        background-color: lightblue;
        padding: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with col1:
    st.subheader("column 1")
    img_path = os.path.join(current_dir, "data/image.png")
    image = Image.open("img_path")
    st.markdown('<div class="custom-column">', unsafe_allow_html=True)
    st.image(image, caption="profile", width=200)
  
with col2:
    st.subheader("column 2")
    st.markdown('<div class="custom-column">', unsafe_allow_html=True)
    st.header("Jane")
    st.write("Hobby : Soccer")
    st.write("Nice to meet you.")

st.divider()

# st.tabs 예시 1
st.markdown('#### *st.tabs 예시 1*')

tab1, tab2 = st.tabs(["탭 이름 1", "탭 이름 2"])

tab1.write("이것은 첫 번째 탭입니다.") 

tab2.write("이것은 두 번째 탭입니다.")



# st.tabs 예시 2
st.markdown('#### *st.tabs 예시 2*')

tab1, tab2 = st.tabs(["선그래프 탭", "데이터 탭"])
data = np.random.randn(10, 3)

with tab1:
    st.subheader("📈선그래프")
    st.line_chart(data)

with tab2:
    st.subheader("🗃데이터")
    st.dataframe(data)

st.divider()

# st.expender 예시 
st.markdown('#### *st.expender 예시*')

colors = ['빨강', '주황', '노랑', '초록', '파랑','보라']

with st.expander("화살표를 눌러 펼쳐보세요."):
    selected_hobbies = st.multiselect('그래프 선 색상을 선택해주세요', colors)
    
st.divider()

# st.container 예시 1
st.markdown('#### *st.container 예시 1*')


with st.container():
    st.write("이것은 컨테이너 내부입니다")
    st.bar_chart(np.random.randn(50, 3))

st.write("이것은 컨테이너 외부입니다")


# st.container 예시 2
st.markdown('#### *st.container 예시 2*')

container = st.container()
container.write("이것은 컨테이너 내부입니다")
st.write("이것은 컨테이너 외부입니다")

# 컨테이너에 추가적인 컨텐츠 삽입
container.write("이것도 컨테이너 내부입니다")

# st.container 예시 3
st.markdown('#### *st.container 예시 3*')

# 컨테이너 생성
container = st.container()

# 컨테이너 내부에 다른 컴포넌트들 추가
with container:
    st.header('컨테이너 내부')
    st.subheader('이곳에 다양한 컴포넌트를 추가할 수 있습니다.')
    st.text('여기에는 텍스트, 이미지, 그래프 등 다양한 컴포넌트를 추가할 수 있습니다.')
    st.button('버튼')

# 컨테이너 외부에 다른 컴포넌트들 추가
st.title('컨테이너 외부')
st.subheader('이곳에는 컨테이너 외부의 컴포넌트들이 위치합니다.')
st.text('컨테이너 외부에는 컨테이너 내부의 컴포넌트들과 독립적인 컴포넌트들을 추가할 수 있습니다.')

st.divider()


# st.empty 예시 
st.markdown('#### *st.empty 예시*')
st.title("st.empty 예시")
# 빈 컨테이너를 생성합니다.
container = st.empty()

# 컨테이너에 텍스트를 출력합니다.
container.text("Hello, Streamlit!")

# 3초 후에 컨테이너의 내용을 변경합니다.
time.sleep(3)
container.text("Streamlit is awesome🔥")

# 3초 후에 컨테이너의 내용을 clear합니다.
time.sleep(3)
container.empty()


    

