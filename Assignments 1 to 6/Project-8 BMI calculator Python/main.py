import streamlit as st
import time

# Set page configuration
st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")

# Custom CSS for styling and animations
st.markdown(
    """
    <style>
        body {
            background-color: #d1f7c4;
            color: #333;
        }
        .stApp {
            background-color: #b2ebf2;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 2px 2px 20px rgba(0, 0, 0, 0.1);
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        .bmi-result {
            animation: fadeIn 1.5s ease-in-out;
            font-size: 24px;
            font-weight: bold;
            color: #1e88e5;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("💪 BMI Calculator")
st.markdown("""
## Calculate your Body Mass Index (BMI)
Enter your **Weight and Height** below:
""")

col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("Weight (in kg)", min_value=1.0, format="%.2f")
with col2:
    height = st.number_input("Height (in meters)", min_value=0.5, format="%.2f")

if height > 0 and weight > 0:
    with st.spinner("Calculating BMI..."):
        time.sleep(1)  # Simulating loading time
        bmi = weight / (height ** 2)
        
    st.subheader("Your BMI is:")
    st.markdown(f'<div class="bmi-result">{bmi:.2f}</div>', unsafe_allow_html=True)
    
    if bmi < 18.5:
        st.error("You are underweight")
    elif 18.5 <= bmi < 24.9:
        st.success("You have a normal weight")
    elif 25 <= bmi < 29.9:
        st.warning("You are overweight")
    else:
        st.error("You are obese")
else:
    st.warning("⚠️ Please enter valid height and weight")

# Footer  
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 14px; color: #555;">You are stronger than you think. Keep striving for a healthier you! 🌟</p>', unsafe_allow_html=True)
st.write("Created by **Harmain Bashir**")          
