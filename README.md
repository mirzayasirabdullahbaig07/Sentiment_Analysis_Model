# 📊 Sentiment Analysis Web App

An **interactive AI-powered web application** built with **Streamlit** that predicts the **sentiment of text** as positive or negative.  
This app supports **both Machine Learning and Deep Learning models** for sentiment analysis.

---

## 🚀 Live Demo  
🔗 [Live App on Streamlit](https://sentimentanalysismodel07.streamlit.app/)

---

## 📌 Features  
- **Predict Sentiment**: Detects whether text is positive or negative.  
- **Dual Model Support**: Choose between:
  1. Machine Learning model (`.pkl`)  
  2. Deep Learning model (`.keras`)  
- **Interactive UI**: Simple input form for entering text.  
- **Confidence Score**: Displays prediction probability for better insights.  
- **User-friendly Interface**: Built using Streamlit with sidebar options.  
- **Portfolio Links**: About Me section included in sidebar.  

---

## 🔍 Usage  
1. Open the app in your browser.  
2. Select a model from the sidebar:  
   - **Machine Learning Model (.pkl)**  
   - **Deep Learning Model (.keras)**  
3. Enter your text in the input area.  
4. Click **Predict**.  
5. The app will display:  
   - Sentiment: 😊 Positive / ☹️ Negative  
   - Confidence Score (0–1)  

---

## 📸 Screenshots
### 🏠 Home Page
<img width="1899" height="828" alt="image" src="https://github.com/user-attachments/assets/10d9d8fc-c345-4279-92ab-b903405000a6" />

### 😊 Positive Sentiment Prediction
<img width="1895" height="855" alt="image" src="https://github.com/user-attachments/assets/0858d871-479c-4097-8e5b-e4ec03ee8ccf" />

### ☹️ Negative Sentiment Prediction
<img width="1916" height="844" alt="image" src="https://github.com/user-attachments/assets/ee94dd6e-5dd6-4a15-89a2-b204d3b98870" />

---

## ⚙️ Tech Stack  
- **Python 3.9+**  
- **Streamlit** (Web App)  
- **NumPy & Pandas** (Data Processing)  
- **TensorFlow / Keras** (Deep Learning Model)  
- **Scikit-learn & Joblib** (Machine Learning Model & Serialization)  

---

## 📄 How It Works  
- The text is **preprocessed using a tokenizer**.  
- Converted to **sequences** and **padded** to match model input.  
- The selected model predicts the **sentiment score**.  
- Score > 0.5 → Positive sentiment; Score ≤ 0.5 → Negative sentiment.  

---

## 👨‍💻 Author  
**Mirza Yasir Abdullah Baig**  

- 💼 [LinkedIn](https://www.linkedin.com/in/mirza-yasir-abdullah-baig/)  
- 🌐 [Kaggle](https://www.kaggle.com/code/mirzayasirabdullah07)  
- 💻 [GitHub](https://github.com/mirzayasirabdullahbaig07)  

---

## ❤️ Acknowledgements  
- [TensorFlow/Keras](https://www.tensorflow.org/)  
- [Scikit-learn](https://scikit-learn.org/stable/)  
- [Streamlit Documentation](https://docs.streamlit.io/)  

---

## ⚠️ Disclaimer  
This project is for **educational purposes only**.  
It is not intended for commercial use but demonstrates **text-based sentiment analysis with AI**.  

---

## 📄 License  
This project is open-source and available under the **MIT License**.  

---
