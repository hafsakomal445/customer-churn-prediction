import streamlit as st
import pandas as pd

from src.prediction.predict import predict_churn

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📉",
    layout="wide"
)

# ==================================================
# HEADER
# ==================================================

st.title("📉 Customer Churn Prediction Dashboard")

st.write(
    "Predict whether a telecom customer is likely to churn."
)

# ==================================================
# PROJECT METRICS
# ==================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Best Model",
        "Random Forest"
    )

with col2:
    st.metric(
        "CV F1 Score",
        "0.6358"
    )

with col3:
    st.metric(
        "Dataset Size",
        "7043"
    )

# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.header("Customer Information")

# ==================================================
# INPUTS
# ==================================================

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

senior = st.selectbox(
    "Senior Citizen",
    [0, 1]
)

partner = st.selectbox(
    "Partner",
    ["Yes", "No"]
)

dependents = st.selectbox(
    "Dependents",
    ["Yes", "No"]
)

tenure = st.slider(
    "Tenure (Months)",
    0,
    72,
    12
)

phone_service = st.selectbox(
    "Phone Service",
    ["Yes", "No"]
)

multiple_lines = st.selectbox(
    "Multiple Lines",
    ["Yes", "No", "No phone service"]
)

internet_service = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

online_security = st.selectbox(
    "Online Security",
    ["Yes", "No", "No internet service"]
)

online_backup = st.selectbox(
    "Online Backup",
    ["Yes", "No", "No internet service"]
)

device_protection = st.selectbox(
    "Device Protection",
    ["Yes", "No", "No internet service"]
)

tech_support = st.selectbox(
    "Tech Support",
    ["Yes", "No", "No internet service"]
)

streaming_tv = st.selectbox(
    "Streaming TV",
    ["Yes", "No", "No internet service"]
)

streaming_movies = st.selectbox(
    "Streaming Movies",
    ["Yes", "No", "No internet service"]
)

contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

paperless_billing = st.selectbox(
    "Paperless Billing",
    ["Yes", "No"]
)

payment_method = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    max_value=200.0,
    value=70.0
)

total_charges = st.number_input(
    "Total Charges",
    min_value=0.0,
    max_value=10000.0,
    value=1000.0
)

# ==================================================
# PREDICTION BUTTON
# ==================================================

if st.button("Predict Churn"):

    input_df = pd.DataFrame({
        "gender": [gender],
        "SeniorCitizen": [senior],
        "Partner": [partner],
        "Dependents": [dependents],
        "tenure": [tenure],
        "PhoneService": [phone_service],
        "MultipleLines": [multiple_lines],
        "InternetService": [internet_service],
        "OnlineSecurity": [online_security],
        "OnlineBackup": [online_backup],
        "DeviceProtection": [device_protection],
        "TechSupport": [tech_support],
        "StreamingTV": [streaming_tv],
        "StreamingMovies": [streaming_movies],
        "Contract": [contract],
        "PaperlessBilling": [paperless_billing],
        "PaymentMethod": [payment_method],
        "MonthlyCharges": [monthly_charges],
        "TotalCharges": [total_charges]
    })

    prediction, probability = predict_churn(input_df)

    st.markdown("---")

    col1, col2 = st.columns(2)

    # ==========================================
    # LEFT COLUMN
    # ==========================================

    with col1:

        st.subheader("Prediction Result")

        if prediction == 1:

            st.error(
                f"⚠️ Customer is likely to churn ({probability:.2%})"
            )

        else:

            st.success(
                f"✅ Customer is likely to stay ({1 - probability:.2%})"
            )

        st.subheader("Churn Probability")

        st.progress(float(probability))

        st.write(
            f"Probability of Churn: {probability:.2%}"
        )

    # ==========================================
    # RIGHT COLUMN
    # ==========================================

    with col2:

        st.subheader("Risk Analysis")

        if probability < 0.30:
            risk = "LOW"

        elif probability < 0.60:
            risk = "MEDIUM"

        else:
            risk = "HIGH"

        if risk == "LOW":
            st.success("🟢 LOW RISK")

        elif risk == "MEDIUM":
            st.warning("🟡 MEDIUM RISK")

        else:
            st.error("🔴 HIGH RISK")

    # ==========================================
    # CUSTOMER DATA
    # ==========================================

    st.markdown("---")

    st.subheader("Customer Data")

    st.dataframe(input_df)

# ==================================================
# FOOTER
# ==================================================

st.markdown("---")

st.markdown(
    """
    ### Developed by Hafsa Komal

    Machine Learning Engineer Portfolio Project

    Customer Churn Prediction using Random Forest
    """
)