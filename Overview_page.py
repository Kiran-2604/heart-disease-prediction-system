import streamlit as st

st.title(" Project Overview")
st.header("About the Project")

st.write("""
The Heart Disease Prediction System is a Machine Learning project developed
to predict whether a patient is at risk of heart disease.
The model uses medical attributes such as:
- Age
- Sex
- Chest Pain Type
- Cholesterol
- Blood Pressure
- Maximum Heart Rate
- ECG Results
- Exercise Angina
- Oldpeak
- ST Slope
""")

st.header("Objective")
st.write("""
The objective of this project is to:
- Analyze heart disease data
- Identify important medical factors
- Build predictive machine learning models
- Provide quick disease prediction
""")

st.header("Machine Learning Workflow")
st.markdown("""
1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Model Training
6. Model Evaluation
7. Deployment using Streamlit
""")

st.header("Algorithms Used")

st.write("""
- Logistic Regression
- Random Forest
- Decision Tree
- Support Vector Machine
""")

st.header("Tools & Technologies")
st.write("""
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
""")
