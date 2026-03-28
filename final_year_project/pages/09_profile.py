import streamlit as st
from utils.history import HistoryManager
from datetime import datetime

st.set_page_config(
    page_title="Profile - Sleep Health",
    page_icon="👤",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Styling
st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%);
        color: #f1f5f9;
    }
    
    .profile-card {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.15) 0%, rgba(30, 58, 138, 0.25) 100%);
        border: 2px solid rgba(59, 130, 246, 0.4);
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
    }
    
    .stat-box {
        background: rgba(30, 58, 138, 0.2);
        border-radius: 10px;
        padding: 1.5rem;
        text-align: center;
        border: 1px solid rgba(59, 130, 246, 0.2);
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white;
        border-radius: 8px;
        border: none;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# Require login for profile page
if not st.session_state.get('logged_in', False):
    st.warning("⚠️ Please login first to view your profile.")
    if st.button("Go to Login"):
        st.switch_page("pages/00_login.py")
    st.stop()

st.markdown("# 👤 My Profile")

nav1, nav2, nav3, nav4 = st.columns(4)
with nav1:
    if st.button("🏠 Home", key="profile_home"):
        st.switch_page("app.py")
with nav2:
    if st.button("📜 History", key="profile_history"):
        st.switch_page("pages/03_history.py")
with nav3:
    if st.button("➕ New Assessment", key="profile_new_assessment"):
        st.switch_page("pages/01_patient_details.py")
with nav4:
    if st.button("🚪 Logout", key="profile_logout"):
        st.session_state.logged_in = False
        st.session_state.username = ''
        st.session_state.user_email = ''
        st.session_state.user_profile = {}
        st.success("Logged out successfully")
        st.switch_page("app.py")

st.markdown("---")

history_manager = HistoryManager()
history = history_manager.load_user_history(st.session_state.username)

st.markdown(f"### Welcome, {st.session_state.username}")

# Profile edit form
with st.form(key='profile_form'):
    profile_name = st.text_input("Full Name", value=st.session_state.user_profile.get('name', st.session_state.username))
    profile_email = st.text_input("Email", value=st.session_state.user_profile.get('email', st.session_state.user_email))
    profile_age = st.number_input("Age", min_value=18, max_value=100, value=st.session_state.user_profile.get('age', 30))
    profile_gender = st.selectbox("Gender", ['Male', 'Female', 'Other'], index=['Male','Female','Other'].index(st.session_state.user_profile.get('gender', 'Male')) if st.session_state.user_profile.get('gender', 'Male') in ['Male','Female','Other'] else 0)
    save_profile = st.form_submit_button("💾 Update Profile")

if save_profile:
    st.session_state.user_profile = {
        'name': profile_name,
        'email': profile_email,
        'age': profile_age,
        'gender': profile_gender
    }
    st.session_state.username = profile_name
    st.session_state.user_email = profile_email
    st.success("✅ Profile updated")

st.markdown("---")

# Quick nav buttons
nav1, nav2, nav3 = st.columns(3)
with nav1:
    if st.button("🏠 Home"):
        st.switch_page("app.py")
with nav2:
    if st.button("📜 History"):
        st.switch_page("pages/03_history.py")
with nav3:
    if st.button("➕ New Assessment"):
        st.switch_page("pages/01_patient_details.py")

# Profile Header
st.markdown("""
<div class="profile-card">
    <div style="display: flex; align-items: center; gap: 2rem;">
        <div style="font-size: 4rem;">😴</div>
        <div>
            <h2 style="margin: 0; color: #e0f2fe;">Sleep Health Tracker</h2>
            <p style="color: #94a3b8; margin: 0.5rem 0;">Monitor your sleep patterns and improve your health</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("### 📊 Your Statistics")

if history:
    col1, col2, col3, col4 = st.columns(4, gap="medium")
    
    # Calculate stats
    total_assessments = len(history)
    avg_sleep_duration = sum(h['sleep_duration'] for h in history) / total_assessments if history else 0
    avg_stress = sum(h['stress_level'] for h in history) / total_assessments if history else 0
    
    predictions = {}
    for entry in history:
        pred = entry['prediction']
        predictions[pred] = predictions.get(pred, 0) + 1
    
    most_common = max(predictions, key=predictions.get) if predictions else "N/A"
    
    with col1:
        st.markdown(f"""
        <div class="stat-box">
            <div style="font-size: 2rem; font-weight: bold; color: #3b82f6;">{total_assessments}</div>
            <div style="color: #94a3b8; font-size: 0.9rem; margin-top: 0.5rem;">Total Assessments</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="stat-box">
            <div style="font-size: 2rem; font-weight: bold; color: #10b981;">{avg_sleep_duration:.1f}h</div>
            <div style="color: #94a3b8; font-size: 0.9rem; margin-top: 0.5rem;">Avg Sleep Duration</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="stat-box">
            <div style="font-size: 2rem; font-weight: bold; color: #f59e0b;">{avg_stress:.1f}/10</div>
            <div style="color: #94a3b8; font-size: 0.9rem; margin-top: 0.5rem;">Avg Stress Level</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="stat-box">
            <div style="font-size: 1.8rem; margin-bottom: 0.5rem;">📊</div>
            <div style="font-size: 1.2rem; font-weight: bold; color: #e0f2fe;">{most_common}</div>
            <div style="color: #94a3b8; font-size: 0.9rem; margin-top: 0.5rem;">Most Common</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Recent Assessments
    st.markdown("### 📈 Recent Assessments")
    
    for i, entry in enumerate(reversed(history[-5:])):
        date = entry.get('date', 'Unknown date')
        prediction = entry['prediction']
        risk = entry['risk_level']
        confidence = entry['confidence']
        
        # Color based on prediction
        color_map = {
            'Normal Sleep': '#10b981',
            'Insomnia': '#f59e0b',
            'Sleep Apnea': '#ef4444'
        }
        color = color_map.get(prediction, '#3b82f6')
        
        st.markdown(f"""
        <div style="background: rgba(30, 58, 138, 0.2); padding: 1rem; border-radius: 8px; margin: 0.5rem 0; border-left: 4px solid {color};">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <div style="color: #e0f2fe; font-weight: bold; font-size: 1.1rem;">{prediction}</div>
                    <div style="color: #94a3b8; font-size: 0.85rem;">{date}</div>
                </div>
                <div style="text-align: right;">
                    <div style="color: {color}; font-weight: bold;">Risk: {risk}</div>
                    <div style="color: #94a3b8; font-size: 0.85rem;">Confidence: {confidence:.0f}%</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
else:
    st.info("📋 No assessment history yet.")

st.markdown("---")

# Action buttons
col1, col2, col3 = st.columns([1, 1, 1], gap="medium")

with col1:
    st.markdown("[🏠 Home](../)", unsafe_allow_html=True)

with col2:
    if st.button("📊 New Assessment", use_container_width=True):
        st.switch_page("pages/01_patient_details.py")

with col3:
    if st.button("📜 Full History", use_container_width=True):
        st.switch_page("pages/03_history.py")
