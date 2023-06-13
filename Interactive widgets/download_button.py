import streamlit as st
import pandas as pd

st.title('Download Button 사용법')

st.header('label')
st.download_button("파일 다운로드1",'file1 1 a')

st.header('file_name')
st.download_button('파일 다운로드2','file2 2 b','file2.csv')

st.header('mime')
st.download_button('파일 다운로드3','file3 3 c',mime='text/csv')
st.download_button('파일 다운로드4','file4 4 d','file4.csv',mime='text/csv')

st.header('DataFrame을 CSV로 다운로드')
rawData = {
    '연차':[1, 2, 3, 4, 5, 6],
    '연도':[2015, 2016, 2017, 2018, 2019, 2020],
    '매출':[1000000, 2000000, 3000000, 4000000, 8000000, 16000000],
    '순익':[100001, 200001, 300001, 400001, 800001, 1600001],
    '직원수':[1, 2, 4, 8, 16, 32]
}

my_large_df = pd.DataFrame(rawData)

@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')

csv = convert_df(my_large_df)

st.download_button(
    label="CSV 파일 다운로드",
    data=csv,
    file_name='large_df.csv',
    mime='text/csv',
)
st.write('모든 재실행 시 계산을 방지하기 위해 캐시 변환')


st.header('binary 파일 다운로드')
st.download_button('binary 파일 다운로드', b'example content')
st.write('binary mime : \'application/octet-stream\'')

st.header('이미지 다운로드')
with open("ali.jpg", "rb") as file:
    btn = st.download_button(
            label="이미지 다운로드",
            data=file,
            file_name="ali.jpg",
            mime="image/jpg"
          )