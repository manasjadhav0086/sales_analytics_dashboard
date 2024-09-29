import pandas as pd
import numpy as np
import streamlit as st
import preprocessor

# Reading the data
df = pd.read_csv('data.csv')

#create time feature
df = preprocessor.fetch_time_feature(df)
print(df)

#sidebar
st.sidebar.title('Filters')

#filters
st.sidebar.multiselect("select Financial Year", df["Financial_Year"].unique())
st.sidebar.multiselect("Select Financial month", df["Financial_Month"].unique())
st.sidebar.multiselect("Select Retailer",  df["Retailer"].unique())
st.sidebar.multiselect("Select Company", df["Company"].unique())
