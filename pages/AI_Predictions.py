import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from utils.data_loader import load_data
from utils.preprocessing import (
    prepare_ml_data,
    get_feature_columns,
    get_target_column
)

st.title("🤖 AI Maintenance Prediction")

# Load Data
df = load_data()

# Check if dataset is empty
if df.empty:
    st.error("Dataset is empty. Please check Medical_Device_Failure_dataset.csv")
    st.stop()

# Preprocess
df_encoded, encoders = prepare_ml_data(df)

features = get_feature_columns(df)
target = get_target_column()

# Check columns exist
missing_cols = [col for col in features if col not in df_encoded.columns]

if missing_cols:
    st.error(f"Missing columns: {missing_cols}")
    st.stop()

if target not in df_encoded.columns:
    st.error(f"Target column '{target}' not found")
    st.stop()

# Train Model
X = df_encoded[features]
y = df_encoded[target]

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

st.subheader("Enter Device Information")

age = st.number_input(
    "Device Age (Years)",
    min_value=0,
    max_value=50,
    value=5
)

maintenance_cost = st.number_input(
    "Maintenance Cost",
    min_value=0,
    value=1000
)

downtime = st.number_input(
    "Downtime (Hours)",
    min_value=0,
    value=10
)

maintenance_frequency = st.number_input(
    "Maintenance Frequency",
    min_value=0,
    value=4
)

failure_event_count = st.number_input(
    "Failure Event Count",
    min_value=0,
    value=1
)

if st.button("Predict Maintenance Class"):

    input_data = pd.DataFrame(
        [[
            age,
            maintenance_cost,
            downtime,
            maintenance_frequency,
            failure_event_count
        ]],
        columns=features
    )

    prediction = model.predict(input_data)[0]

    # Decode prediction if encoded
    try:
        prediction_label = encoders[target].inverse_transform(
            [prediction]
        )[0]
    except:
        prediction_label = prediction

    st.success(
        f"Predicted Maintenance Class: {prediction_label}"
    )

    st.balloons()
