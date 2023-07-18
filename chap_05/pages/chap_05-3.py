import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

st.title('5.3 상호작용을 통한 동적 데이터 시각화')

st.divider()

# st.color_picker 예시
st.markdown("#### *st.color_picker 예시 1*")
color = st.color_picker("색을 선택해주세요!", "#FFFFFF", key=1)
st.write("현재 색은", color, "입니다")
st.markdown(f"<p style='color:{color}'>색이 적용된 텍스트입니다.</p>",
            unsafe_allow_html=True)

st.markdown("#### *st.color_picker 예시 2*")
color = st.color_picker("색을 선택해주세요!", "#FFFFFF", label_visibility="hidden", key=2)
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
fig, ax = plt.subplots()
ax.plot(x, y, color = color)
st.pyplot(fig)

st.markdown("#### *st.color_picker 예시 3*")
color = st.color_picker("색을 선택해주세요!", "#FFFFFF", key=3)
bg_css = f"background-color: {color};"
st.write(f"<div style='{bg_css}'>이 문구의 배경색이 변경됩니다.</div>",
         unsafe_allow_html=True)

st.divider()


# st.camera_input 예시
st.markdown("#### *st.camera_input 예시 1*")
picture = st.camera_input("사진을 찍을 수 있습니다.", key=4)
if picture:
    st.image(picture)

st.markdown("#### *st.camera_input 예시 2*")
file_buffer = st.camera_input("사진을 찍을 수 있습니다.", key=5)
if file_buffer is not None:
    bytes_data = file_buffer.getvalue()
    st.write(type(bytes_data)) # bytes_data의 타입 확인

st.markdown("#### *st.camera_input 예시 3*")
st.header("camera_input()")
st.subheader("PIL, Numpy 라이브러리")

file_buffer = st.camera_input("사진을 찍을 수 있습니다.", key=6)

if file_buffer is not None:
    image_pil = Image.open(file_buffer)

    # To convert PIL Image to numpy array:
    image_array = np.array(image_pil)

    # image_array의 타입 출력
    # <class "numpy.ndarray">
    st.write(type(image_array))

    # image_array의 shape 출력
    # (height, width, channels)
    st.write(image_array.shape)

st.divider()


# st.data_editor 예시
st.markdown("#### *st.data_editor 예시 1*")
df = pd.DataFrame(
    [
       {"명령어": "st.selectbox", "평점": 4, "is_widget": True},
       {"명령어": "st.balloons", "평점": 5, "is_widget": False},
       {"명령어": "st.time_input", "평점": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df, height = 200, num_rows="fixed", key=7)
edited_df = st.data_editor(df, height = None, num_rows="fixed", key=8)

st.markdown("#### *st.data_editor 예시 2*")
edited_df = st.data_editor(df, width = 2000, num_rows="fixed", key=9)
edited_df = st.data_editor(df, width = None, num_rows="fixed", key=10)

st.markdown("#### *st.data_editor 예시 3*")
edited_df = st.data_editor(df, num_rows="fixed", hide_index=True, key=11)
edited_df = st.data_editor(df, num_rows="fixed", hide_index=False, key=12)

st.markdown("#### *st.data_editor 예시 4*")
edited_df = st.data_editor(df, num_rows="fixed", hide_index=False,
                           column_order=("is_widget","명령어","평점"), key=13)
edited_df = st.data_editor(df, num_rows="fixed", hide_index=False,
                           column_order=None, key=14)

st.markdown("#### *st.data_editor 예시 5*")
edited_df = st.data_editor(df, column_config={"command": "Streamlit 명령어",
                                              "rating": st.column_config.NumberColumn(
                                                  "당신이 주는 평점",
                                                  help="이 명령어에 몇점이나 주시겠습니까 (1-5)?",
                                                  min_value=1,
                                                  max_value=5,
                                                  step=1,
                                              ),
                                              "is_widget": "위젯인가 ?",
                                             },
                           disabled=["명령어", "is_widget"],
                           hide_index=True,
                           key=15
                          )
favorite_command = edited_df.loc[edited_df["평점"].idxmax()]["명령어"]
st.markdown(f"최애 명령어는 **{favorite_command}** 🎈")