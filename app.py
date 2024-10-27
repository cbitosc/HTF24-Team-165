import streamlit as st
import pandas as pd
from diagnosis_system import suggest_diagnoses
from research_integration import fetch_latest_research

# Set page configuration
st.set_page_config(page_title="AI Diagnostic System", layout="wide")

# Custom CSS for additional styling with light blue background
st.markdown("""
<style>
    body {
        background-color: #e3f2fd;  /* Light blue background */
        height: 100vh;  /* Full height for the gradient */
        margin: 0;  /* Remove default margin */
    }
    .main {
        background-color: rgba(255, 255, 255, 0.9);  /* White background for main content with slight transparency */
        border-radius: 10px;  /* Rounded corners */
        padding: 20px;  /* Padding around main content */
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);  /* Subtle shadow */
    }
    h1 {
        color: black;  /* Welcome message color */
        text-align: center;  /* Center align title */
        font-size: 3em;  /* Increased font size for welcome message */
        margin: 20px 0;  /* Space above and below the title */
        padding: 10px;  /* Padding around the title */
    }
    h2 {
        color: #003366;  /* Dark blue color for main heading */
        font-size: 2.5em;  /* Increased font size for main heading */
        text-align: center;  /* Center align subtitle */
    }
    p, li {
        font-size: 1.5em;  /* Increased font size for paragraphs and list items */
    }
    .stButton>button {
        background-color: #007bff;  /* Button color */
        color: white;  /* Button text color */
    }
    .stTextInput>div>input {
        border-radius: 5px;  /* Rounded corners for text input */
    }
    .sidebar .sidebar-content {
        background-color: rgba(255, 255, 255, 0.8);  /* Light sidebar background with slight transparency */
        border-radius: 10px;  /* Rounded corners for sidebar */
    }
    hr {
        margin: 40px 0;  /* Space above and below the horizontal line */
        border: 1px solid #007bff;  /* Blue color for horizontal line */
    }
    .thank-you {
        font-size: 1.8em;  /* Increase font size for thanking note */
        text-align: center;  /* Center align thank you message */
        color: black;  /* Color for thank you message */
        margin-top: 40px;  /* Space above the thank you message */
    }
</style>
""", unsafe_allow_html=True)

# Welcome message
st.markdown("<h1>Hey user ....WELCOME! 🎉</h1>", unsafe_allow_html=True)

# Title and description
st.markdown("<h2>🩺 AI-POWERED DIAGNOSTIC  AND TREATMENT SUPPORT   SYSTEM FOR MEDICAL  PROFESSIONALS</h2>", unsafe_allow_html=True)
st.write("Enter your symptoms to receive suggested diagnoses and treatment plans.")

# Sidebar for symptom selection
st.sidebar.header("Select Symptoms")
expanded_symptom_options = [
    'fever', 'cough', 'headache', 'fatigue', 'sore throat', 
    'chills', 'nausea', 'vomiting', 'diarrhea', 'muscle pain', 
    'shortness of breath', 'loss of taste', 'loss of smell', 
    'skin rash', 'joint pain', 'sweating'
]

selected_symptoms = st.sidebar.multiselect("Choose symptoms:", expanded_symptom_options)
additional_symptoms = st.sidebar.text_input("Add any additional symptoms (comma-separated):")

# Combine selected symptoms with additional inputs
symptoms_input = ", ".join(selected_symptoms + [symptom.strip() for symptom in additional_symptoms.split(',') if symptom.strip()]) if additional_symptoms else ", ".join(selected_symptoms)

# Show diagnosis and treatment only if symptoms are provided
if symptoms_input:
    # Get diagnosis suggestions and treatments
    results = suggest_diagnoses(symptoms_input)

    # Display each suggested diagnosis with urgency, treatment, and research
    for _, row in results.iterrows():
        st.subheader(f"Diagnosis: {row['Diagnosis']}")
        st.write(f"**Treatment**: {row['Treatment']}")
        st.write(f"**Urgency Level**: {row['Urgency']}")

        # Fetch recent research articles
        research_articles = fetch_latest_research(row['Diagnosis'])
        st.write("**Latest Research Articles**:")
        for article in research_articles:
            st.write(f"- [{article['title']}]({article['link']})")

    # Horizontal line after entering symptoms
    st.markdown("<hr>", unsafe_allow_html=True)

# Feedback section
st.sidebar.header("Feedback")
feedback = st.sidebar.text_area("We value your feedback! Please share your thoughts:")
if st.sidebar.button("Submit Feedback"):
    st.sidebar.success("Thank you for your feedback!")

# Thanking note at the bottom
st.markdown("<div class='thank-you'>Thank you for using our AI Diagnostic System! We hope you find it helpful. 😊</div>", unsafe_allow_html=True)

# Add a small image below the thanking note
st.image(r"C:\Users\dell\Documents\CBIT[4]\CBIT\doctor.jpg", width=320)  # Set width to 200 pixels for a smaller image