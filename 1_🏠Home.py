import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide"
)

st.markdown("# FIFA 2023 OFFICIAL DATA ⚽")
st.sidebar.markdown("Developed by [Fábio Vilela](https://github.com/FabioCaxa)")

btn = st.button("Get the dataset from Kaggle")

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

st.markdown("""
            The dataset from 2017 to 2023 provides comprehensive information on professional football players. It includes a wide range of attributes such as player demographics, physical characteristics, game statistics, contract details, and club affiliations.

            With **over 17,000 records**, this dataset serves as a valuable resource for football analysts, researchers, and enthusiasts interested in exploring various aspects of the football world. It allows studying player attributes, performance metrics, market evaluation, club analysis, player positioning, and player development over time.
            """)