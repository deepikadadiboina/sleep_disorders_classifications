import streamlit as st

st.set_page_config(
    page_title="Login - Sleep Health",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Ensure session state keys exist
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ''
if 'user_email' not in st.session_state:
    st.session_state.user_email = ''
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {}

st.markdown("# 🔐 User Login")

if st.session_state.logged_in:
    st.success(f"Logged in as **{st.session_state.username}**")
    if st.button("✅ Go to Profile"):
        st.switch_page("pages/09_profile.py")
    if st.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ''
        st.session_state.user_email = ''
        st.session_state.user_profile = {}
        st.success("Logged out successfully.")
        st.stop()

with st.form(key='login_form'):
    username = st.text_input("Full Name", value=st.session_state.user_profile.get('name', ''))
    email = st.text_input("Email", value=st.session_state.user_profile.get('email', ''))
    age = st.number_input("Age", min_value=18, max_value=100, value=st.session_state.user_profile.get('age', 30))
    gender = st.selectbox("Gender", ['Male', 'Female', 'Other'], index=['Male','Female','Other'].index(st.session_state.user_profile.get('gender','Male')) if st.session_state.user_profile.get('gender','Male') in ['Male','Female','Other'] else 0)
    submit = st.form_submit_button("🔓 Login")

if submit:
    if not username or not email:
        st.error("Please provide both name and email.")
    else:
        st.session_state.logged_in = True
        st.session_state.username = username
        st.session_state.user_email = email
        st.session_state.user_profile = {
            'name': username,
            'email': email,
            'age': age,
            'gender': gender
        }
        st.success(f"Welcome back, {username}! You are now logged in.")
        st.switch_page("pages/09_profile.py")

st.markdown("---")
if st.button("🏠 Continue as Guest"):
    st.session_state.logged_in = False
    st.switch_page("app.py")
