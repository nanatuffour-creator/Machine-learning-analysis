import streamlit as st
import sys
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append('../src')

from src.predict import predict_yield

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
    with open("predicted_results.txt","w") as f:
        f.write(f"{rainfall},{temperature},{humidity},{soil_pH},{nitrogen},{phosphorus},{potassium},{result:.2f}\n")

    st.success(f"Predicted Yield: {result:.2f} tons/hectare")
