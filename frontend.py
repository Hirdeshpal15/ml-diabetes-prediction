import streamlit as st
import requests

# Your Azure API URL
API_URL = "https://ml-diabetes-api-hirdesh-d8gdc3f0e0a8hza4.germanywestcentral-01.azurewebsites.net/predict"

st.title("Diabetes Prediction App 🩺")

# Inputs
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.slider("Age", 1, 100, 30)
hypertension = st.selectbox("Hypertension", [0, 1])
heart_disease = st.selectbox("Heart Disease", [0, 1])
smoking_history = st.selectbox("Smoking History", ["never", "current", "former"])
bmi = st.number_input("BMI", 10.0, 50.0, 25.0)
hba1c = st.number_input("HbA1c Level", 3.0, 15.0, 5.5)
glucose = st.number_input("Blood Glucose Level", 50, 300, 120)

# Button
if st.button("Predict"):
    input_data = {
        "gender": gender,
        "age": age,
        "hypertension": hypertension,
        "heart_disease": heart_disease,
        "smoking_history": smoking_history,
        "bmi": bmi,
        "HbA1c_level": hba1c,
        "blood_glucose_level": glucose
    }

    response = requests.post(API_URL, json=input_data)

    if response.status_code == 200:
        result = response.json()
        st.success(f"Prediction: {result['diabetes']}")
    else:
        st.error("Error calling API")