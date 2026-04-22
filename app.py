# import the modules
import pandas as pd
import streamlit as st
import numpy as np
import calendar
# set up the page
st.set_page_config(page_title="Simple Sales Dashboard",page_icon="🎈")
# title the page
st.title("Simple Sales Dashboard App")
# load the dataset
data = pd.read_csv("sample_data2.csv")
st.write(data)

# sort the month chronologically
month_order = list(calendar.month_abbr)[1:7]
data['Month_name']=pd.Categorical(data['Month_name'],categories=month_order,ordered=True)
data=data.sort_values('Month_name')
st.title('Monthly Data Overview')
st.dataframe(data)

# sidebar filter
region_options = ['All'] + list(data['Region'].unique())
month_options = ['All'] + month_order
region = st.sidebar.selectbox("Select Region",region_options)
month = st.sidebar.selectbox("select Month",month_options)
# filter the data
data_filtered = data.copy()
if region !="All":
    data_filtered = data_filtered[data_filtered['Region']==region]
if month != "All":
    data_filtered = data_filtered[data_filtered['month-name']==month]

# KPIs
total_sales = data_filtered['Sales'].sum()
st.metric(label=f"Total Sales",value=f"${total_sales:,.2f}")

# charts1
st.write('### Sales by Product Category')
chart1_data = data_filtered.groupby('Product_category')['Sales'].sum()
st.bar_chart(chart1_data)

# chart2 line chart
st.write('### Sales Trend Over Time')
chart2_data = data_filtered.groupby('Month_name')['Sales'].sum()

st.line_chart(chart2_data)