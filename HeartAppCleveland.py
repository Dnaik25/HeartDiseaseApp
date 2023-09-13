import streamlit as st
import pandas as pd
import pickle

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

# Load pre-trained models (replace with your actual models)
with open("HeartDiseaseCleveland.pkl", "rb") as f:
    cleveland_model = pickle.load(f)


# Dataset Features (Replace with your actual dataset features)
CLEVELAND_FEATURES = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
       'exang', 'oldpeak', 'slope', 'ca_1.0', 'ca_2.0',
       'ca_3.0', 'thal_6.0', 'thal_7.0']

def get_features(dataset_choice):
    if dataset_choice == "UCI Heart Disease":
        return {feature: st.slider(feature, 0, 100) for feature in CLEVELAND_FEATURES}

def predict(features, model):
    df = pd.DataFrame([features])
    return model.predict(df)[0]


def main():
    st.title("Heart Disease Prediction")

    dataset_choice = st.selectbox("Choose a dataset:", ["UCI Heart Disease"])
    features = get_features(dataset_choice)

    if st.button("Predict"):
        if dataset_choice == "UCI Heart Disease":
            prediction = predict(features, cleveland_model)

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


if __name__ == "__main__":
    main()
