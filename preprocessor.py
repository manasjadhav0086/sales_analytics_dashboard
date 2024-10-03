import pandas as pd
import streamlit as st

# Fetching the date and creating time-based features
def fetch_time_feature(df):
    # Convert the Date column to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Extract Year, Month, and Day from the Date
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day
    
    # Create Financial Month mapping
    month_dict = {4: 1, 5: 2, 6: 3, 7: 4, 8: 5, 9: 6, 10: 7, 11: 8, 12: 9, 1: 10, 2: 11, 3: 12}
    df['Financial_Month'] = df['Month'].map(month_dict)
    
    # Create Financial Year based on the Month
    df['Financial_Year'] = df.apply(lambda x: f"{x['Year']} - {x['Year']+1}" if x['Month'] >= 4 else f"{x['Year']-1} - {x['Year']}", axis=1)
    return df

# Multiselect function
def multiselect(title, option_list):
    selected = st.sidebar.multiselect(title, option_list)
    select_all = st.sidebar.checkbox('Select  All',  value=False, key = title)
    if select_all:
        selected_options = option_list
    else:
        selected_options = selected
    return selected_options