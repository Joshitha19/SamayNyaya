import streamlit as st

def show_judge_assistant():
    st.title("Policy Simulator")

    slider = st.slider("Shift % Civil Cases to Mediation", 0, 50, 10)

    reduction = slider * 0.5

    st.metric("Estimated Backlog Reduction (%)", reduction)
    st.progress(int(reduction))
