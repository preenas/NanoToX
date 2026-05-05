import streamlit as st
import pandas as pd
import os
from PIL import Image
import joblib

from pages.predict import predict
from pages.ui_utils import hide_streamlit
# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="NanoTox ML System", layout="wide")
hide_streamlit()
# =========================
# LOAD FEATURES
# =========================
BASE_DIR = os.path.dirname(__file__)
features = joblib.load(os.path.join("pages", "feature_columns.pkl"))

# =========================
# HEADER
# =========================
try:
    head = Image.open("head.png")
    st.image(head, width=900)
except:
    st.warning("Header image not found")

st.markdown("<h2 style='text-align:center;'>NanoTox Prediction System</h2>", unsafe_allow_html=True)

# =========================
# NAVIGATION
# =========================
nav1, nav2, nav3 = st.columns([1, 6, 1])

with nav1:
    if st.button("⬅️ Home"):
        st.switch_page("Home_page.py")

with nav3:
    if st.button("🔄 Reset"):
        st.session_state.clear()
        st.rerun()

# =========================
# INPUT MODE
# =========================
option = st.radio("Select Input Method", ["Manual Input", "Upload File"], horizontal=True)

# =========================
# MANUAL INPUT
# =========================
if option == "Manual Input":

    st.header("Enter Experimental Details")

    c1, c2, c3 = st.columns(3)

    nanoparticle = c1.text_input("Nanoparticle")
    zeta = c2.number_input("Zeta potential (mV)", value=0.0)
    cell_age = c3.selectbox("Cell age (E/A)", ["A", "E"])

    c1, c2, c3 = st.columns(3)

    type_np = c1.selectbox("Type (O/I)", ["O", "I"])
    cells = c2.text_input("Cells")
    tissue = c3.text_input("Tissue source")

    c1, c2, c3 = st.columns(3)

    coating = c1.text_input("Coating", "")
    cell_line = c2.selectbox("Cell line (L/P)", ["L", "P"])
    exposure = c3.number_input("Exposure time (hr)", value=0.0)

    c1, c2, c3 = st.columns(3)

    diameter = c1.number_input("Diameter (nm)", value=0.0)
    animal = c2.selectbox("Animal/Human", ["Human", "Mouse"])
    test = c3.text_input("Test")

    c1, c2, c3 = st.columns(3)

    concentration = c1.number_input("Concentration μM", value=0.0)
    morphology = c2.text_input("Cell morphology")
    indicator = c3.text_input("Test indicator")

    st.subheader("Additional Conditions")

    c1, c2, c3 = st.columns(3)

    biochemical = c1.text_input("Biochemical metric")
    interference = c2.selectbox("Interference (Y/N)", ["Y", "N"])
    colloidal = c3.selectbox("Colloidal stability (Y/N)", ["Y", "N"])

    positive = st.selectbox("Positive control (Y/N)", ["Y", "N"])

    if st.button("🔬 Predict Toxicity"):

        user_input = {
            "Nanoparticle": nanoparticle,
            "Type: Organic (O)/inorganic (I)": type_np,
            "coat": coating,
            "Diameter (nm)": diameter,
            "Concentration μM": concentration,
            "Zeta potential (mV)": zeta,
            "Cells": cells,
            "Cell line (L)/primary cells (P)": cell_line,
            "Animal/ Human": animal,
            "Cell morphology": morphology,
            "Cell age: embryonic (E), Adult (A)": cell_age,
            "Cell-organ/tissue source": tissue,
            "Exposure time (h)": exposure,
            "Test": test,
            "Test indicator": indicator,
            "Biochemical metric": biochemical,
            "Interference checked (Y/N)": interference,
            "Colloidal stability checked (Y/N)": colloidal,
            "Positive control (Y/N)": positive
        }

        viability, prob, tox = predict(user_input)

        st.metric("Cell Viability (%)", round(viability, 4))
        st.metric("Toxicity Probability", round(prob, 4))

        if tox:
            st.error("⚠️ TOXIC")
        else:
            st.success("✅ NON-TOXIC")

# =========================
# FILE UPLOAD
# =========================
if option == "Upload File":

    st.header("Upload Dataset")

    file = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"])

    if file:

        if file.name.endswith(".csv"):
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file, engine="openpyxl")

        st.dataframe(df.head())

        for col in features:
            if col not in df.columns:
                df[col] = 0

        df = df.reindex(columns=features)

        if st.button("Run Prediction"):

            results = [predict(row.to_dict()) for _, row in df.iterrows()]

            df["Predicted Viability"] = [r[0] for r in results]
            df["Toxicity Probability"] = [r[1] for r in results]
            df["Toxic Class"] = ["Toxic" if r[2] else "Non-toxic" for r in results]

            st.dataframe(df)

            df.to_excel("results.xlsx", index=False)

            with open("results.xlsx", "rb") as f:
                st.download_button(
                    "⬇️ Download Results",
                    f,
                    file_name="NanoTox_results.xlsx"
                )