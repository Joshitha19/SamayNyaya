import streamlit as st

def show_signup():

    st.markdown("""
    <style>

    /* Same Background */
    .stApp {
        background-color: #EFDFBB;
    }

    /* Center card */
    .signup-container {
        display: flex;
        justify-content: center;
        margin-top: 130px;
    }

    .signup-card {
        background-color: #DAC1B1;
        padding: 45px;
        border-radius: 12px;
        width: 420px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.15);
    }

    .signup-title {
        text-align: center;
        font-size: 32px;
        font-weight: 600;
        color: #722F37;
        margin-bottom: 30px;
    }

    /* Input styling */
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

    st.markdown('<div class="signup-container"><div class="signup-card">', unsafe_allow_html=True)

    st.markdown('<div class="signup-title">Create Account</div>', unsafe_allow_html=True)

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm = st.text_input("Confirm Password", type="password")

    if st.button("Register"):
        if password != confirm:
            st.error("Passwords do not match")
        elif name and email and password:
            st.success("Account created. Please login.")
        else:
            st.warning("Fill all fields")

    st.markdown('</div></div>', unsafe_allow_html=True)
