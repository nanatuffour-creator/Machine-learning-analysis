import joblib
import numpy as np

model = joblib.load("../models/cocoa_model.pkl")

def predict_yield(features):
    arr = np.array(features).reshape(1, -1)
    return model.predict(arr)[0]
