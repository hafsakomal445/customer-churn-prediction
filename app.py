import streamlit as st

st.set_page_config(
    page_title="Customer Churn Prediction",
    layout="wide"
)

st.title("📉 Customer Churn Prediction")

st.write(
    "Predict whether a customer is likely to churn."
)
# Add Sidebar
st.sidebar.header("Customer Information")
# Create Input Fields

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
    "Tenure",
    0,
    72,
    12
)

monthly_charges = st.number_input(
    "Monthly Charges",
    0.0,
    200.0,
    50.0
)

total_charges = st.number_input(
    "Total Charges",
    0.0,
    10000.0,
    1000.0
)
# Prediction Button
if st.button("Predict"):
    st.success("Prediction generated")