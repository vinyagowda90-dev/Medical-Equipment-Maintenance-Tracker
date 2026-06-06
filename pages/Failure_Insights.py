import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

df = load_data()

st.title("⚠️ Failure Insights")

fig = px.histogram(
    df,
    x="Failure_Event_Count",
    color="Maintenance_Class"
)

st.plotly_chart(fig,use_container_width=True)

fig2 = px.sunburst(
    df,
    path=[
        "Country",
        "Device_Type",
        "Maintenance_Class"
    ]
)

st.plotly_chart(fig2,use_container_width=True)

st.subheader("Top Risk Devices")

risk = df.sort_values(
    "Failure_Event_Count",
    ascending=False
)

st.dataframe(risk.head(20))
