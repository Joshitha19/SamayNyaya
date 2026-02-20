import streamlit as st
import pandas as pd

def show_home():

    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
    }

    .stApp {
        background-color: #DAC1B1;  /* Silk */
    }

    .top-nav {
        position: absolute;
        top: 10px;
        right: 80px;
        font-size: 18px;
        color: #3D0A05; /* Dark Red */
        font-weight: 500;
    }

    .top-nav span {
        margin-left: 60px;
        cursor: pointer;
        transition: 0.3s;
    }

    .top-nav span:hover {
        color: #7F1F0E; /* Ruby Red */
    }

    .main-container {
        text-align: center;
        margin-top: 120px;
    }

    .title {
        font-size: 72px;
        font-weight: 700;
        color: #3D0A05; /* Dark Red */
        margin-bottom: 20px;
    }

    .tagline {
        font-size: 22px;
        color: #3D0A05;
        margin-bottom: 70px;
    }

    div.stButton > button {
        background-color: #AC746C; /* Indian Red */
        color: white;
        width: 220px;
        height: 55px;
        font-size: 18px;
        border-radius: 8px;
        border: none;
        font-weight: 500;
    }

    div.stButton > button:hover {
        background-color: #7F1F0E; /* Ruby Red */
        color: white;
    }

    .section-card {
        background-color: #A58570; /* Grey Beige */
        padding: 40px;
        border-radius: 20px;
        margin-bottom: 50px;
    }

    h3 {
        color: #3D0A05;
    }

    </style>
    """, unsafe_allow_html=True)

    # ---------------- NAV ---------------- #

    st.markdown("""
        <div class="top-nav">
            <span>Dashboard</span>
            <span>Analytics</span>
            <span>Scheduling</span>
        </div>
    """, unsafe_allow_html=True)

    # ---------------- HERO ---------------- #

    st.markdown("""
        <div class="main-container">
            <div class="title">⚖️ SamayNyaya</div>
            <div class="tagline">
                Ensuring Justice Without Delay. AI-powered intelligent judicial workflow platform.
            </div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,1,1])

    with col2:
        sub1, sub2 = st.columns(2)
        if sub1.button("Sign In"):
            st.session_state.page = "login"
            st.rerun()
        if sub2.button("Sign Up"):
            st.session_state.page = "signup"
            st.rerun()

    st.markdown("<br><br>", unsafe_allow_html=True)

    # ---------------- DASHBOARD TITLE ---------------- #

    st.markdown("""
        <div style='text-align:center; font-size:42px; font-weight:700; 
                    color:#3D0A05; margin-bottom:50px;'>
            📊 Judicial Intelligence Dashboard
        </div>
    """, unsafe_allow_html=True)

    # ---------------- DATA ---------------- #

    total_civil = 11141266
    total_criminal = 37338483
    total_cases = 48479749
    pre_litigation = 1297653

    civil_gt_1yr = 7892074
    criminal_gt_1yr = 27351361

    # ---------------- OVERALL STATS ---------------- #

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 📌 Overall Case Statistics")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("⚖️ Civil Cases", f"{total_civil:,}", "↑ 2.1%")
    col2.metric("🚔 Criminal Cases", f"{total_criminal:,}", "↑ 1.4%")
    col3.metric("📊 Total Cases", f"{total_cases:,}")
    col4.metric("📝 Pre-Litigation", f"{pre_litigation:,}")

    st.markdown("</div>", unsafe_allow_html=True)

    # ---------------- AGE ANALYTICS ---------------- #

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### ⏳ Cases Older Than 1 Year")

    col5, col6 = st.columns(2)

    with col5:
        st.metric("Civil > 1 Year", f"{civil_gt_1yr:,}", "70.8%")
        st.progress(0.708)

    with col6:
        st.metric("Criminal > 1 Year", f"{criminal_gt_1yr:,}", "73.2%")
        st.progress(0.732)

    st.markdown("</div>", unsafe_allow_html=True)

    # ---------------- AGE-WISE ---------------- #

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 📈 Age-wise Pending Cases")

    data = pd.DataFrame({
        "Age Group": ["<1 Year", "1-3 Years", "3-5 Years", "5-10 Years", ">10 Years"],
        "Civil (%)": [25, 25, 23, 20, 7],
        "Criminal (%)": [75, 75, 77, 80, 93]
    })

    st.bar_chart(data.set_index("Age Group"))

    st.markdown("</div>", unsafe_allow_html=True)

