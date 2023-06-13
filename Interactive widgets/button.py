import streamlit as st

st.title('Button 사용법')

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

st.header('label')
st.button("Button1")

st.header('key')
st.button("Button2")
# st.button("Button2") # error
st.button("Button2",key = "btn2")

st.header('help')
st.button("Button3",help = "클릭해주세요.")

st.header('on_click, args, kwargs')
def handle_on_click():
    st.balloons()
    print('clicked on_click button')

def handle_on_click_args(*args):
    st.snow()
    print(f'clicked on_click args button with args={args}')

def handle_on_click_kwargs(**kwargs):
    st.snow()
    print(f'clicked on_click kwargs button with kwargs={kwargs}')

st.button('on_click', on_click=handle_on_click)
st.button('on_click args', on_click=handle_on_click_args, args=('123',))
st.button('on_click kwargs', on_click=handle_on_click_kwargs, kwargs={"one":1})

st.header('type')
st.button("Button4")
st.button("Button5",type = "secondary")
st.button("Button6",type = "primary")

st.header('disabled')
st.button("Button7")
st.button("Button8",disabled = True)
st.button("Button9",disabled = False)

st.header('use_container_width')
st.button("Button10")
st.button("Button11",use_container_width = True)
st.button("Button12",use_container_width = False)





