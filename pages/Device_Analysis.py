import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

df = load_data()

st.title("🔬 Device Analysis")

fig = px.histogram(
    df,
    x="Device_Type",
    color="Device_Type"
)

st.plotly_chart(fig,use_container_width=True)

fig2 = px.box(
    df,
    x="Device_Type",
    y="Age"
)

st.plotly_chart(fig2,use_container_width=True)
