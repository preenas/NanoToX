import streamlit as st
from PIL import Image
import os
import base64
from pages.ui_utils import hide_streamlit
# ================= PAGE CONFIG ================= #
st.set_page_config(page_title="Gopi Mohan - About", layout="wide")
hide_streamlit()

# ================= BASE DIRECTORY ================= #
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def img_path(file):
    return os.path.join(BASE_DIR, file)

# ================= SAFE IMAGE FUNCTIONS ================= #
def safe_show_image(file, width=None):
    path = img_path(file)
    if os.path.exists(path):
        st.image(path, width=width)
    else:
        st.warning(f"Missing file: {file}")

def load_square_image(file):
    path = img_path(file)

    if not os.path.exists(path):
        st.warning(f"Missing file: {file}")
        return None

    img = Image.open(path).convert("RGB")

    # center crop
    w, h = img.size
    min_dim = min(w, h)

    left = (w - min_dim) // 2
    top = (h - min_dim) // 2
    right = (w + min_dim) // 2
    bottom = (h + min_dim) // 2

    img = img.crop((left, top, right, bottom))

    # FORCE UNIFORM SIZE
    img = img.resize((300, 300))

    return img

# ================= CUSTOM CSS ================= #
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">

<style>
.stApp {
    background: #f5f8fc;
}

.big-title {
    text-align: center;
    font-family: 'Playfair Display', serif;
    font-size: 62px;
    font-weight: 700;
    color: #1E3A8A;
}

.name-style {
    font-family: 'Inter', sans-serif;
    font-size: 34px;
    font-weight: 600;
    color: #0f172a;
}

.details {
    font-family: 'Inter', sans-serif;
    font-size: 18px;
    line-height: 1.8;
    color: #334155;
}

.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 30px;
    font-weight: 600;
    color: #2F4F75;
}
</style>
""", unsafe_allow_html=True)

# ================= TITLE ================= #
st.markdown(
    "<div class='big-title'>Welcome to Gopi Mohan’s<br>Cheminformatics Lab</div>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# ================= PROFILE ================= #
col1, col2 = st.columns([1.2, 2])

with col1:
    safe_show_image("sir1.png", width=380)

with col2:
    st.markdown("<div class='name-style'>Dr. Gopi Mohan C.</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='details'>
    <b>Professor</b><br>
    Amrita School of Nanosciences and Molecular Medicine, Kochi<br><br>

    <b>Qualification:</b> Ph.D<br><br>

    <b>Email:</b> cgmohan@aims.amrita.edu<br><br>

    <b>Research Interests:</b> Computational Biology, Structural Bioinformatics, Nanoinformatics
    </div>
    """, unsafe_allow_html=True)

# ================= BACKGROUND ================= #
st.markdown("<div class='section-title'>Background</div>", unsafe_allow_html=True)

st.markdown("""
<div class='details'>
Dr. Gopi Mohan C. is a Professor at Bioinformatics & Computational Biology Group, 
Amrita Center for Nanosciences and Molecular Medicine. He had graduated with Ph.D. 
from Banaras Hindu University, Varanasi, following which, had gained experience as 
Post-doctoral fellow from the Molecular Biophysics Unit at the Indian Institute of Science, Bangalore, 
and as Research Officer from the Department of Biology and Biochemistry, University of Bath, United Kingdom.

Further, he had worked as an Associate Researcher of CNRS in Laboratoire de Cristallographie, 
and Modelisation des Materiaux Mineraux et Biologiques, University Henri Poincare, Nancy, France.

Dr. Gopi Mohan has experience being a faculty at the National Institute of Pharmaceutical Education & Research (NIPER), 
Mohali, Punjab, from 2005 and serving there for six and half years. During his stay at NIPER, 
he has been instrumental in setting up different laboratories in the Pharmacoinformatics discipline.

He was a recipient of Indo-Finland grant for computational biology, relating to drug development, 
and had visited University of Helsinki and University of Turku, to complete this collaborative bilateral program successfully.

Dr. Gopi Mohan has supervised many Ph.D. and postgraduate students, and completed many research and industrial consultancy projects. 
He has published more than 70 research papers in refereed journals and is also an active reviewer of different international/national research journals, thesis and grants.

Research interests of Dr. Gopi Mohan encompass Computational Biology & Structural Bioinformatics, 
Structure-Based Drug Design, Protein Crystallography, and Nanoinformatics. 
Dr. Gopi Mohan is cited as an internationally recognized expert in the field of Structural Bioinformatics & Chemoinformatics by Synergix Ltd., United Kingdom.
</div>

""", unsafe_allow_html=True)

# ================= PHD SCHOLARS ================= #
st.markdown("<div class='section-title'>Ph.D. Scholars</div>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    img = load_square_image("pic1.jpg")
    if img:
        st.image(img, width=180)
    st.markdown("**Abdul Rahoof S.**")

with col2:
    img = load_square_image("pic2.png")
    if img:
        st.image(img, width=180)
    st.markdown("**Preena S. Parvathy**")

with col3:
    img = load_square_image("pic3.jpg")
    if img:
        st.image(img, width=180)
    st.markdown("**Reshmi R.**")

with col4:
    img = load_square_image("pic4.jpg")
    if img:
        st.image(img, width=180)
    st.markdown("**Lakshmi A. Nair**")

# ================= RESEARCH GROUP ================= #
def get_base64(path):
    full_path = img_path(path)
    if os.path.exists(full_path):
        with open(full_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

img1 = get_base64("team1.jpg")
img2 = get_base64("team2.jpg")

st.markdown("<div style='height:40px;'></div>", unsafe_allow_html=True)

st.markdown(f"""
<style>
.carousel-container {{
    max-width: 900px;
    margin: auto;
    overflow: hidden;
}}

.carousel-wrapper {{
    display: flex;
    width: 200%;
    animation: slide 8s infinite;
}}

.carousel-wrapper img {{
    width: 50%;
    border-radius: 20px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.15);
}}

@keyframes slide {{
    0% {{ transform: translateX(0%); }}
    45% {{ transform: translateX(0%); }}
    50% {{ transform: translateX(-50%); }}
    95% {{ transform: translateX(-50%); }}
    100% {{ transform: translateX(0%); }}
}}
</style>

<div class="section-title" style="text-align:center;">Research Group</div>
<div style="height:25px;"></div>

<div class="carousel-container">
    <div class="carousel-wrapper">
        <img src="data:image/jpeg;base64,{img1}">
        <img src="data:image/jpeg;base64,{img2}">
    </div>
</div>
""", unsafe_allow_html=True)

# ================= FOOTER ================= #
st.markdown("""
<hr style="margin-top:60px;">
<div style="text-align:center; padding:20px; font-size:15px;">
    <b>Team Cheminformatics</b><br>
    Amrita School of Nanosciences and Molecular Medicine
</div>
""", unsafe_allow_html=True)