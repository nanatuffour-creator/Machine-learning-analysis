import streamlit as st
# import sys

# sys.path.append('../src')

import joblib
import numpy as np

model = joblib.load("../models/cocoa_model.pkl")

def predict_yield(features):
    arr = np.array(features).reshape(1, -1)
    return model.predict(arr)[0]

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
