import streamlit as st
import numpy as np

def page2():
    st.title("Loan Default System")
    st.subheader("Result: ")
    with st.expander("Loan Details", expanded=False):
        age = st.session_state.age
        income = st.session_state.income
        loan_amount = st.session_state.loan_amount
        credit_score = st.session_state.credit_score
        months_employed = st.session_state.months_employed
        interest_rate = st.session_state.interest_rate
        loan_term = st.session_state.loan_term
        education_code = st.session_state.education
        employment_type_code = st.session_state.employment_type
        marital_status_code = st.session_state.marital_status
        mortgage_code = st.session_state.mortgage
        dependents_code = st.session_state.dependents
        cosigner_code = st.session_state.cosigner
        loan_purpose_code = st.session_state.loan_purpose
        prediction = st.session_state.prediction

        education = ["High School", "Bachelor's", "Master's", "PhD"][education_code]
        employment_type = ["Full-time", "Part-Time", "Self-Employed", "Unemployed"][employment_type_code]
        marital_status = ["Married", "Single", "Divorced"][marital_status_code]
        mortgage = ["Yes", "No"][mortgage_code]
        dependents = ["Yes", "No"][dependents_code]
        cosigner = ["Yes", "No"][cosigner_code]
        loan_purpose = ["Business", "Auto", "Education", "Home", "Other"][loan_purpose_code]

        st.write("Age: ", age)
        st.write("Annual Income (RM): ", income)
        st.write("Loan Amount (RM): ", loan_amount)
        st.write("Credit Score: ", credit_score)
        st.write("Months Employed: ", months_employed)
        st.write("Interest Rate: ", interest_rate)
        st.write("Loan Term (months): ", loan_term)
        st.write("Education: ", education)
        st.write("Employment Type: ", employment_type)
        st.write("Marital Status: ", marital_status)
        st.write("Mortgage: ", mortgage)
        st.write("Dependents: ", dependents)
        st.write("Cosigner: ", cosigner)
        st.write("Loan Purpose: ", loan_purpose)

    if isinstance(prediction, (list, np.ndarray)):
        if len(prediction) > 0:
            if prediction[0] == 0:
                st.write("Result: The loan is not default")
            else:
                st.write("Result: The loan is default")
        else:
            st.write()
            st.write("Invalid Prediction")
    else:
        if prediction == 0:
            st.subheader("The loan is not default")
        else:
            st.subheader("The loan is default")
    st.text("Thank you!")

    if st.button("Back"):
        st.session_state.page = "page1"
        st.experimental_rerun()

    if st.button("Done"):
        st.session_state.page = "main"
        st.experimental_rerun()

