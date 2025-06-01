import streamlit as st
from predict import predict_thought

st.title("🧠 NeuroBridge - Brainwave Communication")

if st.button("Predict Thought from EEG"):
    intent = predict_thought([0.45, 0.32, 0.21, 0.55])
    st.success(f"Predicted Thought: {intent}")