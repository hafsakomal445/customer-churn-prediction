import pandas as pd
import numpy as np

def clean_data(df):

    # Remove customer ID
    df = df.drop("customerID", axis=1)

    # Replace blanks with NaN
    df["TotalCharges"] = df["TotalCharges"].replace(" ", np.nan)

    # Convert to numeric
    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )

    # Fill missing values
    df["TotalCharges"] = df["TotalCharges"].fillna(
        df["TotalCharges"].median()
    )

    return df