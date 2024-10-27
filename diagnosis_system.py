from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pandas as pd

# Sample data with diagnoses, symptoms, treatments, and urgency levels
data = {
    'Symptoms': [
        'fever, cough', 
        'fever, headache', 
        'sore throat, fever', 
        'cough, fatigue', 
        'fever, chills',
        'nausea, vomiting', 
        'diarrhea, fatigue', 
        'muscle pain, fever', 
        'shortness of breath, cough', 
        'loss of taste, fever'
    ],
    'Diagnosis': [
        'Flu', 
        'Migraine', 
        'Strep Throat', 
        'Common Cold', 
        'Malaria',
        'Gastroenteritis', 
        'COVID-19', 
        'Dengue Fever', 
        'Pneumonia', 
        'COVID-19'
    ],
    'Treatment': [
        'Rest and hydration',
        'Pain relievers and rest in a dark room',
        'Antibiotics as prescribed by a doctor',
        'Rest, fluids, and over-the-counter cough medicine',
        'Antimalarial drugs and doctor consultation',
        'Hydration and rest, possibly antiemetics',
        'Isolation and supportive care',
        'Hydration and pain relief',
        'Antibiotics and hospitalization if severe',
        'Isolation and supportive care'
    ],
    'Urgency': [
        'Moderate', 
        'Low', 
        'High', 
        'Moderate', 
        'High',
        'Moderate', 
        'High', 
        'Moderate', 
        'High', 
        'High'
    ]
}

# Load data into a DataFrame
df = pd.DataFrame(data)

# Initialize the vectorizer and model
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['Symptoms'])
y = df['Diagnosis']

# Train a model to suggest diagnoses
model = LogisticRegression()
model.fit(X, y)

def suggest_diagnoses(symptoms_input):
    """
    Suggest diagnoses based on symptoms input.
    Returns a DataFrame containing possible conditions with treatment and urgency information.
    """
    input_vector = vectorizer.transform([symptoms_input])
    similarities = model.decision_function(input_vector)
    top_indices = similarities.argsort()[0][-3:][::-1]  # Get indices of top 3 closest diagnoses
    
    # Get diagnosis, treatment, and urgency for each result
    results = df.iloc[top_indices][['Diagnosis', 'Treatment', 'Urgency']]
    return results
