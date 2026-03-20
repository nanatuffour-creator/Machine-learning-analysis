import joblib
import os
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from data_preprocessing import load_data, preprocess_data, split_data

df = load_data("../data/raw/cocoa_data.csv")
X, y = preprocess_data(df)
X_train, X_test, y_train, y_test = split_data(X, y)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

preds = model.predict(X_test)

print("MSE:", mean_squared_error(y_test, preds))
print("R2:", r2_score(y_test, preds))

BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # repo root
MODEL_PATH = os.path.join(BASE_DIR, "models", "cocoa_model.pkl")

model = joblib.load(MODEL_PATH)
print("Model saved!")
