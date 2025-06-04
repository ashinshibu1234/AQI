import warnings
warnings.filterwarnings("ignore")

import pickle
import streamlit as st
import base64

# ✅ Set page config - MUST be the first Streamlit command
st.set_page_config(page_title="🌍 Air Quality Predictor", layout="centered", page_icon="🌿")

# Load the trained model
with open(r"C:\Users\USER\Main_Project.pkl", 'rb') as file:
    reg2 = pickle.load(file)

# Function to convert image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Convert background image to base64
bg_image = get_base64_image(r"C:\Users\USER\Downloads\wmremove-transformed.png")

# Inject CSS for background image, white font color, and bold text
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bg_image}");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }}

    h1, h2, h3, h4, h5, h6, p, div, span, label {{
        color: white !important;
        font-weight: bold !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Inject CSS for button styling
st.markdown(
    """
    <style>
    div.stButton > button {
        color: white !important;
        font-weight: bold !important;
        background-color: #0078D4; /* Adjust button color as needed */
        border-radius: 5px;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit App Content
st.title("🌍 Air Quality Index Prediction")
st.markdown("---")

# AQI Explanation Section
st.subheader("📖 What is an AQI 🏭🌿")
st.markdown("""
The **Air Quality Index (AQI) 🚦** is an essential measure that helps assess and communicate the air pollution levels in a specific area.  
It consolidates data from multiple pollutants into a single index value, offering an easily interpretable scale with **color codes** and **health impact indicators**.

### 🌡️ AQI Levels & Health Implications 🌏
| AQI Range  | Status                             | Health Impact |
|------------|----------------------------------|---------------|
| **0–50**   | ✅ **Good** 🌿                   | Minimal risk, air quality is ideal |
| **51–100** | 🟡 **Moderate** 🌤               | Acceptable air quality; slight discomfort for sensitive individuals |
| **101–200**| 🟠 **Unhealthy for Sensitive Groups** 🤧 | Some health effects for vulnerable people |
| **201–300**| 🔴 **Poor** 😷                   | Increased health risks for all individuals |
| **301–400**| 🟣 **Very Poor** 🏥              | Serious health effects and respiratory distress possible |
| **401–500**| ⚫ **Severe** 🚨                 | Hazardous air quality, emergency health warnings |
""")
st.markdown("---")

# Input Section
st.subheader("🔢 Enter Pollution Levels (µg/m³ or mg/m³) 🏭")
st.markdown("Provide the concentration levels of key pollutants to predict the AQI:")

co = st.number_input("**CO (mg/m³) 🏭**", min_value=0.0, format="%.2f")
ozone = st.number_input("**Ozone (µg/m³) 🌎**", min_value=0.0, format="%.2f")
no2 = st.number_input("**NO₂ (µg/m³) 🚗**", min_value=0.0, format="%.2f")
so2 = st.number_input("**SO₂ (µg/m³) 🌋**", min_value=0.0, format="%.2f")
pm25 = st.number_input("**PM2.5 (µg/m³) ☁️**", min_value=0.0, format="%.2f")
pm10 = st.number_input("**PM10 (µg/m³) 🌫️**", min_value=0.0, format="%.2f")

# Prediction and Display
if st.button("✅ Predict AQI"):
    prediction = reg2.predict([[co, ozone, no2, so2, pm25, pm10]])[0]
    st.markdown(f"### 🧪 Predicted AQI: `{round(prediction, 2)}`")

    if prediction <= 50:
        st.success("🌿 **Good Air Quality** ✅")
        st.info("🌍 The air quality is excellent, posing little or no health risk.")

    elif prediction <= 100:
        st.warning("🌤 **Moderate Air Quality** 🟡")
        st.info("🏥 Air quality is acceptable, though sensitive individuals may experience mild discomfort.")

    elif prediction <= 200:
        st.warning("🟠 **Unhealthy for Sensitive Groups** 🤧")
        st.info("😷 Sensitive individuals may experience health effects, though the general public is not likely to be impacted.")

    elif prediction <= 300:
        st.error("🔴 **Poor Air Quality** 😷")
        st.info("🚨 Everyone may experience adverse health effects, and vulnerable groups may suffer more serious consequences.")

    elif prediction <= 400:
        st.error("🟣 **Very Poor Air Quality** 🏥")
        st.info("⚠️ Significant health risks, especially for people with respiratory conditions.")

    elif prediction <= 500:
        st.error("⚫ **Severe Air Pollution** 🚨")
        st.info("❌ Extremely hazardous conditions; breathing discomfort likely for all.")

    else:
        st.error("🚨 **Beyond the AQI Scale** ❗")
        st.warning("☠️ This indicates dangerously high pollution levels posing severe health risks to everyone.")

st.markdown("---")
st.caption("Stay informed. Stay safe. 🌎💙")