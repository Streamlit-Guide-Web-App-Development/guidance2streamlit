
from datetime import datetime
from tqdm import tqdm
import streamlit as st
import time
import pandas as pd


st.title("Streamlit Deploy Test")

st.markdown(
"""
Hello Likelions,

This is a demo of Streamlit deployment.

""")

name = st.text_input("What's your name?", "Lion")

date = st.date_input("Choose a date", datetime.now().date())


st.markdown(f"## Hello {name}!\n## The date is {date.strftime('%Y-%m-%d')}")

st.subheader("A cached dataframe")

@st.cache_data()
def get_data(date):
    for i in tqdm(range(10)):
        time.sleep(0.1)
    return pd.DataFrame(
        {"date": pd.date_range(date, periods=3), "c": [7, 8, 5], "d": [10, 11, 7]}
    ).set_index("date")


df = get_data(date)
st.write(df)
