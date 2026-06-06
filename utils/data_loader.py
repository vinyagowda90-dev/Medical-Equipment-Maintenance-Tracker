import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    """
    Load Medical Device Failure Dataset
    """

    df = pd.read_csv(
        "data/Medical_Device_Failure_dataset.csv"
    )

    return df


@st.cache_data
def get_basic_stats(df):

    stats = {
        "total_records": len(df),
        "total_failures": df["Failure_Event_Count"].sum(),
        "avg_cost": round(df["Maintenance_Cost"].mean(), 2),
        "avg_downtime": round(df["Downtime"].mean(), 2)
    }

    return stats


@st.cache_data
def get_device_types(df):

    return sorted(
        df["Device_Type"].unique().tolist()
    )


@st.cache_data
def get_countries(df):

    return sorted(
        df["Country"].unique().tolist()
    )


def filter_data(df, device_type=None, country=None):

    filtered_df = df.copy()

    if device_type and device_type != "All":
        filtered_df = filtered_df[
            filtered_df["Device_Type"] == device_type
        ]

    if country and country != "All":
        filtered_df = filtered_df[
            filtered_df["Country"] == country
        ]

    return filtered_df
