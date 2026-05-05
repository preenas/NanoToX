import streamlit as st
from supabase import create_client, Client

# Supabase connection
SUPABASE_URL = st.secrets["supabase"]["url"]
SUPABASE_KEY = st.secrets["supabase"]["key"]

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ------------------------------
# Session Setup
# ------------------------------
def init_session():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "user_name" not in st.session_state:
        st.session_state.user_name = None
    if "user_email" not in st.session_state:
        st.session_state.user_email = None

# ------------------------------
# Login Function
# ------------------------------
def login_user(email, password):
    try:
        response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })

        if response.user:
            st.session_state.logged_in = True
            st.session_state.user_email = response.user.email
            st.session_state.user_name = response.user.user_metadata.get("first_name", "User")
            return True

    except Exception:
        return False

# ------------------------------
# Signup Function
# ------------------------------
def signup_user(email, password, metadata):
    try:
        supabase.auth.sign_up({
            "email": email,
            "password": password,
            "options": {
                "data": metadata
            }
        })
        return True
    except Exception:
        return False

# ------------------------------
# Logout
# ------------------------------
def logout_user():
    supabase.auth.sign_out()
    st.session_state.clear()