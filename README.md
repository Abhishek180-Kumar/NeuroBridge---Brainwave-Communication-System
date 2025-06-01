# NeuroBridge - Brainwave Communication System

## Project Overview
NeuroBridge is a Brain-Computer Interface (BCI) project that predicts user thoughts from EEG signals and provides voice feedback using text-to-speech. The project uses a machine learning model for classification and a Streamlit-based web app for interaction.

## Features
- Predicts thoughts from EEG feature input.
- Converts predicted thoughts to speech asynchronously.
- Interactive web UI with Streamlit.
- Non-blocking TTS using pyttsx3 and threading.

## Technologies
- Python
- Streamlit
- pyttsx3
- scikit-learn / joblib

## Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/neurobridge.git
   cd neurobridge
