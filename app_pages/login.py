import streamlit as st

def show_login():

    st.markdown("""
    <style>

    /* Background same as home */
    .stApp {
        background-color: #EFDFBB;
    }

    /* Center card */
    .login-container {
        display: flex;
        justify-content: center;
        margin-top: 140px;
    }

    .login-card {
        background-color: #DAC1B1;
        padding: 45px;
        border-radius: 12px;
        width: 420px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.15);
    }

    .login-title {
        text-align: center;
        font-size: 32px;
        font-weight: 600;
        color: #722F37;
        margin-bottom: 30px;
    }

    /* Inputs */
    .stTextInput > div > div > input {
        border-radius: 6px;
        border: 1px solid #A58570;
        height: 42px;
    }

    /* Button styling */
    div.stButton > button {
        background-color: #AC746C;
        color: white;
        width: 100%;
        height: 48px;
        font-size: 16px;
        border-radius: 6px;
        border: none;
        font-weight: 500;
        margin-top: 15px;
        transition: all 0.2s ease-in-out;
    }

    div.stButton > button:hover {
        background-color: #7F1F0E;
        color: white;
        transform: translateY(-2px);
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="login-container"><div class="login-card">', unsafe_allow_html=True)

    st.markdown('<div class="login-title">Sign In</div>', unsafe_allow_html=True)

    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if name and email and password:
            st.session_state.logged_in = True
            st.session_state.user = name
            st.rerun()
        else:
            st.warning("Fill all fields")

    st.markdown('</div></div>', unsafe_allow_html=True)
