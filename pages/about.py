import streamlit as st
from PIL import Image
import os
import base64

st.set_page_config(page_title="Gopi Mohan - About", layout="wide")

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">

<style>

/* Clean Research Background */
.stApp {
    background: #f5f8fc;
}

/* Fade Animation */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(25px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Main Title */
.big-title {
    text-align: center;
    font-family: 'Playfair Display', serif;
    font-size: 68px;
    font-weight: 700;
    color: #1E3A8A;
    letter-spacing: 1px;
    margin-bottom: 10px;
    animation: fadeInUp 1.2s ease-out;
}
/* Accent Line Below Title */
.title-line {
    width: 120px;
    height: 4px;
    background: #3B82F6;
    margin: 20px auto 50px auto;
    border-radius: 2px;
    animation: fadeInUp 1.4s ease-out;
}
/* Name */
.name-style {
    font-family: 'Inter', sans-serif;
    font-size: 36px;
    font-weight: 600;
    color: #0f172a;
}

/* Details */
.details {
    font-family: 'Inter', sans-serif;
    font-size: 19px;
    line-height: 1.8;
    color: #334155;
}

/* Section Heading */
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 32px;
    font-weight: 600;
    color: #2F4F75;
    margin-bottom: 10px;
}

/* Background Text */
.background-text {
    font-family: 'Poppins', sans-serif;
    font-size: 19px;
    line-height: 1.9;
    text-align: justify;
    color: #444444;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ---------------- #
st.markdown(
    "<div class='big-title'>Welcome to Gopi Mohan’s<br>Cheminformatics Lab</div>",
    unsafe_allow_html=True
)

st.markdown("<div style='height:40px;'></div>", unsafe_allow_html=True)

# ---------------- PROFILE SECTION ---------------- #
col1, col2 = st.columns([1.2, 2])

with col1:
    image = Image.open("/workspaces/NanoToX/sir1.png")
    st.image(image,width=400)

with col2:
    st.markdown("<div class='name-style'>Dr. Gopi Mohan C.</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='details'>
    <b>Professor</b><br>
    Amrita School of Nanosciences and Molecular Medicine, Kochi<br><br>

    <b>Qualification:</b> Ph.D<br><br>

    <b>Email:</b> 
    <a href="mailto:cgmohan@aims.amrita.edu">cgmohan@aims.amrita.edu</a><br><br>

    <b>Research Interests:</b> Computational Biology & Structural Bioinformatics, 
    Nanoinformatics, Protein Crystallography, Structure-Based Drug Design
    </div>
    """, unsafe_allow_html=True)



# ---------------- BACKGROUND ---------------- #
st.markdown("<div class='section-title'>Background</div>", unsafe_allow_html=True)

st.markdown("""
<div class='background-text'>
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


# ---------------- PHD SCHOLARS SECTION ---------------- #

st.markdown("<div class='section-title'>Ph.D. Scholars</div>", unsafe_allow_html=True)
st.markdown("<div style='height:30px;'></div>", unsafe_allow_html=True)

# Get base directory dynamically (SAFE method)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def load_square_image(filename):
    img_path = os.path.join(BASE_DIR, filename)
    img = Image.open(img_path)

    # Crop to square (center crop)
    width, height = img.size
    min_dim = min(width, height)
    left = (width - min_dim) // 2
    top = (height - min_dim) // 2
    right = (width + min_dim) // 2
    bottom = (height + min_dim) // 2
    img = img.crop((left, top, right, bottom))

    return img

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("<div class='scholar-card'>", unsafe_allow_html=True)
    st.image(load_square_image("pic1.jpg"), width=160)
    st.markdown("<div class='scholar-name'>Abdul Rahoof S.</div>", unsafe_allow_html=True)
    st.markdown("<div class='scholar-role'>Ph.D. Scholar</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='scholar-card'>", unsafe_allow_html=True)
    st.image(load_square_image("pic2.png"), width=160)
    st.markdown("<div class='scholar-name'>Preena S. Parvathy</div>", unsafe_allow_html=True)
    st.markdown("<div class='scholar-role'>Ph.D. Scholar</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='scholar-card'>", unsafe_allow_html=True)
    st.image(load_square_image("pic3.jpg"), width=160)
    st.markdown("<div class='scholar-name'>Reshmi R.</div>", unsafe_allow_html=True)
    st.markdown("<div class='scholar-role'>Ph.D. Scholar</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col4:
    st.markdown("<div class='scholar-card'>", unsafe_allow_html=True)
    st.image(load_square_image("pic4.jpg"), width=160)
    st.markdown("<div class='scholar-name'>Lakshmi A. Nair</div>", unsafe_allow_html=True)
    st.markdown("<div class='scholar-role'>Ph.D. Scholar</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- RESEARCH GROUP CAROUSEL ---------------- #

def get_image_base64(path):
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()

img1 = get_image_base64("team1.jpg")
img2 = get_image_base64("team2.jpg")

st.markdown("<div style='height:40px;'></div>", unsafe_allow_html=True)

st.markdown(f"""
<style>
.carousel-container {{
    position: relative;
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
    box-shadow: 0 15px 40px rgba(0, 60, 120, 0.15);
}}

@keyframes slide {{
    0%   {{ transform: translateX(0%); }}
    45%  {{ transform: translateX(0%); }}
    50%  {{ transform: translateX(-50%); }}
    95%  {{ transform: translateX(-50%); }}
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

# ---------------- PAGE END ---------------- #


st.markdown("<div style='height:80px;'></div>", unsafe_allow_html=True)

st.markdown("""
<hr style="border: none; height: 1px; background-color: #e5e7eb; width: 60%; margin: auto;">

<div style="
    text-align: center;
    padding: 30px 20px;
    font-size: 15px;
    color: #334155;
    letter-spacing: 0.3px;
">
    <em>Thank you for visiting our site.</em>
    <br><br>
    <span style="font-weight: 500;">
        Team Cheminformatics
    </span><br>
    Amrita School of Nanoscience and Molecular Medicine<br>
    Amrita Vishwavidhyapeetham, Kochi
</div>
""", unsafe_allow_html=True)