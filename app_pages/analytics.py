import streamlit as st
import pandas as pd

def show_analytics():
    st.title("Analytics")

    delay_data = pd.DataFrame({
        "Delay": ["Yes", "No"],
        "Cases": [1320, 4680]
    })

    st.subheader("Delay Distribution")
    st.bar_chart(delay_data.set_index("Delay"))
