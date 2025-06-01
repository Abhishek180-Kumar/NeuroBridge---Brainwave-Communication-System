# predict.py
import joblib
import numpy as np
import pyttsx3
import threading

model = joblib.load("eeg_classifier.pkl")

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def predict_thought(eeg_signal):
    features = np.array([eeg_signal])
    intent = model.predict(features)[0]
    print("Predicted Intent:", intent)

    # Run TTS in separate thread to avoid Streamlit conflict
    threading.Thread(target=speak, args=(intent,), daemon=True).start()
    
    return intent
