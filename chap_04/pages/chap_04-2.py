#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import pydeck as pdk

# seed 설정 
np.random.seed(100)

st.title('4.5 Scatterplot')

st.divider()
# st.altair_chart 예시 
st.markdown('#### *st.altair_chart 예시*')
# 데이터프레임 만들기
df_chart = pd.DataFrame(
    np.random.randn(100, 3),
    columns=["x축의 값", "y축의 값", "z값"])

# Altair 차트 객체 만들기
df_altair_chart = alt.Chart(df_chart).mark_circle().encode(
    x="x축의 값", y="y축의 값", size="z값", color="z값", 
    tooltip=["x축의 값", "y축의 값", "z값"])

# Streamlit에서 차트 표시
st.altair_chart(df_altair_chart, use_container_width=True)

# Scatter Plot(Matplotlib 라이브러리 활용) 예시 
st.markdown('#### *Scatter Plot(Matplotlib 라이브러리 활용) 예시*')

# 랜덤한 데이터 만들기
np.random.seed(10)
x = np.random.rand(100)  
y = np.random.rand(100)

x_positive = np.random.rand(100)  
y_positive = 1.5 * x_positive + np.random.rand(100)

x_negative = np.random.rand(100)  
y_negative = -1.5 * x_negative + np.random.rand(100)

plt.figure(figsize = (15,6))

# 상관관계를 갖지 않는 산점도
plt.subplot(1,3,1)
plt.scatter(x, y, color = "orange", alpha = 0.7)
plt.xlabel("X축의 값")
plt.ylabel("Y축의 값")
plt.title("산점도")

# 양의 상관관계를 갖는 산점도
plt.subplot(1,3,2)
plt.scatter(x_positive, y_positive, color = "red", alpha = 0.7)
plt.xlabel("X축의 값")
plt.ylabel("Y축의 값")
plt.title("양의 상관관계를 가지는 산점도")

# 음의 상관관계를 갖는 산점도
plt.subplot(1,3,3)
plt.scatter(x_negative, y_negative, alpha = 0.7)
plt.xlabel("X축의 값")
plt.ylabel("Y축의 값")
plt.title("음의 상관관계를 가지는 산점도")
st.pyplot(plt)

# Scatter Plot(Plotly 라이브러리 활용) 예시 
st.markdown('#### *Scatter Plot(Plotly 라이브러리 활용) 예시*')

# 랜덤 데이터 생성
np.random.seed(2023)
points = 100
x = np.random.normal(0, 1, points)
y = np.random.normal(0, 1, points)
colors = np.random.choice(["그룹 B","그룹 C","그룹 A"], points)
sizes = np.random.uniform(1, 20, points)

data = pd.DataFrame({"x": x, "y": y, "colors": colors, "sizes": sizes})

# 산점도 생성
fig = px.scatter(data, x="x", y="y", color="colors", size="sizes")

# Streamlit에서 차트 표시
st.plotly_chart(fig)

st.divider()

st.title('4.6 Box Plot')

st.divider()
# Box Plot(Matplotlib 라이브러리 활용) 예시 
st.markdown('#### *Box Plot(Matplotlib 라이브러리 활용) 예시*')
data = np.random.randn(100, 9)
df = pd.DataFrame(data, columns=["S", "T", "R", "E", "A", "M", "L", "I", "T"])

fig, ax = plt.subplots(figsize=(4,4))

ax.boxplot(x=data, notch=True, sym="rs", vert=True)
ax.set_xticklabels(df.columns)
ax.set_ylabel("value")
st.pyplot(fig, clear_figure=True, use_container_width=False)

# Boxplot(Seaborn 라이브러리 활용) 예시 
st.markdown('#### *Boxplot(Seaborn 라이브러리 활용) 예시*')
# 데이터 생성
data = np.random.normal(0, 1, size=(100, 6))
df = pd.DataFrame(data, columns=["S", "T", "R", "E", "A", "M"])

# 그래프 생성
fig, ax = plt.subplots()
sns.boxplot(data=df, orient="h", width=0.3, palette ="Set3")

st.pyplot(fig)


# Boxplot (Plotly 라이브러리 활용) 예시 
st.markdown('#### *Boxplot (Plotly 라이브러리 활용) 예시*')
data = np.random.normal(0, 1, size=(100, 9))
df = pd.DataFrame(data, columns=["S", "T", "R", "E", "A", "M", "L", "I", "T"])
df_long = pd.melt(df, var_name="Variable", value_name="Value")

fig = px.box(df_long, x="Variable", y="Value", title="Box Plot")
st.plotly_chart(fig)
st.divider()

st.title('4.7 Heatmap')

st.divider()
# Heatmap (Matplotlib 라이브러리 활용) 예시 
st.markdown('#### *Heatmap (Matplotlib 라이브러리 활용) 예시*')
data = np.random.rand(10, 10)
fig, ax = plt.subplots()
ax.imshow(data, cmap="hot", interpolation="nearest")
st.pyplot(fig)

# Heatmap (Seaborn 라이브러리 활용) 예시 
st.markdown('#### *Heatmap (Seaborn 라이브러리 활용) 예시*')
data = np.random.rand(10, 10)
fig, ax = plt.subplots()
sns.heatmap(data, annot=True, fmt=".2f", cmap="hot", square=True)
st.pyplot(fig)

# Heatmap(Plotly 라이브러리 활용) 예시 
st.markdown('#### *Heatmap(Plotly 라이브러리 활용) 예시*')
data = np.random.rand(10, 10)
fig = go.Figure(data=go.Heatmap(z=data, colorscale="hot"))
st.plotly_chart(fig)
st.divider()

st.title('4.8 Area Chart')

st.divider()
# st.area_chart 예시 1
st.markdown('#### *st.area_chart 예시 1*')
# 데이터 생성 
data = {
    "Year": [2018, 2019, 2020, 2021, 2022, 2023],
    "Seoul": [50, 55, 60, 58, 56, 52],
    "Busan": [45, 50, 52, 50, 48, 46],
    "Jeju": [70, 72, 68, 66, 64, 60]
}

df = pd.DataFrame(data)

# 그래프 생성 
st.area_chart(df.set_index("Year"))

# st.area_chart 예시 2
st.markdown('#### *st.area_chart 예시 2*')
# 데이터 생성 
df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

# 그래프 생성 
st.area_chart(df)

# Area chart(Seaborn 라이브러리 활용) 예시 
st.markdown('#### *Area chart(Seaborn 라이브러리 활용) 예시*')
df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

fig, ax = plt.subplots()

sns.lineplot(data=df)

ax.fill_between(df.index, df["a"], color="blue", alpha=0.3)
ax.fill_between(df.index, df["a"], df["b"], color="green", alpha=0.3)
ax.fill_between(df.index, df["b"], df["c"], color="yellow", alpha=0.3)
ax.fill_between(df.index, df["c"], color="red", alpha=0.3)

st.pyplot(fig)

# Area chart(plotly 라이브러리 활용) 예시 
st.markdown('#### *Area chart(plotly 라이브러리 활용) 예시*')
# 데이터 생성 
df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

# 그래프 생성
fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index, y=df["a"], fill="tozeroy", mode="none"))
fig.add_trace(go.Scatter(x=df.index, y=df["b"], fill="tozeroy", mode="none"))
fig.add_trace(go.Scatter(x=df.index, y=df["c"], fill="tozeroy", mode="none"))

st.plotly_chart(fig)
st.divider()

st.title('4.9 Map')

st.divider()
# st.map 예시 1
st.markdown('#### *st.map 예시 1*')
df = pd.DataFrame(
    np.random.randn(1000, 2) / [20, 20] + [37.57, 126.98],
    columns=["lat", "lon"])

st.map(df, zoom=10, use_container_width=False)

# st.map 예시 2
st.markdown('#### *st.map 예시 2*')
locations = {
  "서울" : [37.566418, 126.977950],#서울시청
  "부산" : [35.180152, 129.074980],#부산시청
  "대구" : [35.871468, 128.601757],#대구시청
  "인천" : [37.456445, 126.705873],#인천시청
  "광주" : [35.160068, 126.851426],#광주광역시청
  "대전" : [36.350664, 127.384819],#대전시청
  "울산" : [35.539772, 129.311486],#울산시청
  "세종" : [36.480838, 127.289181],#세종시청
  "경기" : [37.275221, 127.009382],#경기도청
  "강원" : [37.885300, 127.729835],#강원(강원도청)
  "충북" : [36.635947, 127.491345],#충북도청
  "충남" : [36.658826, 126.672849],#충남도청
  "전북" : [35.820599, 127.108759],#전북도청
  "전남" : [34.816351, 126.462924],#전남도청
  "경북" : [36.574108, 128.509303],#경북도청
  "경남" : [35.238398, 128.692371],#경남도청
  "제주" : [33.3617007, 126.511657]#제주
    }

df_locations = pd.DataFrame(locations).T
df_locations.columns = ["lat", "lon"]

st.map(df_locations, zoom=5.5, use_container_width=True)

# st.pydeck_chart 예시 1
st.markdown('#### *st.pydeck_chart 예시 1 : ScatterplotLayer 타입*')
# 서울시 좌표 중심으로 랜덤 데이터 생성
np.random.seed(100)
df = pd.DataFrame(
    np.random.randn(1000, 2) / [20, 20] + [37.57, 126.98],
    columns=["lat", "lon"])

# ScatterplotLayer로 시각화
layer = pdk.Layer(
    "ScatterplotLayer",
    data=df,
    get_position=["lon", "lat"],
    get_radius=200,
    get_color=[255, 0, 0],
)

# Deck 객체 생성
deck = pdk.Deck(
    map_style="light",
    layers=[layer],
    initial_view_state=pdk.ViewState(
        latitude=37.57,
        longitude=126.98,
        zoom=10,
        pitch=50,
    ),
)

# PyDeck 차트 출력
st.pydeck_chart(deck)

# st.pydeck_chart 예시 2
st.markdown('#### *st.pydeck_chart 예시 2: HexagonLayer 타입*')
# 서울시 좌표 중심으로 랜덤 데이터 생성
np.random.seed(100)
df = pd.DataFrame(
    np.random.randn(1000, 2) / [20, 20] + [37.57, 126.98],
    columns=["lat", "lon"])

# HexagonLayer로 시각화
layer = pdk.Layer(
    "HexagonLayer",
    data=df,
    get_position=["lon", "lat"],
    radius=200,
    elevation_scale=4,
    elevation_range=[100, 1000],
    pickable=False,
    extruded=True,
)

# Deck 객체 생성
deck = pdk.Deck(
    map_style="light",
    layers=[layer],
    initial_view_state=pdk.ViewState(
        latitude=37.57,
        longitude=126.98,
        zoom=10,
        pitch=50,
    ),
)

# PyDeck 차트 출력
st.pydeck_chart(deck)


# st.pydeck_chart 예시 3
st.markdown('#### *st.pydeck_chart 예시 3: HeatmapLayer타입*')
# 서울시 좌표 중심으로 랜덤 데이터 생성
df = pd.DataFrame(
    np.random.randn(1000, 2) / [20, 20] + [37.57, 126.98],
    columns=["lat", "lon"])

# HexagonLayer로 시각화
layer = pdk.Layer(
    "HeatmapLayer",
    data=df,
    get_position=["lon", "lat"],
)

# Deck 객체 생성
deck = pdk.Deck(
    map_style="light",
    layers=[layer],
    initial_view_state=pdk.ViewState(
        latitude=37.57,
        longitude=126.98,
        zoom=10,
        pitch=50,
    ),
)

# PyDeck 차트 출력
st.pydeck_chart(deck)






