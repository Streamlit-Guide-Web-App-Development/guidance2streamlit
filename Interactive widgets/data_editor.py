import streamlit as st
import pandas as pd

df = pd.DataFrame(
    [
       {"명령어": "st.selectbox", "평점": 4, "is_widget": True},
       {"명령어": "st.balloons", "평점": 5, "is_widget": False},
       {"명령어": "st.time_input", "평점": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df, num_rows="fixed")
favorite_command = edited_df.loc[edited_df["평점"].idxmax()]["명령어"]
st.markdown(f"너의 가장 선호하는 명령어는 **{favorite_command}** 🎈")


edited_df = st.data_editor(df, width = 2000, num_rows="fixed")

edited_df = st.data_editor(df, height = 500, num_rows="fixed")

edited_df = st.data_editor(df, width = 200, use_container_width = True, num_rows="fixed")

edited_df = st.data_editor(df, width = 200, use_container_width = False, num_rows="fixed")

edited_df = st.data_editor(df, num_rows="fixed",hide_index=True)

edited_df = st.data_editor(df, num_rows="fixed",hide_index=False)

edited_df = st.data_editor(df, num_rows="fixed",hide_index=False, column_order=('is_widget','명령어','평점'))

edited_df = st.data_editor(
    df,
    column_config={
        "명령어": "Streamlit 명령어",
        "평점": st.column_config.NumberColumn(
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
)

favorite_command = edited_df.loc[edited_df["평점"].idxmax()]["명령어"]
st.markdown(f"최애 명령어는 **{favorite_command}** 🎈")

df = pd.DataFrame(
    [
       {"명령어": "st.selectbox", "평점": 4, "is_widget": True},
       {"명령어": "st.balloons", "평점": 5, "is_widget": False},
       {"명령어": "st.time_input", "평점": 3, "is_widget": True},
   ]
)

edited_df = st.data_editor(df, num_rows="dynamic")
favorite_command = edited_df.loc[edited_df["평점"].idxmax()]["명령어"]
st.markdown(f"너의 가장 선호하는 명령어는 **{favorite_command}** 🎈")
