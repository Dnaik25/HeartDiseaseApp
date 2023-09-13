import streamlit as st

background_image_css = """
<style>
body {
    background-image: url("HeartBCG.jpeg");
    background-size: cover;
}
</style>
"""

# Set the background image using custom CSS
st.markdown(background_image_css, unsafe_allow_html=True)

# Page title
st.title("BMI Calculator")

# Sidebar for user input
st.sidebar.header("User Input")
height = st.sidebar.slider("Enter your height (in cm)", 100.0, 250.0, 170.0)
weight = st.sidebar.slider("Enter your weight (in kg)", 30.0, 200.0, 70.0)

# Calculate BMI
bmi = weight / ((height / 100) ** 2)

# Determine health classification
health_status = ""
if bmi < 18.5:
    health_status = "Underweight"
elif 18.5 <= bmi < 24.9:
    health_status = "Normal Weight"
elif 25 <= bmi < 29.9:
    health_status = "Overweight"
else:
    health_status = "Obese"

# Display results
st.write("## BMI Calculation Results")
st.write(f"**Height:** {height} cm")
st.write(f"**Weight:** {weight} kg")
st.write(f"**BMI:** {bmi:.2f}")
st.write(f"**Health Classification:** {health_status}")

# Provide health recommendations
st.write("## Health Recommendations")
if health_status == "Underweight":
    st.write("You may want to consider increasing your calorie intake and consulting a healthcare professional.")
elif health_status == "Normal Weight":
    st.write("Maintaining a healthy weight is important. Keep up the good work!")
elif health_status == "Overweight":
    st.write("Consider making dietary and lifestyle changes to reach a healthier weight.")
else:
    st.write("Obesity can lead to various health issues. Consult a healthcare professional for guidance.")

# Disclaimer
st.write("## Disclaimer")
st.write("This BMI calculator is for informational purposes only and should not replace professional medical advice.")
