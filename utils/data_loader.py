import pandas as pd

def load_data():
    df = pd.read_csv(
        "data/Medical_Device_Failure_dataset.csv"
    )

    return df
