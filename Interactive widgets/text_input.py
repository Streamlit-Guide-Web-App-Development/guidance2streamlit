import streamlit as st


st.header('Text Input')

name = st.text_input(label = '당신의 이름은 무엇입니까?')
st.write(name, '입니다')


st.subheader('label')
st.text_input(
    label = "**굵은 텍스트**, _기울인 텍스트_, ~~취소선~~, 인라인 코드: $x + y$ ,🙌 이모지 :+1: ,[링크](https://example.com)")


st.subheader('label_visiblilty')
name = st.text_input(label = '당신의 이름은 무엇입니까?', label_visibility = 'visible', key = '1')
st.write(name, '입니다')
name = st.text_input(label = '당신의 이름은 무엇입니까?', label_visibility = 'hidden', key = '2')
st.write(name, '입니다')
name = st.text_input(label = '당신의 이름은 무엇입니까?', label_visibility = 'collapsed', key = '3')
st.write(name, '입니다')


st.subheader('value')
name = st.text_input(label = '당신의 이름은 무엇입니까?', value = '멋쟁이사자처럼', key = '4')
st.write(name, '입니다')


st.subheader('key')
def update_test_2():
    st.session_state.test2 = st.session_state.test1

def update_test_1():
    st.session_state.test1 = st.session_state.test2

st.text_input(label = 'key_예시_1', key = 'test1', on_change = update_test_2)
st.text_input(label = 'key_예시_2', key = 'test2', on_change = update_test_1)


st.subheader('on_change')
def update_var():
    st.session_state.key_test1 = st.session_state.key_test2

def update_key():
    st.session_state.key_test2 = var_test

st.text_input(label = 'on_change_key', on_change = update_var, key = 'key_test2')
var_test = st.text_input(label = 'on_change_var', on_change = update_key, key = 'key_test1')




st.subheader('placeholder')
email = st.text_input('이메일 주소를 입력해주세요.',
					   placeholder = 'likelion@likelion.org')
st.write('입력하신 이메일 주소는', email)


st.subheader('help')
st.text_input('당신의 이름은 무엇입니까?', help="성을 포함한 이름 전체를 입력해주세요")


st.subheader('max_chars')
name = st.text_input('당신의 이름은 무엇입니까?', max_chars = 30, key = '5')
st.write(name, '입니다')


st.subheader('type')
password = st.text_input('비밀번호를 입력하세요', '', type = 'password')
st.write('필드에 입력된 값은 ', password, '입니다')


st.subheader('diabled')
name = st.text_input('당신의 이름은 무엇입니까?', '', disabled = True, key = '6')
st.write(name, '입니다')


# def test(value, *args):
    

# st.text_input(label = 'on_change'
#              ,value = '3'
#              ,on_change = test
#              ,args = (3, ))