import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(path):
    return pd.read_csv(path)

def preprocess_data(df):
    df = df.dropna()
    X = df.drop("yield", axis=1)
    y = df["yield"]
    return X, y

def split_data(X, y):
    return train_test_split(X, y, test_size=0.2, random_state=42)
