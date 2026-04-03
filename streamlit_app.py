import streamlit as st
import pandas as pd

# Page settings
st.set_page_config(
    page_title="Health Risk Prediction",
    page_icon="🩺",
    layout="centered"
)

# Title
st.title("🩺 Personalized Health Risk Prediction")
st.write("Fill the details below to know your health risk")

# Input fields
recency = st.number_input(
    "Recency (Last health checkup in days)",
    min_value=0,
    step=1
)

frequency = st.number_input(
    "Frequency (Doctor visits per year)",
    min_value=0,
    step=1
)

monetary = st.number_input(
    "Medical Expense (Approx ₹)",
    min_value=0,
    step=100
)

time = st.number_input(
    "Health Issue Duration (in months)",
    min_value=0,
    step=1
)

# Predict button
if st.button("Predict Health Risk"):
    # Simple risk calculation logic
    score = (recency * 0.3) + (frequency * 0.3) + (time * 0.4)
    risk_percentage = min(int(score * 10), 100)

    st.subheader("🔍 Prediction Result")

    # Risk result
    if risk_percentage < 30:
        st.success(f"Low Risk ✅ ({risk_percentage}%)")
        st.info("You are healthy. Maintain your lifestyle with regular exercise and good diet.")
    elif risk_percentage < 60:
        st.warning(f"Medium Risk ⚠️ ({risk_percentage}%)")
        st.info("Please improve your diet, exercise regularly and reduce stress.")
    else:
        st.error(f"High Risk 🚨 ({risk_percentage}%)")
        st.info("Consult a doctor immediately and avoid unhealthy habits.")

    # Progress bar
    st.progress(risk_percentage)

    # Chart: use DataFrame for single values
    df = pd.DataFrame({
        "Metrics": ["Recency", "Frequency", "Monetary", "Time"],
        "Values": [recency, frequency, monetary, time]
    })

    st.subheader("📊 Health Input Overview")
    st.bar_chart(df.set_index("Metrics"))