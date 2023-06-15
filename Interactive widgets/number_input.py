import streamlit as st

st.number_input(label = 'Label 출력 필드입니다'
               ,help = '사용자에게 간단한 설명을 제공할 수 있습니다')

# st.text_area(label = 'Label 출력 필드입니다',
#              placeholder = '입력 형식 예시입니다',
#              help = '사용자에게 간단한 설명을 제공할 수 있습니다',
#              max_chars = 30)

st.header('Number Input')

st.subheader('label')
st.number_input('label')


st.subheader('min_value')
st.number_input('min_value', min_value = 0)


st.subheader('max_value')
st.number_input("max_value", max_value = 10)


st.subheader('value')
st.number_input('value', value = 0)


st.subheader('format')
st.number_input("숫자를 입력해주세요.", format="%.2f")
st.number_input("숫자를 입력해주세요.", value = 0, format="%d")


st.subheader('step')
st.number_input('step', step = 1)


# 백분율로 표시 -> 에러
# value3 = st.number_input("Enter a number", format="{:.2%}")