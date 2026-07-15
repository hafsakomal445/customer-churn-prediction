import joblib
import pandas as pd

# Load model and feature columns
model = joblib.load("models/churn_model.pkl")
feature_columns = joblib.load("models/feature_columns.pkl")


def predict_churn(input_df):
    """
    Predict customer churn probability.
    """

    # One-hot encoding
    input_encoded = pd.get_dummies(
        input_df,
        drop_first=True
    )

    # Match training columns
    input_encoded = input_encoded.reindex(
        columns=feature_columns,
        fill_value=0
    )

    prediction = model.predict(input_encoded)[0]

    probability = model.predict_proba(
        input_encoded
    )[0][1]

    return prediction, probability