import streamlit as st
from supabase import create_client, Client
from PIL import Image
import re
import os
st.set_page_config(page_title="NanoToX Authentication", layout="centered")
BASE_DIR = os.path.dirname(__file__)
head_path = os.path.join(BASE_DIR, "head.png")
# ---------- Header ----------
st.image(head_path, use_container_width=True)

# ---------- Supabase ----------
SUPABASE_URL = st.secrets["supabase"]["url"]
SUPABASE_KEY = st.secrets["supabase"]["key"]
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ---------- Session ----------
if "auth_page" not in st.session_state:
    st.session_state.auth_page = "login"

def switch(page):
    st.session_state.auth_page = page
    st.rerun()

# ---------- Password Validation ----------
def validate_password(password, confirm):
    if len(password) < 8:
        return "Password must be at least 8 characters"
    if not re.search(r"[A-Z]", password):
        return "Must contain a capital letter"
    if not re.search(r"[a-z]", password):
        return "Must contain a lowercase letter"
    if not re.search(r"\d", password):
        return "Must contain a number"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Must contain a special character"
    if password != confirm:
        return "Passwords do not match"
    return None

# =====================================================
# ================= LOGIN =============================
# =====================================================

if st.session_state.auth_page == "login":

    st.markdown("## 🔐 LOG IN")

    email = st.text_input("Email Address")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        try:
            response = supabase.auth.sign_in_with_password({
                "email": email,
                "password": password
            })

            if response.user:
                st.session_state.user = response.user
                st.success("Login successful!")
                st.switch_page("home.py")

        except:
            st.error("Invalid email or password")

    if st.button("Forgot password?"):
        switch("reset")

    st.write("Not a user?")
    if st.button("Create Account"):
        switch("signup")

# =====================================================
# ================= SIGNUP ============================
# =====================================================

elif st.session_state.auth_page == "signup":

    st.markdown("## 📝 SIGN UP")

    account_type = st.radio("Select Account Type", ["Academia", "Industry"])

    email = st.text_input("Email Address")
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    institution = st.text_input("Institution Name")
    country = st.text_input("Country")

    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Create Account"):

        error = validate_password(password, confirm_password)

        if error:
            st.error(error)

        else:
            try:
                supabase.auth.sign_up({
                    "email": email,
                    "password": password,
                    "options": {
                        "data": {
                            "first_name": first_name,
                            "last_name": last_name,
                            "account_type": account_type,
                            "institution": institution,
                            "country": country
                        }
                    }
                })

                st.success("Account created! Check your email to verify.")
                switch("login")

            except:
                st.error("Signup failed")

    if st.button("Already have an account? Login"):
        switch("login")

# =====================================================
# ================= RESET =============================
# =====================================================

elif st.session_state.auth_page == "reset":

    st.markdown("## 🔄 Reset Password")

    email = st.text_input("Enter your email")

    if st.button("Send Reset Link"):
        try:
            supabase.auth.reset_password_email(email)
            st.success("Reset link sent!")
            switch("login")
        except:
            st.error("Error sending reset email")

    if st.button("Back to Login"):
        switch("login")