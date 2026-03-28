import streamlit as st
import time
from utils.model import predictor
from utils.history import HistoryManager

st.set_page_config(
    page_title="Patient Details - Sleep Health",
    page_icon="😴",
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
    
    .input-card {
        background: linear-gradient(135deg, rgba(30, 58, 138, 0.15) 0%, rgba(15, 23, 42, 0.3) 100%);
        border: 1px solid rgba(59, 130, 246, 0.2);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white;
        padding: 12px 24px;
        border-radius: 8px;
        border: none;
        font-weight: 600;
        width: 100%;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'loading' not in st.session_state:
    st.session_state.loading = False

st.markdown("# 👤 Patient Details")

# Navigation quick links
nav1, nav2, nav3, nav4 = st.columns(4)
with nav1:
    if st.button("🏠 Home"):
        st.switch_page("app.py")
with nav2:
    if st.button("📜 History"):
        st.switch_page("pages/03_history.py")
with nav3:
    if st.button("👤 Profile"):
        st.switch_page("pages/09_profile.py")
with nav4:
    if st.session_state.get('logged_in', False):
        if st.button("🚪 Logout"):
            st.session_state.logged_in = False
            st.session_state.username = ''
            st.session_state.user_email = ''
            st.session_state.user_profile = {}
            st.success("Logged out successfully")
            st.switch_page("app.py")
    else:
        if st.button("🔐 Login"):
            st.switch_page("pages/00_login.py")

if not st.session_state.get('logged_in', False):
    st.info("You are using guest mode. History and profile are available after login.")

st.markdown("### Complete your health assessment to receive personalized sleep insights")
st.markdown("---")

# Create form columns
with st.container():
    # Personal Information Section
    st.markdown("""
    <div class="input-card">
        <h3 style="color: #e0f2fe; margin-top: 0;">👤 Personal Information</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        gender = st.selectbox(
            "Gender",
            options=["Male", "Female"],
            key="gender"
        )
        gender_val = 0 if gender == "Male" else 1
    
    with col2:
        age = st.slider(
            "Age (years)",
            min_value=18,
            max_value=85,
            value=35,
            step=1,
            key="age"
        )
    
    # Sleep Habits Section
    st.markdown("""
    <div class="input-card">
        <h3 style="color: #e0f2fe; margin-top: 0;">😴 Sleep Habits</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3, gap="medium")
    
    with col1:
        sleep_duration = st.slider(
            "Sleep Duration (hours)",
            min_value=2.0,
            max_value=12.0,
            value=7.0,
            step=0.5,
            key="sleep_duration"
        )
    
    with col2:
        sleep_quality = st.slider(
            "Sleep Quality (1-10)",
            min_value=1,
            max_value=10,
            value=7,
            step=1,
            key="sleep_quality"
        )
    
    with col3:
        stress_level = st.slider(
            "Stress Level (1-10)",
            min_value=1,
            max_value=10,
            value=5,
            step=1,
            key="stress_level"
        )
    
    snoring_level = st.slider(
        "Snoring Level (1-10, 1=None, 10=Severe)",
        min_value=1,
        max_value=10,
        value=3,
        step=1,
        key="snoring_level"
    )
    
    # Health Metrics Section
    st.markdown("""
    <div class="input-card">
        <h3 style="color: #e0f2fe; margin-top: 0;">🩺 Health Metrics</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        bmi_category = st.selectbox(
            "BMI Category",
            options=["Underweight", "Normal Weight", "Overweight", "Obese"],
            index=1,
            key="bmi_category"
        )
        bmi_val = {"Underweight": 0, "Normal Weight": 1, "Overweight": 2, "Obese": 3}[bmi_category]
    
    with col2:
        heart_rate = st.slider(
            "Heart Rate (bpm)",
            min_value=50,
            max_value=150,
            value=75,
            step=1,
            key="heart_rate"
        )
    
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        sbp = st.slider(
            "Systolic Blood Pressure (mmHg)",
            min_value=90,
            max_value=180,
            value=120,
            step=1,
            key="sbp"
        )
    
    with col2:
        dbp = st.slider(
            "Diastolic Blood Pressure (mmHg)",
            min_value=60,
            max_value=120,
            value=80,
            step=1,
            key="dbp"
        )
    
    col1, col2, col3 = st.columns(3, gap="medium")
    
    with col1:
        physical_activity = st.slider(
            "Physical Activity (days/week)",
            min_value=0,
            max_value=7,
            value=3,
            step=1,
            key="physical_activity"
        )
    
    with col2:
        daily_steps = st.slider(
            "Daily Steps (thousands)",
            min_value=0,
            max_value=20,
            value=8,
            step=1,
            key="daily_steps"
        )
    
    with col3:
        oxygen_saturation = st.slider(
            "Oxygen Saturation (%)",
            min_value=90.0,
            max_value=100.0,
            value=98.0,
            step=0.1,
            key="oxygen_saturation"
        )
    
    st.markdown("---")
    
    # Collect patient data
    patient_data = {
        'gender': gender_val,
        'age': age,
        'sleep_duration': sleep_duration,
        'sleep_quality': sleep_quality,
        'stress_level': stress_level,
        'snoring_level': snoring_level,
        'bmi_category': bmi_val,
        'heart_rate': heart_rate,
        'sbp': sbp,
        'dbp': dbp,
        'physical_activity': physical_activity,
        'daily_steps': daily_steps * 1000,  # Convert thousands to steps
        'oxygen_saturation': oxygen_saturation
    }
    
    # Analyze Sleep Button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔍 Analyze Sleep", key="analyze_btn", use_container_width=True):
            # Save to session state and show loading
            st.session_state.patient_data = patient_data
            st.session_state.loading = True
            
            # Show loading animation
            with st.spinner(""):
                loading_placeholder = st.empty()
                
                with loading_placeholder.container():
                    st.markdown("""
                    <div style="text-align: center; padding: 2rem;">
                        <div style="animation: pulse 1.5s ease-in-out infinite; font-size: 2rem;">⏳</div>
                        <p style="color: #94a3b8; font-size: 1.2rem; margin-top: 1rem;">
                            Analyzing your sleep data...
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
                
                time.sleep(2)  # Simulate processing
            
            # Get prediction
            prediction_result = predictor.predict(patient_data)
            st.session_state.prediction_result = prediction_result
            
            # Get recommendations
            recommendations = predictor.get_recommendations(patient_data, prediction_result)
            st.session_state.recommendations = recommendations
            
            # Save to history (user-aware)
            history_manager = HistoryManager()
            history_manager.add_prediction(patient_data, prediction_result, username=st.session_state.username)
            
            # Switch to results page
            st.switch_page("pages/02_results.py")

st.sidebar.markdown("---")
st.sidebar.markdown("💡 **Tip**: Ensure all measurements are as accurate as possible for better predictions.")
