import streamlit as st

st.title('Text Area')

st.text_area(label='문의 내용을 입력해주세요', help='영업시간 외 작성된 문의에 대한 답변은 익일 영업시간에 등록될 예정입니다.', key='1')
st.write('')
st.write('')

st.text_area(label='문의 내용을 입력해주세요', height=200, max_chars=1000, key='2')
st.write('')
st.write('')

st.text_area(label='문의 내용을 입력해주세요', height=200, max_chars=1000,
			 disabled=True, placeholder='서비스 점검중입니다.', label_visibility="collapsed", key='3')