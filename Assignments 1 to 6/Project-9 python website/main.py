import streamlit as st
import pandas as pd
import random

# Set page configuration
st.set_page_config(page_title="Student Data Generator", layout="wide")

# Custom CSS for background color
st.markdown(
    """
    <style>
        body {
            background-color: #f0f2f6;
        }
        .stApp {
            background-color: #e3f2fd;
            padding: 20px;
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Student CSV File Generator")

names = ['Harmain', 'Ayra', 'Ahmed', 'Orhan', 'Azmeer', 'Almeer', 'Fatima', 'Essa', 'Ali', 'Shahmeer', 'Azlan', 'Sarina', 'Dawood', 'Mustafa', 'Elaf', 'Ayzal', 'Daneen', 'Behram', 'Ayesha', 'Alyana']

students = []

for i in range(1, 21):  # Corrected loop range
    student = {
        "ID": i,
        "Name": random.choice(names),
        "Age": random.randint(18, 25),
        "Grade": random.choice(['A', 'B', 'C', 'D', 'E', 'F']),
        "Marks": random.randint(40, 100)
       
    }
    students.append(student)

# Create DataFrame
df = pd.DataFrame(students)

# Display DataFrame
st.subheader("Generated Students Data")
st.dataframe(df)

# Convert DataFrame to CSV
csv_file = df.to_csv(index=False).encode('utf-8')

# Download Button
st.download_button(
    label="Download CSV File",
    data=csv_file,
    file_name="students.csv",
    mime="text/csv"
)

st.success("Students Record Generated Successfully!")
