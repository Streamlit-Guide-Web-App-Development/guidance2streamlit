#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import numpy as np
import pandas as pd

st.title('3.3 데이터 디스플레이')

st.divider()
# st.dataframe 예시 1
st.markdown('#### *st.dataframe 예시 1*')
array = np.random.rand(10,5) # 배열 생성

df = pd.DataFrame(array, columns=["A", "B", "C", "D", "E"]) # 데이터 프레임 생성 

st.dataframe(df) # 데이터 프레임 출력

# st.dataframe 예시 2
st.markdown('#### *st.dataframe 예시 2*')

df_menu = pd.DataFrame({
    "메뉴명": ["아메리카노", "르완다 가토 케자 네추럴", "과테말라 아카테낭고 게이샤 워시드", "밀크티라떼"],
    "가격": [4500, 8000, 9000, 7500]
}) # 데이터 프레임 생성 

st.dataframe(df_menu, width=10, height=180, use_container_width=True) # 데이터프레임 출력


st.divider()
# st.table 예시 1
st.markdown('#### *st.table 예시 1*')

list_menu = ["Smoothie", "Coke", "Latte", "Americano", "Cake"] # 리스트 생성

st.table(list_menu) # 테이블 생성

# st.table 예시 2
st.markdown('#### *st.table 예시 2*')

array1 = np.random.randn(8, 4)
array2 = np.random.randint(1, 10, size=(8, 4)) # 배열 생성

st.table(array1) # 테이블 출력
st.table(array2)

# st.table 예시 3
st.markdown('#### *st.table 예시 3*')

df_cafe = pd.DataFrame({"메뉴명": ["Juice", "Americano", "Latte", "espresso"],
        "가격": [5000, 3000, 4000, 2000],
        "핫/아이스 가능 여부": ["불가능", "가능", "가능", "가능"]}) # 데이터프레임 생성

st.table(df_cafe) # 테이블 출력


st.divider()
# Pandas styler 예시 1: 데이터프레임 활용
st.markdown('#### *Pandas styler 예시 1: 데이터프레임 활용*')

df = pd.DataFrame(np.random.randint(0, 10, size=(5, 5)), columns=list("ABCDE"))

st.dataframe(df.style.highlight_max(axis=0)) 

# Pandas styler 예시 2: 데이터 프레임 활용 
st.markdown('#### *Pandas styler 예시 2: 데이터프레임 활용*')

df = pd.DataFrame(np.random.rand(10,5), columns=["A", "B", "C", "D", "E"])

st.dataframe(df.style.background_gradient())

# Pandas styler 예시 3: 테이블 활용 
st.markdown('#### *Pandas styler 예시 3: 테이블 활용*')

df = pd.DataFrame(np.random.randn(10,4), columns=["A","B","C","D"])

st.table(df.style.bar())


st.divider()
# st.metric 예시 1
st.markdown('#### *st.metric 예시 1*')

col1, col2, col3 = st.columns(3)
col1.metric("온도", "25.4 °C", "1.2 °C")
col2.metric("풍속", "9 mph3", "-8%")
col3.metric("습도", "51%", "4%")

# st.metric 예시 2
st.markdown('#### *st.metric 예시 2*')

col1, col2, col3 = st.columns(3)
col1.metric(label="달러USD", value="1,276.20 원", delta="-12.00원")
col2.metric(label="일본JPY", value="958.63 원", delta="-7.44 원")
col3.metric(label="유럽연합EUR", value="1,335.82 원", delta="11.44 원")





