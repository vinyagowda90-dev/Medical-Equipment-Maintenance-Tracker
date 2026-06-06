import pandas as pd
from sklearn.preprocessing import LabelEncoder


def preprocess_data(df):
    """
    Clean and preprocess the dataset
    """

    df = df.copy()

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Fill missing values
    for col in df.columns:

        if df[col].dtype == "object":
            df[col].fillna(df[col].mode()[0], inplace=True)

        else:
            df[col].fillna(df[col].median(), inplace=True)

    return df


def encode_categorical_features(df):
    """
    Encode categorical columns
    """

    df = df.copy()

    encoders = {}

    categorical_cols = df.select_dtypes(
        include=["object"]
    ).columns

    for col in categorical_cols:

        encoder = LabelEncoder()

        df[col] = encoder.fit_transform(
            df[col].astype(str)
        )

        encoders[col] = encoder

    return df, encoders


def prepare_ml_data(df):
    """
    Prepare data for Machine Learning
    """

    df = preprocess_data(df)

    encoded_df, encoders = encode_categorical_features(df)

    return encoded_df, encoders


def get_feature_columns(df):
    """
    Select ML features
    """

    features = [
        "Age",
        "Maintenance_Cost",
        "Downtime",
        "Maintenance_Frequency",
        "Failure_Event_Count"
    ]

    return features


def get_target_column():
    """
    Target variable
    """

    return "Maintenance_Class"
