import streamlit as st
import joblib

st.title('Heart Disease Prediction')
st.header('Data Analysis')

# ---------------- Inputs ---------------- #
age = st.slider("Enter your age", min_value=18, max_value=100, value=18)

sex = st.selectbox("Gender", ["Female", "Male"])
sex = 0 if sex == "Female" else 1

chest_pain_map = {
    "1 - Typical Angina": 1,
    "2 - Atypical Angina": 2,
    "3 - Non-Anginal Pain": 3,
    "4 - Asymptomatic": 4
}
chest_pain_type = chest_pain_map[st.selectbox("Chest Pain Type", list(chest_pain_map.keys()))]

resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", min_value=50, max_value=260, step=1, value=50)
cholesterol = st.number_input("Cholesterol (mg/dl)", min_value=70, max_value=600, step=1, value=70)

fasting_blood_sugar = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["Yes", "No"])
fasting_blood_sugar = 1 if fasting_blood_sugar == "Yes" else 0

resting_ecg_map = {
    "0 - Normal": 0,
    "1 - ST-T Wave Abnormality": 1,
    "2 - Left Ventricular Hypertrophy": 2
}
resting_ecg = resting_ecg_map[st.selectbox("Resting ECG Result", list(resting_ecg_map.keys()))]

max_heart_rate = st.number_input("Maximum Heart Rate Achieved (bpm)", min_value=30, max_value=230, step=1, value=30)

exercise_angina = st.selectbox("Exercise-Induced Angina", ["Yes", "No"])
exercise_angina = 1 if exercise_angina == "Yes" else 0

st_depression = st.number_input("ST Depression", min_value=0.0, max_value=10.0, step=0.1, format="%.1f")


# ---------------- Load pkl Files ---------------- #
final = joblib.load(r'Heart Disease.pkl')
stand = joblib.load(r'ss.pkl')

# ---------------- Buttons ---------------- #
predict = st.button("Predict")

# ---------------- Prediction ---------------- #
if predict:
    result = final.predict(stand.transform([[age, sex, chest_pain_type, resting_bp,
              cholesterol, fasting_blood_sugar, resting_ecg, max_heart_rate,
              exercise_angina, st_depression]]))[0]
    if result == 1:
        st.error("Disease Diagnosed")
    else:
        st.success("No Disease Diagnosed")