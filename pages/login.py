import streamlit as st
from PIL import Image
import re
import os
from auth import login_user, signup_user, init_session
from pages.ui_utils import hide_streamlit

st.set_page_config(page_title="NanoToX Authentication", layout="centered")

hide_streamlit()
init_session()

# ================= SAFE PATH ================= #
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

head_path = os.path.join(BASE_DIR, "head.png")


# ================= HEADER ================= #
try:
    head = Image.open(head_path)
    st.image(head, use_container_width=True)
except:
    st.warning("Header image not found (head.png)")

# ================= SESSION ================= #

if "auth_page" not in st.session_state:
    st.session_state.auth_page = "login"

def switch(page):
    st.session_state.auth_page = page
    st.rerun()

# Password validation
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

# =================================================
# LOGIN
# =================================================
if st.session_state.auth_page == "login":

    st.markdown("## 🔐 LOG IN")

    email = st.text_input("Email Address")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        success = login_user(email, password)

        if success:
            st.success(f"Welcome {st.session_state.user_name} 👋")
            st.switch_page("Home_page.py")
        else:
            st.error("Invalid email or password")

    if st.button("Forgot password?"):
        switch("reset")

    st.write("Not a user?")
    if st.button("Create Account"):
        switch("signup")

# =================================================
# SIGNUP
# =================================================
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
            metadata = {
                "first_name": first_name,
                "last_name": last_name,
                "account_type": account_type,
                "institution": institution,
                "country": country
            }

            success = signup_user(email, password, metadata)

            if success:
                st.success("Account created! Check your email to verify.")
                switch("login")
            else:
                st.error("Signup failed")

    if st.button("Already have an account? Login"):
        switch("login")

# =================================================
# RESET PASSWORD
# =================================================
elif st.session_state.auth_page == "reset":

    from auth import supabase

    st.markdown("## 🔄 Reset Password")

    email = st.text_input("Enter your email")

    if st.button("Send Reset Link"):
        try:
            supabase.auth.reset_password_for_email(email)
            st.success("Reset link sent!")
            switch("login")
        except:
            st.error("Error sending reset email")

    if st.button("Back to Login"):
        switch("login")