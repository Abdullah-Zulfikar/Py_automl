import pandas as pd
import os

def load_dataset(file_path):
    if file_path.endswith("csv"):
        df = pd.read_csv(file_path)
    elif file_path.endswith(".xlsx"):
        df = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupport file type")
    return df


def detect_data_type(df):
    if 'text' in df.columns or df.select_dtypes(include='object').shape[1] > 0:
        avg_length = df.select_dtypes(include='object').astype(str).apply(lambda col: col.str.len().mean()).mean()
        if avg_length > 30:
            return "nlp"
    if 'image' in df.columns or any("jpg" in str(x) for x in df.iloc[0].astype(str)):
        return "image"
    elif 'date' in df.columns or df.select_dtypes(include='datetime').shape[1] > 0:
        return "timeseries"
    else:
        return "tabular"
    