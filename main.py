import pandas as pd
import numpy as np
import streamlit as st
import preprocessor

st.set_page_config(layout="wide")

# Reading the data
df = pd.read_csv('data.csv')

#create time feature
df = preprocessor.fetch_time_feature(df)
print(df)

#sidebar
st.sidebar.title('Filters')

#filters
Selected_year = preprocessor.multiselect("select Financial Year", df["Financial_Year"].unique())
Selected_month = preprocessor.multiselect("Select Financial Month", df["Financial_Month"].unique())
Selected_retailer = preprocessor.multiselect("Select Retailer",  df["Retailer"].unique())
Selected_company = preprocessor.multiselect("Select Company", df["Company"].unique())

#lGlobal  filters
filtered_df = df[(df["Financial_Year"].isin(Selected_year)) & (df["Financial_Month"].isin(Selected_month)) & (df["Retailer"].isin(Selected_retailer)) & (df["Company"].isin(Selected_company))]

# Dashboard Title
st.title('Sales Analytics Dashboard')

# Creating columns
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Total Sales", value = int(filtered_df["Amount"].sum()))
with col2:
    st.metric(label="Total Margin", value = int(filtered_df["Margin"].sum()))
with col3:
    st.metric(label="Total Transactions", value = len(filtered_df["Margin"]))
with col4:
    st.metric(label="Total Margin (in %)", value = int(filtered_df["Margin"].sum()*100/filtered_df["Amount"].sum()))