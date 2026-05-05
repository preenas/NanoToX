import streamlit as st
from supabase import create_client, Client
from PIL import Image
import re

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="NanoToX Login",
    page_icon="🔒",
    layout="centered"
)

# ================= LOAD IMAGE =================
head = Image.open("/workspaces/NanoToX/head.png")
st.image(head, width=850)

# ================= CONNECT SUPABASE =================
SUPABASE_URL = st.secrets["supabase"]["url"]
SUPABASE_KEY = st.secrets["supabase"]["key"]
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ================= SESSION STATE =================
if "page" not in st.session_state:
    st.session_state.page = "home"

if "user" not in st.session_state:
    st.session_state.user = None


# ================= NAVIGATION FUNCTION =================
def go(page_name):
    st.session_state.page = page_name
    st.rerun()


# ================= PASSWORD VALIDATION =================
def valid_password(password, confirm):
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


# ==========================================================
# ======================= HOME =============================
# ==========================================================
if st.session_state.page == "home":

    if st.session_state.user:
        first_name = st.session_state.user.user_metadata.get("first_name", "")
        st.success(f"Welcome {first_name} 👋")

        if st.button("Try Prediction"):
            go("prediction")

        if st.button("Logout"):
            supabase.auth.sign_out()
            st.session_state.user = None
            st.rerun()

    else:
        st.markdown("### AI Driven Nanotoxicity Prediction Tool")

        if st.button("Login"):
            go("login")

        if st.button("Create Account"):
            go("signup")


# ==========================================================
# ======================= LOGIN ============================
# ==========================================================
elif st.session_state.page == "login":

    st.subheader("LOG IN")

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
                go("home")

        except Exception:
            st.error("Invalid email or password")

    if st.button("Forgot Password?"):
        go("reset")

    if st.button("Back"):
        go("home")


# ==========================================================
# ======================= SIGNUP ===========================
# ==========================================================
elif st.session_state.page == "signup":

    st.subheader("SIGN UP")

    account_type = st.radio("Select Account Type", ["Academia", "Industry"])
    email = st.text_input("Email Address")
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    institution = st.text_input("Institution Name")
    country = st.text_input("Country")

    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Create Account"):

        error = valid_password(password, confirm_password)

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
                go("login")

            except Exception:
                st.error("Signup failed")

    if st.button("Already have an account? Login"):
        go("login")


# ==========================================================
# ======================= RESET ============================
# ==========================================================
elif st.session_state.page == "reset":

    st.subheader("Reset Password")
    email = st.text_input("Enter your email")

    if st.button("Send Reset Link"):
        try:
            supabase.auth.reset_password_email(email)
            st.success("Password reset email sent!")
            go("login")
        except Exception:
            st.error("Error sending reset email")

    if st.button("Back to Login"):
        go("login")


# ==========================================================
# ==================== PREDICTION ==========================
# ==========================================================
elif st.session_state.page == "prediction":

    if not st.session_state.user:
        go("login")

    st.title("Prediction Page")

    user_input = st.text_input("Enter SMILES")

    if st.button("Predict"):
        st.success("Result: Toxic (Demo)")