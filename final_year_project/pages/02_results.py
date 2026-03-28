import streamlit as st
from utils.report_generator import ReportGenerator
from datetime import datetime

st.set_page_config(
    page_title="Results - Sleep Health",
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
    
    .result-card {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.15) 0%, rgba(30, 58, 138, 0.25) 100%);
        border: 2px solid rgba(59, 130, 246, 0.4);
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        margin: 1rem 0;
    }
    
    .prediction-text {
        font-size: 2.5rem;
        font-weight: bold;
        margin: 1rem 0;
    }
    
    .risk-badge {
        display: inline-block;
        padding: 0.75rem 1.5rem;
        border-radius: 8px;
        font-weight: 600;
        font-size: 1.1rem;
        margin: 0.5rem;
    }
    
    .rec-card {
        background: rgba(30, 58, 138, 0.2);
        border-left: 4px solid #3b82f6;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.75rem 0;
        color: #cbd5e1;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white;
        padding: 12px 20px;
        border-radius: 8px;
        border: none;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# Top navigation
nav1, nav2, nav3, nav4 = st.columns(4)
with nav1:
    if st.button("🏠 Home", key="results_home_top"):
        st.switch_page("app.py")
with nav2:
    if st.button("🔙 Back", key="results_back_top"):
        st.switch_page("pages/01_patient_details.py")
with nav3:
    if st.button("📜 History", key="results_history_top"):
        st.switch_page("pages/03_history.py")
with nav4:
    if st.session_state.get('logged_in', False):
        if st.button("🚪 Logout", key="results_logout_top"):
            st.session_state.logged_in = False
            st.session_state.username = ''
            st.session_state.user_email = ''
            st.session_state.user_profile = {}
            st.success("Logged out successfully")
            st.switch_page("app.py")
    else:
        if st.button("🔐 Login", key="results_login_top"):
            st.switch_page("pages/00_login.py")

if not st.session_state.get('logged_in', False):
    st.info("Guest mode: results are available, but history/profile will not be saved.")

# Check if we have results
if st.session_state.get('prediction_result') is None:
    st.warning("⚠️ No assessment results found. Please complete the patient details form first.")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Go to Assessment", use_container_width=True):
            st.switch_page("pages/01_patient_details.py")
else:
    patient_data = st.session_state.patient_data
    prediction_result = st.session_state.prediction_result
    recommendations = st.session_state.recommendations
    
    st.markdown("# 📊 Assessment Results")
    st.markdown("---")
    
    # Simple result display
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"### {prediction_result['emoji']} {prediction_result['prediction']}")
        st.metric("Predicted Condition", prediction_result['prediction'], delta=f"Risk: {prediction_result['risk_level'].upper()}")
        st.metric("Confidence Score", f"{prediction_result['confidence']:.1f}%")
    
    st.markdown("---")
    
    # Key Findings
    st.markdown("### 🔍 Key Findings")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("😴 Sleep Duration", f"{patient_data['sleep_duration']:.1f} hrs")
    with col2:
        st.metric("⭐ Sleep Quality", f"{patient_data['sleep_quality']}/10")
    with col3:
        st.metric("😰 Stress Level", f"{patient_data['stress_level']}/10")
    with col4:
        st.metric("❤️ Heart Rate", f"{patient_data['heart_rate']} bpm")
    
    # Recommendations Section
    st.markdown("---")
    st.markdown("### 💡 Personalized Recommendations")
    
    rec_col1, rec_col2, rec_col3 = st.columns(3, gap="medium")
    
    # Lifestyle
    with rec_col1:
        st.markdown("#### 🧘 Lifestyle")
        if 'lifestyle' in recommendations:
            for rec in recommendations['lifestyle']:
                st.markdown(f'<div class="rec-card">{rec}</div>', unsafe_allow_html=True)
    
    # Sleep Habits
    with rec_col2:
        st.markdown("#### 😴 Sleep Habits")
        if 'sleep_habits' in recommendations:
            for rec in recommendations['sleep_habits']:
                st.markdown(f'<div class="rec-card">{rec}</div>', unsafe_allow_html=True)
    
    # Medical Advice
    with rec_col3:
        st.markdown("#### 🩺 Medical Advice")
        if 'medical_advice' in recommendations:
            for rec in recommendations['medical_advice']:
                st.markdown(f'<div class="rec-card">{rec}</div>', unsafe_allow_html=True)
    
    # Action Buttons
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 1, 1], gap="medium")
    
    with col1:
        if st.button("📥 Download Report", use_container_width=True):
            try:
                report_generator = ReportGenerator()
                pdf_bytes = report_generator.generate_report(
                    patient_data,
                    prediction_result,
                    recommendations
                )
                
                st.download_button(
                    label="📄 Save PDF Report",
                    data=pdf_bytes,
                    file_name=f"sleep_health_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
            except Exception as e:
                st.error(f"Error generating report: {str(e)}")
    
    with col2:
        if st.button("📊 View History", use_container_width=True):
            st.switch_page("pages/03_history.py")
    
    with col3:
        if st.button("🔄 New Assessment", use_container_width=True):
            st.session_state.patient_data = None
            st.session_state.prediction_result = None
            st.session_state.recommendations = None
            st.switch_page("pages/01_patient_details.py")
