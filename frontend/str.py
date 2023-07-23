import streamlit as st
import requests

# title 
st.title("Plant Disease Recognition")
st.sidebar.title("Options")

# Selectbox 
plant_type = st.sidebar.selectbox("Select plant type", ["Tomato", "Potato"])

# Upload image
uploaded_file = st.file_uploader("Upload image", type=["jpg", "jpeg", "png"])

# Button 
if st.button("Predict"):
    if uploaded_file is not None:
        # Prepare request
        files = {"file": uploaded_file}
        url = f"http://localhost:8000/predict"
        params = {"plant_type": plant_type}
        
        # Send API request and get response
        response = requests.post(url, files=files, params=params)
        prediction = response.json()
        
        # Display result
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        st.success(f"Prediction: {prediction['class']} ({prediction['confidence']:.2f})")
    else:
        st.warning("Please upload an image for prediction")
