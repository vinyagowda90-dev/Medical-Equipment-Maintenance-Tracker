import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("data/Medical_Device_Failure_dataset.csv")

# Encode categorical columns
categorical_cols = df.select_dtypes(include=["object"]).columns

encoders = {}

for col in categorical_cols:
    encoder = LabelEncoder()
    df[col] = encoder.fit_transform(df[col].astype(str))
    encoders[col] = encoder

# Features
features = [
    "Age",
    "Maintenance_Cost",
    "Downtime",
    "Maintenance_Frequency",
    "Failure_Event_Count"
]

X = df[features]

# Target
y = df["Maintenance_Class"]

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# Save model
joblib.dump(
    model,
    "models/random_forest.pkl"
)

print("Model saved successfully!")
