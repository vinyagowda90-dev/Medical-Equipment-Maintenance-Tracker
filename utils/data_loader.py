import pandas as pd
import streamlit as st

@st.cache_data
def load_data():

    try:
        df = pd.read_csv(
            "data/Medical_Device_Failure_dataset.csv"
        )

        return df

    except Exception as e:
        st.error(f"Dataset Error: {e}")
        st.stop()
