import streamlit as st
import joblib

st.title('Heart Disease Prediction')
st.header('Data Analysis')


# ---------------- Inputs ---------------- #

age                 = st.slider("Enter your age",min_value=18,max_value=100,value=0)
sex                 = st.selectbox("Gender",["Female", "Male", "Other"])
chest_pain_type     = chest_pain_type = st.selectbox("Chest Pain Type",options={"1 – Typical Angina": 1,
                                                                                "2 – Atypical Angina": 2,
                                                                                "3 – Non-Anginal Pain": 3,
                                                                                "4 – Asymptomatic": 4,}.keys(),
                      help="Type of chest pain experienced")
resting_bp          = st.number_input("Resting Blood Pressure (mm Hg)",min_value=50,max_value=260,step=1)
cholesterol         = st.number_input("Serum Cholesterol (mg/dl)",min_value=70,max_value=600,step=1)
fasting_blood_sugar = st.selectbox("Fasting Blood Sugar > 120 mg/dl",options=["Yes", "No"],
                      help="Whether fasting blood sugar exceeds 120 mg/dl")
resting_ecg         = st.selectbox("Resting ECG Result",options=["0 – Normal",
                                                                 "1 – ST-T Wave Abnormality",
                                                                 "2 – Left Ventricular Hypertrophy"],
                       help="Resting electrocardiographic results")
max_heart_rate      = st.number_input("Maximum Heart Rate Achieved (bpm)",min_value=30,max_value=230,step=1)
exercise_angina     = st.selectbox("Exercise-Induced Angina",options=["Yes", "No"],
                       help="Angina brought on by physical exertion")
st_depression       = st.number_input("ST Depression (induced by exercise)",min_value=0.0,max_value=10.0,step=0.1,format="%.1f")

slope_map = {
    "1 – Upsloping": 1,
    "2 – Flat": 2,
    "3 – Downsloping": 3
}
slope = slope_map[st.selectbox("Slope of ST Segment", list(slope_map.keys()))]

ca = st.selectbox("Number of Major Vessels (0–3)", [0, 1, 2, 3])

thal_map = {
    "1 – Normal": 1,
    "2 – Fixed Defect": 2,
    "3 – Reversible Defect": 3
}
thal = thal_map[st.selectbox("Thalassemia Type", list(thal_map.keys()))]


# ---------------- Load pkl Files ---------------- #

final = joblib.load(r'Heart Disease.pkl')  
stand = joblib.load(r'ss.pkl')

# ---------------- Buttons ---------------- #
    
predict = st.button("Predict") 

# ---------------- Prediction ---------------- #

if predict:

   result = final.predict(stand.transform([[age, sex, chest_pain_type, resting_bp,
          cholesterol, fasting_blood_sugar, resting_ecg, max_heart_rate,
          exercise_angina, st_depression, slope, ca, thal]]))[0]


    if result == 0:
        st.success("Disease Diagnosed")

    else:
        st.error("No Disease Diagnosed")