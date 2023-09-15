import pandas as pd
import pickle
import streamlit as st


# Load pre-trained models (replace with your actual models)
with open("HeartDiseaseCleveland.pkl", "rb") as f:
    cleveland_model = pickle.load(f)

with open("HeartDiseaseBRFSS.pkl", "rb") as f:
    brfss_model = pickle.load(f)


# Dataset Features (Replace with your actual dataset features)
CLEVELAND_FEATURES = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
       'exang', 'oldpeak', 'slope', 'ca_1.0', 'ca_2.0',
       'ca_3.0', 'thal_6.0', 'thal_7.0']

BRFSS_FEATURES = ['Mental_health', 'General_health', 'Stroke', 'COPD', 'Kidney_disease',
       'High_BP', 'High_cholestrol', 'Sex', 'Age_group', 'HIV', 'Income_level',
       'Education_level', 'Fruit_intake', 'Green_intake', 'Potato_servings',
       'Heart_disease']

def get_cleveland_input():
    user_input_cleveland = {}

    # Numerical input
    age = st.number_input("Age", min_value=20, max_value=85)
    user_input_cleveland["age"] = age

    # Categorical input

    sex_mapping = {"Male": 1, "Female": 0}

    sex = st.radio("Sex", options=["Male", "Female"])
    user_input_cleveland["sex"] = sex

    cp_mapping = {"Typical Angina": 1, "Atypical Angina": 2, "Non-Anginal Pain": 3, "Asymptomatic": 4}

    cp = st.radio("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"])
    user_input_cleveland["cp"] = cp

    trestbps = st.slider("Resting Blood Pressure", 50, 200)
    user_input_cleveland["trestbps"] = trestbps

    chol = st.number_input("Serum Choelstrol", min_value=100, max_value=600)
    user_input_cleveland["chol"] = chol

    fbs_mapping = {"Yes": 1, "No": 0}

    fbs = st.selectbox("Fasting Blood sugar > 120 mg/dl", options=["Yes", "No"])
    user_input_cleveland["fbs"] = fbs

    restecg_mapping = {"Normal": 0, "ST-T wave abnormality": 1, "Left ventricular hypertrophy": 2 }

    restecg = st.selectbox("Resting ECG results", options=["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"])
    user_input_cleveland["restecg"] = restecg

    thalach = st.number_input("Max Heart Rate", min_value=60, max_value=250)
    user_input_cleveland["thalach"] = thalach

    exang_mapping = {"Yes": 1, "No": 0}

    exang = st.selectbox("Excercise induced angina", options=["Yes", "No"])
    user_input_cleveland["exang"] = exang

    oldpeak = st.number_input("ST depression induced by exercise", min_value=0, max_value=10)
    user_input_cleveland["oldpeak"] = oldpeak

    slope_mapping = {"Upsloping": 1, "Flat": 2, "Downsloping":3}

    slope = st.selectbox("Slope of Peak exercise ST", options=["Upsloping", "Flat", "Downsloping"])
    user_input_cleveland["slope"] = slope

    ca1_0_mapping = {"Yes": 1, "No": 0}

    ca1_0 = st.selectbox("1 Major Blood Vessel colored by Floroscopy", options=["Yes", "No"])
    user_input_cleveland["ca_1.0"] = ca1_0

    ca2_0_mapping = {"Yes": 1, "No": 0}

    ca2_0 = st.selectbox("2 Major Blood Vessel colored by Floroscopy", options=["Yes", "No"])
    user_input_cleveland["ca_2.0"] = ca2_0

    ca3_0_mapping = {"Yes": 1, "No": 0}

    ca3_0 = st.selectbox("3 Major Blood Vessel colored by Floroscopy", options=["Yes", "No"])
    user_input_cleveland["ca_3.0"] = ca3_0

    thal6_0_mapping = {"Yes": 1, "No": 0}

    thal6_0 = st.selectbox("Thallesemia Fixed defect", options=["Yes", "No"])
    user_input_cleveland["thal_6.0"] = thal6_0

    thal7_0_mapping = {"Yes": 1, "No": 0}

    thal7_0 = st.selectbox("Thallesemia Reversable defect", options=["Yes", "No"])
    user_input_cleveland["thal_7.0"] = thal7_0

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
        user_input_cleveland[key] = mapping[user_input_cleveland[key]]

    return user_input_cleveland

def get_brfss_input():

    user_input_brfss = {}

    mental_mapping = {"Zero-days when mental health not good": 1, "1-13days when mental health not good": 2,
                      "14\+ days when mental health not good": 3}

    mental_health = st.radio("Mental Health Status", options=["Zero-days when mental health not good", "1-13days when mental health not good", "14+ days when mental health not good"])
    user_input_brfss["Mental_health"] = mental_health

    gen_mapping = {"Good or Better Health": 1, "Fair or Poor": 0}

    general_health = st.radio("General Health Status", options=["Good or Better Health", "Fair or Poor"])
    user_input_brfss["General_health"] = general_health

    stroke_mapping = {"Yes": 1, "No": 0}

    stroke = st.radio("Ever Diagnosed with a Stroke", options=["Yes", "No"])
    user_input_brfss["Stroke"] = stroke

    copd_mapping = {"Yes": 1, "No": 0}

    copd = st.radio("Ever told you had C.O.P.D. emphysema or chronic bronchitis?", options=["Yes", "No"])
    user_input_brfss["COPD"] = copd

    kidney_mapping = {"Yes": 1, "No": 0}

    kidney_disease = st.radio("Ever told you have kidney disease?", options=["Yes", "No"])
    user_input_brfss["Kidney_disease"] = kidney_disease

    bp_mapping = {"Yes": 1, "No": 0}

    high_bp = st.radio(" Ever Told Blood Pressure High (above 80/120 mmHg?", options=["Yes", "No"])
    user_input_brfss["High_BP"] = high_bp

    chol_mapping = {"High (above 200mg/dL)": 1, "Normal(below 200mg/dL)": 0}

    high_chol = st.radio("Blood Cholestrol Level", options=["High (above 200mg/dL)", "Normal(below 200mg/dL)"])
    user_input_brfss["High_cholestrol"] = high_chol

    sex_mapping = {"Male": 1, "Female": 0}

    sex = st.radio("Sex", options=["Male", "Female"])
    user_input_brfss["Sex"] = sex

    age_mapping = {"18 to 24": 1, "25 to 34": 2, "35 to 44": 3, "45 to 54": 4, "55 to 64": 5, "65 or older": 6}
    age_group = st.radio("Age Group", options=["18 to 24", "25 to 34", "35 to 44", "45 to 54",
                                               "55 to 64", "65 or older"])
    user_input_brfss["Age_group"] = age_group

    hiv_mapping = {"Yes": 1, "No": 0}
    hiv_group = st.radio(" Ever tested HIV", options=["Yes", "No"])
    user_input_brfss["HIV"] = hiv_group

    income_mapping = {"Less than $15000": 1, "$15000 to $25000": 2, "$25000 to $35000": 3,
                      "$35000 to $50000": 4, "$50000 to $100000": 5, "$100000 to $200000": 6,
                      "$200 000 or more": 7}
    income_group = st.radio("What is your Income Level", options=["Less than $15000", "$15000 to $25000",
                                                                  "$25000 to $35000", "$35000 to $50000",
                                                                  "$50000 to $100000", "$100000 to $200000",
                                                                  "$200000 or more"])
    user_input_brfss["Income_level"] = income_group

    education_mapping = {"Did not graduate High School": 1, "Graduated High School": 2, "Attended College or Technical School": 3,
                         "Graduated from college or Technical School": 4}
    education_group = st.radio("Education Level", options=["Did not graduate High School", "Graduated High School",
                                                           "Attended College or Technical School",
                                                           "Graduated from college or Technical School"])
    user_input_brfss["Education_level"] = education_group

    fruit = st.number_input("Daily Fruit Intake", min_value=0, max_value=9900)
    user_input_brfss["Fruit_intake"] = fruit

    vege = st.number_input("Daily Green Vegetables Intake", min_value=0, max_value=9900)
    user_input_brfss["Green_intake"] = vege

    potato = st.number_input("Daily Potato Servings", min_value=0, max_value=9900)
    user_input_brfss["Potato_servings"] = potato

    mappings = {
        "Mental_health": mental_mapping,
        "General_health": gen_mapping,
        "Stroke": stroke_mapping,
        "COPD": copd_mapping,
        "Kidney_disease": kidney_mapping,
        "High_BP": bp_mapping,
        "High_cholestrol": chol_mapping,
        "Sex": sex_mapping,
        "Age_group": age_mapping,
        "HIV": hiv_mapping,
        "Income_level": income_mapping,
        "Education_level": education_mapping
    }

    for key, mapping in mappings.items():
        user_input_brfss[key] = mapping[user_input_brfss[key]]

    return user_input_brfss

def predict(features, model):
    df = pd.DataFrame([features])
    return model.predict(df)[0]


def main():
    st.title("Heart Disease Prediction")

    dataset_choice = st.selectbox("Choose a dataset:", ["Behavioural Factors (BRFSS)","UCI Heart Disease"])

    st.write("Please answer below questions regarding you health data results")

    if dataset_choice == "Behavioural Factors (BRFSS)":
        user_data = get_brfss_input()
        model = brfss_model
    else:
        user_data = get_cleveland_input()
        model = cleveland_model

    st.write("Summary of the details you provided:")
    st.write(user_data)

    if st.button("Predict"):
        prediction_prob = predict(user_data, model)

        if prediction_prob > 0.5:
            display_string = f"You have a {prediction_prob *100}% chance of heart disease"

        else:
            display_string = "Based on your health lifestyle it is not likely that you have a heart disease"

        st.text_input("Prediction Result", value=display_string, disabled=True)


        # if prediction == 1:
        #     display_string = "Likely Risk of Heart Disease"
        # else:
        #     display_string = "It is unlikely that you have heart disease"
        #
        # st.text_input("Prediction Result", value=display_string, disabled=True)

        if prediction_prob > 0.5:
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
