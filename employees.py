import streamlit as st
import datetime
import pandas as pd

DATA_URL = 'Employees.csv'

@st.cache_data
def load_data(nrows):
    
    data = pd.DataFrame()

    if(nrows == -1):
        data = pd.read_csv(DATA_URL)
    else:
        data = pd.read_csv(DATA_URL, nrows=nrows)

    return data


st.title('R05 Employee Attrition')
st.header(':gray[_Dataframe:bar_chart:_]')
st.header('A header with _italics_ :blue[colors] and emojis :sunglasses:')
st.dataframe(load_data(3000))

##################################################################
# Filters for sidebar
##################################################################
sidebar = st.sidebar
sidebar.title('Filters')

agree = sidebar.checkbox('Show datasource : ')

if agree:
    st.dataframe(load_data(-1))