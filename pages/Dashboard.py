import streamlit as st
from utils.data_loader import load_data

df = load_data()

st.title("📊 Dashboard")

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Total Devices",
    len(df)
)

col2.metric(
    "Avg Maintenance Cost",
    f"${df['Maintenance_Cost'].mean():,.0f}"
)

col3.metric(
    "Avg Downtime",
    f"{df['Downtime'].mean():.1f} hrs"
)

col4.metric(
    "Total Failures",
    int(df['Failure_Event_Count'].sum())
)

st.dataframe(df.head())
