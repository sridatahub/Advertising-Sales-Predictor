import streamlit as st
import numpy as np
import pickle
import os

# Load model (same folder)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "Ad_Sales_model.pkl")

with open(model_path, "rb") as file:
    model = pickle.load(file)

st.title("Ad Sales Prediction App")

st.subheader("Enter Advertisement Cost")

tv = st.number_input("TV Advertising Cost", min_value=0.0)
radio = st.number_input("Radio Advertising Cost", min_value=0.0)
newspaper = st.number_input("Newspaper Advertising Cost", min_value=0.0)

if st.button("Predict Sales"):
    features = np.array([[tv, radio, newspaper]])
    prediction = model.predict(features)

    st.success(f"Predicted Sales: {prediction[0]:.2f}")
