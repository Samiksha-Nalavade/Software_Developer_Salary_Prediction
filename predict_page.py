
# This file is used to display the prediction page which allows users to predict a salary based on country of residence,
# education level, and years of experience.

import streamlit as st
import pickle
import numpy as np


# Function to retrieve the pickle file (saved_steps.pkl) from Jupyter Notebook file titled 'salary_prediction.ipynb'.
def load_model():
    with open('c:\MiniProject\saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

# Load data.
data = load_model()

regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]


# Function populates the prediction parameters in the prediction page using Streamlit.
def show_predict_page():
    st.title("Software Developer Salary Prediction")

    st.write("""### We need some information to predict the salary""")

    # Countries that user can pick from. 14
    countries = (
        "United States",
        "India",
        "United Kingdom",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
    )

    education = (
        "Less than a Bachelors",
        "BTech",
        "BA",
        "BSC",
        "Master's degree "
        
    )

   
    

    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", education)
    

    expericence = st.slider("Years of Experience", 0, 50, 3)

    # Button that when clicked, takes all user input, and uses the Decision tree regression algorithm to predict a salary.
    ok = st.button("Calculate Salary")
    if ok:
        X = np.array([[country, education, expericence ]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
       
        X = X.astype(float)

        salary = regressor.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")