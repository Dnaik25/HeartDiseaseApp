import streamlit as st
import pandas as pd
import pickle

# Load pre-trained models (replace with your actual models)
with open("HeartDiseaseCleveland.pkl", "rb") as f:
    cleveland_model = pickle.load(f)


# Dataset Features (Replace with your actual dataset features)
CLEVELAND_FEATURES = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
       'exang', 'oldpeak', 'slope', 'ca_1.0', 'ca_2.0',
       'ca_3.0', 'thal_6.0', 'thal_7.0']

import streamlit as st


def get_user_input():
    user_input = {}

    # Numerical input
    age = st.number_input("Age", min_value=20, max_value=85)
    user_input["age"] = age

    # Categorical input

    sex_mapping = {"Male": 1, "Female": 0}

    sex = st.radio("Sex", options=["Male", "Female"])
    user_input["sex"] = sex

    cp_mapping = {"Typical Angina": 1, "Atypical Angina": 2, "Non-Anginal Pain": 3, "Asymptomatic": 4}

    cp = st.radio("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"])
    user_input["cp"] = cp

    trestbps = st.slider("Resting Blood Pressure", 50, 200)
    user_input["trestbps"] = trestbps

    chol = st.number_input("Serum Choelstrol", min_value=100, max_value=600)
    user_input["chol"] = chol

    fbs_mapping = {"Yes": 1, "No": 0}

    fbs = st.selectbox("Fasting Blood sugar > 120 mg/dl", options=["Yes", "No"])
    user_input["fbs"] = fbs

    restecg_mapping = {"Normal": 0, "ST-T wave abnormality": 1, "Left ventricular hypertrophy": 2 }

    restecg = st.selectbox("Resting ECG results", options=["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"])
    user_input["restecg"] = restecg

    thalach = st.number_input("Max Heart Rate", min_value=60, max_value=250)
    user_input["thalach"] = thalach

    exang_mapping = {"Yes": 1, "No": 0}

    exang = st.selectbox("Excercise induced angina", options=["Yes", "No"])
    user_input["exang"] = exang

    oldpeak = st.number_input("ST depression induced by exercise", min_value=0, max_value=10)
    user_input["oldpeak"] = oldpeak

    slope_mapping = {"Upsloping": 1, "Flat": 2, "Downsloping":3}

    slope = st.selectbox("Slope of Peak exercise ST", options=["Upsloping", "Flat", "Downsloping"])
    user_input["slope"] = slope

    ca1_0_mapping = {"Yes": 1, "No": 0}

    ca1_0 = st.selectbox("1 Major Blood Vessel colored by Floroscopy", options=["Yes", "No"])
    user_input["ca_1.0"] = ca1_0

    ca2_0_mapping = {"Yes": 1, "No": 0}

    ca2_0 = st.selectbox("2 Major Blood Vessel colored by Floroscopy", options=["Yes", "No"])
    user_input["ca_2.0"] = ca2_0

    ca3_0_mapping = {"Yes": 1, "No": 0}

    ca3_0 = st.selectbox("3 Major Blood Vessel colored by Floroscopy", options=["Yes", "No"])
    user_input["ca_3.0"] = ca3_0

    thal6_0_mapping = {"Yes": 1, "No": 0}

    thal6_0 = st.selectbox("Thallesemia Fixed defect", options=["Yes", "No"])
    user_input["thal_6.0"] = thal6_0

    thal7_0_mapping = {"Yes": 1, "No": 0}

    thal7_0 = st.selectbox("Thallesemia Reversable defect", options=["Yes", "No"])
    user_input["thal_7.0"] = thal7_0
    ca1_0_mapping = {"Yes": 1, "No": 0}

    mappings = {
        "sex": sex_mapping,
        "cp": cp_mapping,
        "fbs": fbs_mapping,
        "restecg": restecg_mapping,
        "exang": exang_mapping,
        "slope": slope_mapping,
        "ca_1.0": ca1_0_mapping,
        "ca_2.0": ca2_0_mapping,
        "ca_3.0": ca3_0_mapping,
        "thal_6.0": thal6_0_mapping,
        "thal_7.0": thal7_0_mapping
        }

    for key, mapping in mappings.items():
        user_input[key] = mapping[user_input[key]]

    return user_input

# def get_features(dataset_choice):
#     if dataset_choice == "UCI Heart Disease":
#         return {feature: st.slider(feature, 0, 100) for feature in CLEVELAND_FEATURES}

def predict(features, model):
    df = pd.DataFrame([features])
    return model.predict(df)[0]


def main():
    st.title("Heart Disease Prediction")

    # dataset_choice = st.selectbox("Choose a dataset:", ["UCI Heart Disease"])
    # features = get_features(dataset_choice)

    st.write("Please answer below questions regarding you health data results")

    user_data = get_user_input()
    st.write("Summary of the details you provided:")
    st.write(user_data)

    if st.button("Predict"):
        # if dataset_choice == "UCI Heart Disease":
        prediction = predict(user_data, cleveland_model)

        if prediction == 1:
            display_string = "Likely Risk of Heart Disease"
        else:
            display_string = "It is unlikely that you have heart disease"

        st.text_input("Prediction Result", value=display_string, disabled=True)

        if prediction == 1:
            st.write(
                "The prediction indicates a likelihood of heart disease. Please consult with a healthcare professional.")
        else:
            st.write(
                "The prediction indicates a lower likelihood of heart disease. However, always consult with a healthcare professional for a comprehensive assessment.")

st.markdown(
    """
    <style>
        .reportview-container {
            background: url("https://www.heart.org/-/media/Images/News/2020/April-2020/0409WomenINOCA_SC.jpg") no-repeat center center fixed;
            background-size: cover;
        }
    </style>
    """,
    unsafe_allow_html=True
)

if __name__ == "__main__":
    main()
