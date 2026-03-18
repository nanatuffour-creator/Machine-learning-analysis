import streamlit as st
import sys
sys.path.append('../src')

from  cocoa_yield_ml_project/src/predict.py import predict_yield

st.title("Cocoa Yield Prediction (Ghana)")

rainfall = st.number_input("Rainfall (mm)")
temperature = st.number_input("Temperature (°C)")
humidity = st.number_input("Humidity (%)")
soil_pH = st.number_input("Soil pH")
nitrogen = st.number_input("Nitrogen")
phosphorus = st.number_input("Phosphorus")
potassium = st.number_input("Potassium")

if st.button("Predict"):
    features = [rainfall, temperature, humidity, soil_pH, nitrogen, phosphorus, potassium]
    result = predict_yield(features)
    st.success(f"Predicted Yield: {result:.2f} tons/hectare")
