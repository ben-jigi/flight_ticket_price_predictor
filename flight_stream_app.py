import streamlit as st
import joblib
import pandas as pd
import os

# ======================
# Load the trained model
# ======================
BASE_DIR = os.path.dirname(__file__)  # ensures path works locally and on Streamlit Cloud
model_path = os.path.join(BASE_DIR, "model", "flight_model.pkl")
pipeline = joblib.load(model_path)

# ======================
# App title
# ======================
st.title("Flight Fare Prediction 🚀")
st.write("Enter the flight details to predict the fare:")

# ======================
# Input fields
# ======================
Airline = st.selectbox("Airline", ["Airline A", "Airline B", "Airline C"])
Source = st.selectbox("Source City", ["City X", "City Y"])
Destination = st.selectbox("Destination City", ["City P", "City Q"])

Journey_Day = st.number_input("Journey Day", min_value=1, max_value=31, value=1)
Journey_Month = st.number_input("Journey Month", min_value=1, max_value=12, value=1)
Journey_Hour = st.number_input("Departure Hour", min_value=0, max_value=23, value=0)
Journey_Minute = st.number_input("Departure Minute", min_value=0, max_value=59, value=0)

Arrival_Hour = st.number_input("Arrival Hour", min_value=0, max_value=23, value=0)
Arrival_Minute = st.number_input("Arrival Minute", min_value=0, max_value=59, value=0)

Total_Stops = st.selectbox("Total Stops", ["non-stop", "1 stop", "2 stops", "3 stops", "4 stops"])
Duration = st.number_input("Duration (minutes)", min_value=30, max_value=1440, value=120)

# ======================
# Predict button
# ======================
if st.button("Predict Fare"):
    input_data = pd.DataFrame({
        "Airline": [Airline],
        "Source": [Source],
        "Destination": [Destination],
        "Journey_Day": [Journey_Day],
        "Journey_Month": [Journey_Month],
        "Journey_Hour": [Journey_Hour],
        "Journey_Minute": [Journey_Minute],
        "Arrival_Hour": [Arrival_Hour],
        "Arrival_Minute": [Arrival_Minute],
        "Total_Stops": [Total_Stops],
        "Duration": [Duration]
    })
    
    try:
        prediction = pipeline.predict(input_data)
        st.success(f"Predicted Flight Fare: ₹{prediction[0]:.2f}")
    except Exception as e:
        st.error(f"Error in prediction: {e}")

