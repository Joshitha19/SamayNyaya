import streamlit as st

# ✅ MUST BE FIRST STREAMLIT COMMAND
st.set_page_config(page_title="SamayNyaya", layout="wide")

# THEN imports
from app_pages.home import show_home
from app_pages.login import show_login
from app_pages.signup import show_signup
from app_pages.dashboard import show_dashboard
from app_pages.analytics import show_analytics
from app_pages.case_management import show_case_management
from app_pages.judge_assistant import show_judge_assistant
from app_pages.scheduling import show_scheduling


# Session states
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------------- NOT LOGGED IN ----------------
if not st.session_state.logged_in:

    if st.session_state.page == "home":
        show_home()

    elif st.session_state.page == "login":
        show_login()

    elif st.session_state.page == "signup":
        show_signup()

# ---------------- AFTER LOGIN ----------------
else:
    st.sidebar.title("⚖️ SamayNyaya")
    page = st.sidebar.radio(
        "Navigate",
        ["Dashboard", "Case Management", "Scheduling", "Analytics", "Judge Assistant"]
    )

    if page == "Dashboard":
        show_dashboard()

    elif page == "Case Management":
        show_case_management()

    elif page == "Scheduling":
        show_scheduling()

    elif page == "Analytics":
        show_analytics()

    elif page == "Judge Assistant":
        show_judge_assistant()

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.page = "home"
        st.rerun()
