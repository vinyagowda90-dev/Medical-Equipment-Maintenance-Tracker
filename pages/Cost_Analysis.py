import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

df = load_data()

st.title("💰 Maintenance Cost Analysis")

fig = px.bar(
    df.groupby("Device_Type")["Maintenance_Cost"]
      .mean()
      .reset_index(),
    x="Device_Type",
    y="Maintenance_Cost",
    color="Maintenance_Cost"
)

st.plotly_chart(fig,use_container_width=True)

fig2 = px.scatter(
    df,
    x="Age",
    y="Maintenance_Cost",
    color="Device_Type",
    size="Failure_Event_Count"
)

st.plotly_chart(fig2,use_container_width=True)
