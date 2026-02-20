import streamlit as st

def show_case_management():
    st.title("Case Management")

    st.subheader("Enter Case Details")

    col1, col2 = st.columns(2)

    with col1:
        case_type = st.selectbox("Case Type", ["Civil", "Criminal", "Commercial"])
        parties = st.number_input("Number of Parties", 1, 20)
        adj = st.number_input("Adjournments", 0, 50)
        evidence = st.number_input("Evidence Count", 0, 100)

    with col2:
        lawyer = st.number_input("Lawyer Count", 0, 10)
        prior = st.number_input("Prior Delays", 0, 10)
        year = st.number_input("Filing Year", 2015, 2025)
        complexity = st.selectbox("Complexity", ["Low", "Medium", "High"])

    st.button("Analyze Case")
