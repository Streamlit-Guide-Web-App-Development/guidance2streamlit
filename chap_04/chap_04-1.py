#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import streamlit as st
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import seaborn as sns

st.title('4.1 Line Chart')

st.divider()

# st.line_chart 예시 
st.markdown('#### *st.line_chart 예시*')

chart_data = pd.DataFrame(
    np.random.randn(10, 2),
    columns=["s", "t"])

st.line_chart(
    chart_data,
    width=0,  
    height=300, 
    use_container_width=True, 
)

# Line Chart(Matplotlib 라이브러리 활용) 예시 
st.markdown('#### *Line Chart(Matplotlib 라이브러리 활용) 예시*')
# 랜덤데이터
x = range(10)
y = [random.randint(1, 10) for _ in x]
# 라인차트
fig, ax = plt.subplots()
ax.plot(x,y, color="navy", linewidth=2, linestyle="-", marker="o")
# 그래프
st.pyplot(fig)

# Line Chart(Seaborn 라이브러리 활용)예시 
st.markdown('#### *Line Chart(Seaborn 라이브러리 활용) 예시*')
data = {
    "Year": [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    "Sales": [100, 150, 200, 180, 150, 130, 200, 250, 270],
    "Revenue": [50, 80, 120, 90, 100, 80, 150, 200, 220]
}
df = pd.DataFrame(data)
fig = plt.figure(figsize=(10, 6))
sns.set_palette("Set2")
# 다중 라인 그래프 그리기
sns.lineplot(x="Year", y="Sales", data=df, marker="o", label="Sales")
sns.lineplot(x="Year", y="Revenue", data=df, marker="o", label="Revenue")
plt.title("Sales and Revenue Trend")
plt.xlabel("Year")
plt.ylabel("Amount")
plt.legend()
st.pyplot(fig)

st.divider()

st.title('4.2 Bar Chart')

st.divider()
# st.bar_chart 예시 
st.markdown('#### *st.bar_chart 예시*')
# 데이터
chart_data = pd.DataFrame(
    np.random.randn(10, 5),
    columns=["a", "b", "c", "d", "e"])
# 막대 차트 출력
st.bar_chart(chart_data,  width=600, height=400, use_container_width=False)

# Bar Chart(Matplotlib 라이브러리 활용)
st.markdown('#### *Bar Chart(Matplotlib 라이브러리 활용) 예시*')
# 데이터셋 생성
x = ['A', 'B', 'C', 'D']
data = [10, 15, 7, 12]
# 막대그래프 생성
fig, ax = plt.subplots()
ax.bar(x, data, width=0.5 , align="center", color="lightblue")
st.pyplot(fig)

# Bar Chart(Bar Chart(Seaborn 라이브러리 활용)활용)
st.markdown('#### *Bar Chart(Seaborn 라이브러리 활용) 예시*')
# 연도별 점수 데이터셋 설정
plt.figure(figsize=(10, 10))
goal = [65, 60, 75, 80, 95]
year = ["2019", "2020", "2021", "2022", "2023"]

# 차트 생성
fig, ax = plt.subplots()
sns.barplot(x=goal, y=year, color="#A8468A")
plt.xlim(55, 100)
st.pyplot(fig)

st.divider()

st.title('4.3 Pie Chart')

st.divider()
# Pie Chart(Matplotlib 라이브러리 활용) 예시 1
st.markdown('#### *Pie Chart(Matplotlib 라이브러리 활용) 예시 1*')
# 랜덤 데이터 생성
labels = ["A", "B", "C", "D"]
sizes = [random.randint(1, 100) for _ in range(len(labels))]

# 그래프 그리기
fig, ax = plt.subplots()
ax.pie(sizes, labels=["A", "B", "C", "D"] ,colors= ["lightsteelblue", "thistle", "bisque", "lightsalmon"], autopct="%1.1f%%",  explode=[0 if s != min(sizes) else 0.1 for s in sizes])
# 그래프 출력
st.pyplot(fig)

# Pie Chart(Matplotlib 라이브러리 활용) 예시 2
st.markdown('#### *Pie Chart(Matplotlib 라이브러리 활용) 예시 2*')
#매개변수 설정
x = [30, 20, 10, 40]
labels = ["A", "B", "C", "D"]
colors = ["lightsteelblue", "thistle", "bisque", "lightsalmon"]
autopct = "%0.0f%%"
#파이차트 생성
fig, ax = plt.subplots()
ax.pie(x, labels=labels, colors=colors, autopct=autopct, radius=1, wedgeprops=dict(width=0.7, edgecolor="w"))
ax.axis("equal")
st.pyplot(fig)
 
# Pie Chart(Plotly 라이브러리 활용) 
st.markdown('#### *Pie Chart(Plotly 라이브러리 활용) 예시*')
# 파이차트
fig = go.Figure(data=go.Pie(
    labels=["A", "B", "C", "D"],                                 
    values=[40,30,20,10],                                        
    marker=dict(colors=px.colors.qualitative.Set3),              
    hole=0.3                                                     
))                                                                             
st.plotly_chart(fig) 

st.divider()

st.title('4.4 Histogram')

st.divider()
# Histogram(Matplotlib 라이브러리 활용) 예시 
st.markdown('#### *Histogram(Matplotlib 라이브러리 활용) 예시*')

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20, color="skyblue", alpha=0.7)
st.pyplot(fig)

# Histogram(Seaborn 라이브러리 활용) 예시 
st.markdown('#### *Histogram(Seaborn 라이브러리 활용) 예시*')

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
fig = plt.figure(figsize=(10,4))
sns.histplot(arr, bins=20, color="pink", kde=True)
st.pyplot(fig)

# Histogram(Plotly 라이브러리 활용) 예시 
st.markdown('#### *Histogram(Plotly 라이브러리 활용) 예시*')

arr = np.random.normal(1, 1, size=100)

fig = go.Figure(data=[go.Histogram(x=arr, nbinsx=10, marker_color="green", opacity=0.5)])
st.plotly_chart(fig)





