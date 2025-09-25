import streamlit as st
import joblib
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Sidebar
st.sidebar.title("ℹ️ About")

st.sidebar.subheader("About this App")
st.sidebar.write("""
This Sentiment Analysis App allows you to analyze text and predict whether it is
positive or negative. You can choose between two types of models:
1. Machine Learning model (.pkl)
2. Deep Learning model (.keras)

Simply enter your text, select the model, and click 'Predict'.
""")

st.sidebar.subheader("About Me")
st.sidebar.write("""
Hi! I am **Mirza Yasir Abdullah Baig**, a passionate AI/ML enthusiast.
You can check out my profiles below:
""")
st.sidebar.markdown("[GitHub](https://github.com/mirzayasirabdullahbaig07)")
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/mirza-yasir-abdullah-baig/)")
st.sidebar.markdown("[Kaggle](https://www.kaggle.com/code/mirzayasirabdullah07)")

# Main title
st.title("📊 Sentiment Analysis App By Mirza Yasir Abdullah Baig")

# Sidebar: select model
model_option = st.sidebar.selectbox(
    "Select Model",
    ("Machine Learning Model (.pkl)", "Deep Learning Model (.keras)")
)

# Load models based on selection
if model_option == "Machine Learning Model (.pkl)":
    model = joblib.load("model.pkl")
    tokenizer = joblib.load("tokenizer.pkl")
else:
    model = load_model("sentiment_model.keras")
    tokenizer = joblib.load("tokenizer.pkl")  # still need tokenizer for text preprocessing

# Text input
user_input = st.text_area("Enter text to analyze sentiment:")

if st.button("Predict"):
    if user_input.strip() != "":
        # Convert text to sequences using tokenizer
        seq = tokenizer.texts_to_sequences([user_input])
        padded = pad_sequences(seq, maxlen=100)

        if model_option == "Machine Learning Model (.pkl)":
            prediction = model.predict(padded)[0]
        else:
            prediction = model.predict(padded)[0][0]

        sentiment = "😊 Positive" if prediction > 0.5 else "☹️ Negative"
        st.success(f"Prediction: {sentiment}")
        # If prediction is an array, get the first element
        confidence = float(prediction)  # convert to scalar
        st.write(f"Confidence Score: {confidence:.2f}")
    else:
        st.warning("Please enter some text.")
