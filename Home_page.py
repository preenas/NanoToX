import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

st.set_page_config(
    page_title="NanoToX",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed"
)
# 🔥 ADD IT HERE
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
[data-testid="stToolbar"] {display: none;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

BASE_DIR = os.path.dirname(__file__)

logo_path = os.path.join(BASE_DIR, "nanotox1-logo.png")
title_path = os.path.join(BASE_DIR, "title1.png")

logo = Image.open(logo_path)
title_img = Image.open(title_path)

# ================= HEADER ================= #
col1, col2, col3, col4 = st.columns([0.5, 1, 2.5, 1])

with col2:
    st.image(logo, width=220)

with col3:
    st.image(title_img, width=800)

with col4:
    nav1, nav2, nav3 = st.columns(3)

    with nav1:
        st.page_link("pages/login.py", label="Login")

    with nav2:
        st.page_link("pages/about.py", label="About")

    with nav3:
        st.page_link("pages/docs.py", label="Docs")

st.divider()

# ================= BUTTON STYLE ================= #
st.markdown("""
<style>
div[data-testid="stButton"] > button {
    height: 120px !important;
    font-size: 30px !important;
    font-weight: 700 !important;
    border-radius: 18px !important;
    border: none !important;
    background-color: #f2f4f8 !important;
    color: #333 !important;
}
div[data-testid="stButton"] > button:hover {
    background-color: #0078d4 !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# ================= MAIN BUTTONS ================= #
left, col1, col2, col3, right = st.columns([1, 2, 2, 2, 1])

with col1:
    if st.button("🚀\n\nTry Prediction", use_container_width=True):
        st.switch_page("pages/app.py")

with col2:
    if st.button("📊\n\nView Dashboard", use_container_width=True):
        st.switch_page("pages/dashboard.py")

with col3:
    if st.button("ℹ️\n\nLearn More", use_container_width=True):
        st.switch_page("pages/learn.py")

# ================= HOW IT WORKS ================= #
components.html("""
<div style="background:white;padding:3rem;border-radius:12px;
max-width:1000px;margin:80px auto;box-shadow:0 3px 12px rgba(0,0,0,0.08);
font-family:Segoe UI;">
<h2 style="text-align:center;">How It Works</h2>

<div style="display:flex;justify-content:space-between;gap:40px;margin-top:30px;">
<div style="flex:1;text-align:center;">
<h3>📂 Upload Data</h3>
<p>Submit nanoparticle datasets for AI-driven toxicity analysis.</p>
</div>

<div style="flex:1;text-align:center;">
<h3>🤖 AI Analysis</h3>
<p>Advanced ML models predict toxicity risks with high accuracy.</p>
</div>

<div style="flex:1;text-align:center;">
<h3>📊 View Results</h3>
<p>Receive detailed reports and actionable safety insights.</p>
</div>
</div>
</div>
""", height=400)
# ---------------- FOOTER WITH MODAL ---------------- #
components.html("""
<style>
.footer {
    text-align: center;
    padding: 20px;
    font-size: 16px;
    border-top: 1px solid #e0e0e0;
    margin-top: 50px;
    font-family: "Segoe UI", sans-serif;
}

.footer a {
    text-decoration: none;
    margin: 0 15px;
    color: #2C3E50;
    font-weight: 500;
    cursor: pointer;
}

.footer a:hover {
    color: #0078d4;
}

.modal-overlay {
    display: none;
    position: fixed;
    z-index: 999;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.4);
}

.modal-content {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: #ffffff;
    padding: 40px;
    width: 50%;
    max-width: 700px;
    border-radius: 15px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    font-family: "Segoe UI", sans-serif;
    line-height: 1.6;
}

.ok-btn {
    margin-top: 25px;
    padding: 10px 30px;
    background-color: #0078d4;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
}

.ok-btn:hover {
    background-color: #005fa3;
}
</style>

<div class="footer">
    <a href="mailto:cgmohan@aims.amrita.edu?subject=NanoToX Inquiry">Contact</a> |
    <a onclick="openModal()">Privacy</a> |
    <a href="https://www.amrita.edu/school/nanosciences/" target="_blank">Institution</a>
</div>

<div id="privacyModal" class="modal-overlay">
    <div class="modal-content">
        <h2>Privacy Policy</h2>
        <p>
            NanoToX is an academic research tool developed for nanotoxicity prediction.
            Uploaded datasets are processed only for generating prediction results and
            are not permanently stored. No personal data is sold or shared.
        </p>
        <p>
            For privacy-related concerns contact:
            <b>cgmohan@aims.amrita.edu</b>
        </p>
        <button class="ok-btn" onclick="closeModal()">OK</button>
    </div>
</div>

<script>
function openModal() {
    document.getElementById("privacyModal").style.display = "block";
}
function closeModal() {
    document.getElementById("privacyModal").style.display = "none";
}
</script>
""", height=350)