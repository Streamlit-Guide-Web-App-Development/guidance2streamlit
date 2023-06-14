import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(
    page_title = "st.color_picker()"
)

st.title('color_picker()')

# 색상 선택기 기본
st.subheader('색상 선택기에서 색 고르기')
color = st.color_picker('색을 선택해주세요!', value = '#00f900', key='1')
st.write('현재 색은', color, '입니다')

# 텍스트 색상 변경하기
st.subheader('텍스트 색상 변경하기')
color2 = st.color_picker('색을 선택해주세요!', '#FFFFFF', key='2')
st.write('현재 색은', color2, '입니다')
st.markdown(f'<p style="color:{color2}">색이 적용된 텍스트입니다.</p>', 
						unsafe_allow_html=True)

# 그래프 색상 변경하기
st.subheader("그래프 색 변경하기")

color3 = st.color_picker('색을 선택해주세요!', '#FFFFFF', key='3')

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

fig, ax = plt.subplots()
ax.plot(x, y, color = color3)

st.pyplot(fig)

# 배경색 변경하기
st.subheader("배경색 변경하기")
color4 = st.color_picker("색을 선택해주세요!", "#FFFFFF", key="4")
bg_css = f"background-color: {color4};"
st.write(f'<div style="{bg_css}">이 문구의 배경색이 변경됩니다.</div>', 
					unsafe_allow_html=True)