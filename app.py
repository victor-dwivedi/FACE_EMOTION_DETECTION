import streamlit as st
import json
from PIL import Image
import numpy as np
import requests

# Load the facial emotion model
with open('facialemotionmodel.json', 'r') as f:
    model_data = json.load(f)

# Function to predict emotion (mock implementation)
def predict_emotion(image_array, model_data):
    # Insert your model's prediction logic here
    return "Happy"  # Dummy emotion for example

st.title("Facial Emotion Recognition")

# Upload an image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Convert image to array and predict emotion
    image_array = np.array(image)
    emotion = predict_emotion(image_array, model_data)
    
    st.write(f"Predicted Emotion: {emotion}")
