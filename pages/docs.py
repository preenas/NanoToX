import streamlit as st
from pages.ui_utils import hide_streamlit
# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="NanoTox - Documentation", layout="wide")
hide_streamlit()
# =========================
# CLEAN CSS (NO CARDS)
# =========================
st.markdown("""
<style>

.main {
    background: linear-gradient(to right, #f8fafc, #eef2ff);
}

/* Section titles */
.section {
    font-size: 26px;
    font-weight: 600;
    margin-top: 35px;
    margin-bottom: 10px;
    color: #1e293b;
}

/* Paragraph text */
.text {
    color: #475569;
    font-size: 15px;
    line-height: 1.7;
    margin-bottom: 15px;
}

/* Table styling */
table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 10px;
}

th, td {
    border: 1px solid #e2e8f0;
    padding: 10px;
    text-align: left;
}

th {
    background-color: #f1f5f9;
}

/* Divider */
hr {
    border: none;
    height: 1px;
    background: #e2e8f0;
    margin: 25px 0;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.markdown("<h1>📘 NanoTox Documentation</h1>", unsafe_allow_html=True)

# =========================
# OVERVIEW
# =========================
st.markdown('<div class="section">🔍 Overview</div>', unsafe_allow_html=True)

st.markdown("""
<p class="text">
NanoTox is an AI-driven platform designed to predict nanoparticle toxicity and cell viability 
based on physicochemical and biological parameters. It enables rapid in silico screening, 
reducing reliance on time-consuming and costly experimental methods.
</p>

<p class="text">
The system supports Safe-by-Design nanomaterial development by identifying potential risks 
early in the research pipeline.
</p>
""", unsafe_allow_html=True)

# =========================
# SYSTEM ARCHITECTURE
# =========================
st.markdown('<div class="section">⚙️ System Architecture</div>', unsafe_allow_html=True)

st.markdown("""
<p class="text"><b>1. Input Layer</b><br>
Physicochemical and biological parameters are provided by the user.</p>

<p class="text"><b>2. Preprocessing</b><br>
• Encoding of categorical variables<br>
• Feature alignment<br>
• Data normalization using scaler</p>

<p class="text"><b>3. Machine Learning Models</b><br>
• XGBoost Regressor → Predicts cell viability (%)<br>
• XGBoost Classifier → Predicts toxicity probability</p>

<p class="text"><b>4. Output Layer</b><br>
• Viability score<br>
• Toxicity probability<br>
• Final classification (Toxic / Non-toxic)</p>
""", unsafe_allow_html=True)

# =========================
# INPUT FEATURES (KEEP TABLE)
# =========================
st.markdown('<div class="section">🧬 Input Features</div>', unsafe_allow_html=True)

st.markdown("""
<table>
<tr><th>Feature</th><th>Description</th></tr>
<tr><td>Nanoparticle</td><td>Type of nanoparticle material</td></tr>
<tr><td>Diameter (nm)</td><td>Particle size</td></tr>
<tr><td>Zeta potential</td><td>Surface charge</td></tr>
<tr><td>Coating</td><td>Surface functionalization</td></tr>
<tr><td>Concentration (μM)</td><td>Exposure concentration</td></tr>
<tr><td>Cells</td><td>Cell type used in study</td></tr>
<tr><td>Cell line</td><td>Primary or cell line classification</td></tr>
<tr><td>Tissue source</td><td>Origin of biological sample</td></tr>
<tr><td>Exposure time (h)</td><td>Duration of exposure</td></tr>
<tr><td>Test</td><td>Experimental assay</td></tr>
<tr><td>Biochemical metric</td><td>Measurement indicator</td></tr>
</table>
""", unsafe_allow_html=True)

# =========================
# MODEL DETAILS
# =========================
st.markdown('<div class="section">🤖 Model Details</div>', unsafe_allow_html=True)

st.markdown("""
<p class="text">
<b>Algorithm:</b> XGBoost (Extreme Gradient Boosting)
</p>

<p class="text">
<b>Why XGBoost?</b><br>
• Handles mixed numerical and categorical data<br>
• Robust to noise and missing values<br>
• High predictive performance for tabular datasets
</p>

<p class="text">
<b>Models Used:</b><br>
• Regression Model → Predicts cell viability (%)<br>
• Classification Model → Predicts toxicity probability
</p>
""", unsafe_allow_html=True)

# =========================
# OUTPUT INTERPRETATION
# =========================
st.markdown('<div class="section">📊 Output Interpretation</div>', unsafe_allow_html=True)

st.markdown("""
<p class="text">
<b>Cell Viability (%)</b><br>
Higher values indicate lower toxicity, while lower values indicate cytotoxic effects.
</p>

<p class="text">
<b>Toxicity Probability</b><br>
Range: 0 to 1<br>
≥ 0.5 → Classified as Toxic<br>
&lt; 0.5 → Classified as Non-toxic
</p>
""", unsafe_allow_html=True)

# =========================
# LIMITATIONS
# =========================
st.markdown('<div class="section">⚠️ Limitations</div>', unsafe_allow_html=True)

st.markdown("""
<p class="text">
• Predictions are based on the training dataset and may not generalize to all nanoparticles.<br>
• The system does not replace experimental validation.<br>
• Performance depends on input data quality.
</p>
""", unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("""
<hr>
<center style='color:#64748b'>
NanoTox Documentation • AI for Safer Nanomaterials
</center>
""", unsafe_allow_html=True)