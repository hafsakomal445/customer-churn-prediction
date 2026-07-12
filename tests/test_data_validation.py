import pandas as pd

df = pd.read_csv(
    "data/processed/customer_churn_clean.csv"
)

assert df.isnull().sum().sum() == 0

print("Data Validation Passed")