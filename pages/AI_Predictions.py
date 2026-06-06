import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from utils.data_loader import load_data

df = load_data()

st.title("🤖 Predict Maintenance Class")

features = [
    "Age",
    "Maintenance_Cost",
    "Downtime",
    "Maintenance_Frequency",
    "Failure_Event_Count"
]

X = df[features]
y = df["Maintenance_Class"]

model = RandomForestClassifier()
model.fit(X,y)

age = st.slider("Age",0,20,5)
cost = st.number_input("Cost",100,10000,1000)
down = st.number_input("Downtime",0,500,10)
freq = st.number_input("Frequency",0,50,5)
fail = st.number_input("Failures",0,50,1)

if st.button("Predict"):

    pred = model.predict(
        [[age,cost,down,freq,fail]]
    )[0]

    st.success(
        f"Predicted Maintenance Class: {pred}"
    )
