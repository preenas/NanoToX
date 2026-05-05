import streamlit as st

def hide_streamlit():
    st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stToolbar"] {display: none;}
    </style>
    """, unsafe_allow_html=True)