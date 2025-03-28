import streamlit as st
import requests

st.set_page_config(page_title="Sentiment Analysis", page_icon="🔍", layout="centered")

st.title("🔍 Sentiment Analysis from Text")
st.markdown("Explore the emotion beyond the words!")

# Take text user input
user_input = st.text_area("Write the text:")

# URL on GCP backend
API_URL = "http://130.211.51.190/predict"  

# Predict when click the button
if st.button("Predict"):
    if not user_input.strip():
        st.warning("Please enter non-empty text")
    else:
        try:
            response = requests.post(API_URL, json={"text": user_input})
            if response.status_code == 200:
                result = response.json()
                sentiment = result.get("sentiment", "unknown")
                st.success(f"Prediction: **{sentiment.upper()}**")
            else:
                st.error("API returned an error")
        except Exception as e:
            st.error(f"API is not available. Hata: {e}")
