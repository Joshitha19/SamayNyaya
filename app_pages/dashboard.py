import streamlit as st
import pandas as pd

def show_dashboard():
    st.markdown('<div class="main-title">Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Overview of judicial workflow metrics</div>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Cases", "6,000")
    col2.metric("Active Cases", "4,280")
    col3.metric("High Risk Cases", "1,320")
    col4.metric("Completed Cases", "400")

    st.divider()

    colA, colB = st.columns(2)

    with colA:
        st.subheader("Case Completion Trend")

        data = pd.DataFrame({
            "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
            "Cases": [120, 190, 150, 220, 180, 250]
        })

        st.bar_chart(data.set_index("Month"))

    with colB:
        st.subheader("Judge Workload Distribution")

        judge_data = pd.DataFrame({
            "Judge": ["Justice Sharma", "Justice Patel", "Justice Kumar", "Justice Singh"],
            "Cases": [120, 80, 200, 95]
        })

        st.bar_chart(judge_data.set_index("Judge"))
