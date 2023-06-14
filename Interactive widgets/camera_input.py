import streamlit as st
import cv2
import numpy as np
from PIL import Image
import tensorflow as tf
import torch
import torchvision

st.title('camera_input()')

st.subheader('웹 카메라 이미지 캡쳐하기')
picture = st.camera_input("사진을 찍을 수 있습니다.", key = '1')

if picture:
    st.image(picture)

st.subheader('이미지 파일 버퍼 처리하기')
file_buffer = st.camera_input("사진을 찍을 수 있습니다.", key = '2')

if file_buffer is not None:
    bytes_data = file_buffer.getvalue() # 이미지 파일 버퍼를 바이트로 읽음
    st.write(type(bytes_data)) # 타입 확인