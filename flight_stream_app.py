# app.py
import streamlit as st
import pandas as pd
import joblib

# ------------------------------
# Load model
# ------------------------------
model_path = "model/flight_model.pkl"  # update if your model is in a different folder
pipeline = joblib.load(model_path)

# ------------------------------
# Page title
# ------------------------------
st.title("Flight Fare Prediction")
st.write("Enter flight details below and get an estimated fare:")


airline = st.selectbox("Airline", ["IndiGo", "Air India", "Jet Airways", "SpiceJet", "Vistara", "GoAir"])
source = st.selectbox("Source", ["Delhi", "Kolkata", "Mumbai", "Chennai"])
destination = st.selectbox("Destination", ["Cochin", "Banglore", "New Delhi", "Hyderabad", "Kolkata"])
total_stops = st.selectbox("Total Stops", ["non-stop", "1 stop", "2 stops", "3 stops", "4 stops"])
journey_day = st.slider("Journey Day", 1, 31, 1)
journey_month = st.slider("Journey Month", 1, 12, 1)
journey_time = st.slider("Journey Hour of Day (0-23)", 0, 23, 12)
arrival_time = st.slider("Arrival Hour of Day (0-23)", 0, 23, 12)
duration = st.slider("Duration (in minutes)", 30, 1440, 180)


weekday_num = st.slider("Weekday (0=Monday, 6=Sunday)", 0, 6, 0)

input_df = pd.DataFrame({
    "Airline": [airline],
    "Source": [source],
    "Destination": [destination],
    "Total_Stops": [total_stops],
    "journey_day": [journey_day],
    "journey_month": [journey_month],
    "journey_time": [journey_time],
    "Arrival_time": [arrival_time],
    "durations": [duration],
    "weekday_num": [weekday_num]
})


if st.button("Predict Fare"):
    prediction = pipeline.predict(input_df)
    st.success(f"Estimated Flight Fare: ₹ {round(prediction[0], 2)}")
