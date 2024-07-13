import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np

def model():
    if 'model' not in st.session_state:
        data = pd.read_csv("loan ass.csv", index_col=0, usecols=lambda x: x not in ['NumCreditLines', 'DTIRatio'])
        data.columns = data.columns.astype(str)
        # Convert columns with non-numeric values to numeric
        for col in data.columns:
            if data[col].dtype == 'object':
                data[col] = data[col].astype('category').cat.codes
        x = data.drop(columns=["Default"])
        y = data["Default"]
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
        model = LogisticRegression(max_iter=1000)
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)

        accuracy = accuracy_score(y_test, y_pred) * 100
        accuracy = round(accuracy, 2)
        st.session_state.accuracy = accuracy
        st.session_state.model = model

    return st.session_state.model
def page1():
    st.title("Loan Default System")
    load_data = model()
    st.write("The model is trained on this dataset: ", "https://www.kaggle.com/datasets/nikhil1e9/loan-default/data")
    st.write("Model Accuracy: ", st.session_state.accuracy)
    age = st.slider("Age", 18, 60)
    income = st.text_input("Annual Income (RM)", 0)
    loan_amount = st.number_input("Loan Amount (RM)", 0)
    credit_score = st.number_input("Credit Score", 300, 850)
    months_employed = st.number_input("Months Employed", 0)
    loan_term = st.selectbox("Loan Term (months)", ["12", "24", "36", "48", "60"])
    interest_rate = st.number_input("Interest Rate for the loan")
    education = st.selectbox("Education", ["High School", "Bachelor's", "Master's", "PhD"])
    employment_type = st.selectbox("Employment Type", ["Full-time", "Part-Time", "Self-Employed", "Unemployed"])
    marital_status = st.selectbox("Marital Status", ["Married", "Single", "Divorced"])
    mortgage = st.selectbox("Mortgage", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["Yes", "No"])
    cosigner = st.selectbox("Cosigner", ["Yes", "No"])
    loan_purpose = st.selectbox("Loan Purpose", ["Business", "Auto", "Education", "Home", "Other (Eg: Personal Loan)"])

    education_code = ["High School", "Bachelor's", "Master's", "PhD"].index(education)
    employment_type_code = ["Full-time", "Part-Time", "Self-Employed", "Unemployed"].index(employment_type)
    marital_status_code = ["Married", "Single", "Divorced"].index(marital_status)
    mortgage_code = ["Yes", "No"].index(mortgage)
    dependents_code = ["Yes", "No"].index(dependents)
    cosigner_code = ["Yes", "No"].index(cosigner)
    loan_purpose_code = ["Business", "Auto", "Education", "Home", "Other"].index(loan_purpose)
    

    if st.button("Submit"):
        prediction = load_data.predict(np.array([[age, income, loan_amount, credit_score, months_employed, interest_rate, loan_term, education_code, employment_type_code, marital_status_code, mortgage_code, dependents_code, cosigner_code, loan_purpose_code]], dtype=np.float32))[0]
        st.session_state.page = "page2"
        st.session_state.age = age
        st.session_state.income = float(income)
        st.session_state.loan_amount = float(loan_amount)
        st.session_state.credit_score = float(credit_score)
        st.session_state.months_employed = float(months_employed)
        st.session_state.interest_rate = float(interest_rate)
        st.session_state.loan_term = float(loan_term)
        st.session_state.education = education_code
        st.session_state.employment_type = employment_type_code
        st.session_state.marital_status = marital_status_code
        st.session_state.mortgage = mortgage_code
        st.session_state.dependents = dependents_code
        st.session_state.cosigner = cosigner_code
        st.session_state.loan_purpose = loan_purpose_code
        st.session_state.prediction = prediction
        st.experimental_rerun()
