import streamlit as st
import pandas as pd
import plotly.express as px


@st.cache_resource
def load_data():
    df = pd.read_csv("data/all_stocks_5yr.csv", index_col="date")
    
    numeric_df = df.select_dtypes(['float','int'])
    numeric_cols = numeric_df.columns

    text_df = df.select_dtypes(['object'])
    text_cols = text_df.columns

    return df, numeric_cols, text_cols


df, numeric_cols, text_cols = load_data()


# Title of dashboard
st.title("Stock Market Dashboard")

# Lets show the dataset
st.write(df)