import streamlit as st
from pages.ui_utils import hide_streamlit
# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="NanoTox - Learn", layout="wide")
hide_streamlit()
# =========================
# CLEAN CSS (UPDATED)
# =========================
st.markdown("""
<style>

/* Background */
.main {
    background: linear-gradient(to right, #f8fafc, #eef2ff);
}

/* HERO */
.hero {
    text-align: center;
    padding: 45px;
    background: linear-gradient(135deg, #4f46e5, #0ea5e9);
    color: white;
    border-radius: 18px;
    margin-bottom: 30px;
}

/* Cards (🔥 FIXED HEIGHT + ALIGNMENT) */
.card {
    background: white;
    padding: 25px;
    border-radius: 16px;
    box-shadow: 0 6px 16px rgba(0,0,0,0.08);
    transition: 0.2s;

    /* 🔥 IMPORTANT FIX */
    min-height: 200px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.card:hover {
    transform: translateY(-4px);
}

/* Section title */
.section {
    font-size: 26px;
    font-weight: 600;
    margin-top: 35px;
    margin-bottom: 10px;
    color: #1e293b;
}

/* Text */
.text {
    color: #475569;
    font-size: 15px;
    line-height: 1.6;
}

/* Arrow container FIX */
.arrow {
    display: flex;
    align-items: center;     /* vertical center */
    justify-content: center; /* horizontal center */
    height: 200px;           /* match card height */
    font-size: 60px;
    color: #64748b;
}

/* Divider */
hr {
    border: none;
    height: 1px;
    background: #e2e8f0;
    margin: 30px 0;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HERO
# =========================
st.markdown("""
<div class="hero">
    <h1>🧪 NanoTox Intelligence Engine</h1>
    <p>AI-driven prediction of nanoparticle toxicity and biological safety</p>
</div>
""", unsafe_allow_html=True)

# =========================
# INTRO
# =========================
st.markdown("""
<div class="card text">
NanoTox is a next-generation machine learning platform designed to predict 
toxicity and cell viability of nanoparticles using integrated physicochemical 
and biological data. By combining machine learning with physicochemical and biological data, it estimates nanoparticle interactions with cells, tissues, and biological systems—before any experimental testing. This empowers researchers in nanomedicine, toxicology, and materials science to cut time, costs, and risks while advancing safer nanomaterial design. As a vital screening platform, NanoTox identifies hazardous nanostructures and guides the development of biocompatible alternatives. 
Our mission: accelerate Safe-by-Design nanomaterials through instant, data-backed safety insights.
</div>
""", unsafe_allow_html=True)

# =========================
# PIPELINE
# =========================
st.markdown('<div class="section">⚙️ Prediction Pipeline</div>', unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns([2,1,2,1,2])

with col1:
    st.markdown("""
    <div class="card text">
    <h4>🧬 Input</h4>
    Nanoparticle properties<br>
    Biological system<br>
    Exposure conditions
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown('<div class="arrow">➡️</div>', unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card text">
    <h4>🤖 AI Models</h4>
    XGBoost Regression<br>
    XGBoost Classification
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown('<div class="arrow">➡️</div>', unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="card text">
    <h4>📊 Output</h4>
    Viability (%)<br>
    Toxicity Probability<br>
    Final Classification
    </div>
    """, unsafe_allow_html=True)

# =========================
# INTERPRETATION
# =========================
st.markdown('<div class="section">📊 Interpretation</div>', unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    st.markdown("""
    <div class="card text">
    <h4>Cell Viability</h4>
    Higher values → Lower toxicity<br>
    Lower values → Higher cytotoxic effect
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card text">
    <h4>Toxicity Probability</h4>
    Range: 0 – 1<br>
    ≥ 0.5 → Classified as Toxic
    </div>
    """, unsafe_allow_html=True)

# =========================
# APPLICATIONS
# =========================
st.markdown('<div class="section">🚀 Applications</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card text">
• Nanomedicine safety assessment<br>
• Drug delivery system evaluation<br>
• Environmental nanotoxicology<br>
• Regulatory risk assessment
</div>
""", unsafe_allow_html=True)

# =========================
# FUTURE
# =========================
st.markdown('<div class="section">🔮 Future Scope</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card text">
• Deep learning integration<br>
• Explainable AI (XAI)<br>
• Larger datasets<br>
• Real-time prediction systems
</div>
""", unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("""
<hr>
<center style='color:#64748b'>
NanoTox • AI for Safer Nanomaterials
</center>
""", unsafe_allow_html=True)