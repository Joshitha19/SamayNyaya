import streamlit as st

def show_scheduling():
    st.title("Scheduling & Judge Allocation")

    judge_data = {
        "Justice Sharma": 120,
        "Justice Patel": 80,
        "Justice Kumar": 200,
        "Justice Singh": 95
    }

    st.bar_chart(judge_data)

    st.success("Recommended Judge: Justice Patel")
