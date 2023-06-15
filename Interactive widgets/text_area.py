import streamlit as st
import numpy as np
import time

# st.text_area(label = 'Label 출력 필드입니다',
#              placeholder = '입력 형식 예시입니다',
#              help = '사용자에게 간단한 설명을 제공할 수 있습니다',
#              max_chars = 30)

st.header('Text Area')

st.subheader('label')
st.text_area(label = '간단한 인사말')

st.subheader('label_visiblilty')
st.text_area(label = '간단한 인사말',
             label_visibility = 'hidden', key = 0)
st.text_area(label = '간단한 인사말',
             label_visibility = 'collapsed', key = 1)


st.subheader('value')
st.text_area(label = '간단한 인사말',
             value = '안녕하세요. 멋쟁이사자처럼 데모페이지 입니다.', key = 2)


st.subheader('height')
st.text_area(label = '간단한 인사말', key = 8)
st.text_area(label = '간단한 인사말', height = 200, key = 3)


st.subheader('placeholder')
st.text_area(label = '이메일 주소를 입력해주세요.',
			 placeholder = 'likelion@likelion.org', key = 4)


st.subheader('help')
st.text_area(label = '간단한 인사말', help="간단한 자기소개도 포함해주시면 좋습니다", key = 5)


st.subheader('max_chars')
st.text_area('간단한 인사말', max_chars = 30, key = 6)


st.subheader('disabled')
st.text_area('disabled: True', '', disabled = True, key = 7)