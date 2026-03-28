import streamlit as st

st.set_page_config(
    page_title="About - Sleep Health",
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
    
    .info-card {
        background: linear-gradient(135deg, rgba(30, 58, 138, 0.15) 0%, rgba(15, 23, 42, 0.3) 100%);
        border: 1px solid rgba(59, 130, 246, 0.2);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
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

st.markdown("# ℹ️ About Sleep Health")
st.markdown("---")

st.markdown("""
### Welcome to Sleep Health

Sleep Health is a professional healthcare application designed to help you understand your sleep patterns 
and identify potential sleep disorders early.

""")

# About the Application
st.markdown("""
#### 🎯 Our Mission

To provide an accessible, AI-powered sleep assessment tool that helps individuals:
- Understand their sleep quality and patterns
- Identify early signs of sleep disorders
- Receive personalized health recommendations
- Track their sleep health over time

""")

st.markdown("""
<div class="info-card">
    <h3 style="color: #e0f2fe; margin-top: 0;">🔬 How It Works</h3>
    <p>Sleep Health uses advanced machine learning algorithms to analyze your:</p>
    <ul style="color: #cbd5e1;">
        <li><strong>Sleep Habits</strong>: Duration, quality, and sleep patterns</li>
        <li><strong>Health Metrics</strong>: Heart rate, blood pressure, oxygen saturation</li>
        <li><strong>Lifestyle Factors</strong>: Physical activity, stress levels, daily habits</li>
        <li><strong>Risk Indicators</strong>: Snoring, BMI category, and other relevant data</li>
    </ul>
    <p style="margin-top: 1rem; color: #94a3b8; font-size: 0.9rem;">
        Our model analyzes these factors to provide a comprehensive assessment of your sleep health.
    </p>
</div>
""", unsafe_allow_html=True)

# Sleep Disorders Overview
st.markdown("#### 😴 Sleep Disorders We Assess")

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown("""
    <div class="info-card" style="height: 100%;">
        <h4 style="color: #28a745;">🟢 Normal Sleep</h4>
        <p>Healthy sleep patterns with 7-9 hours nightly, good daytime functioning, and no significant sleep disruptions.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card" style="height: 100%;">
        <h4 style="color: #ffc107;">🟡 Insomnia</h4>
        <p>Difficulty falling or staying asleep, non-restorative sleep, and daytime impairment despite adequate sleep opportunity.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="info-card" style="height: 100%;">
        <h4 style="color: #dc3545;">🔴 Sleep Apnea</h4>
        <p>Repeated breathing interruptions during sleep, often accompanied by snoring and excessive daytime sleepiness.</p>
    </div>
    """, unsafe_allow_html=True)

# Privacy & Disclaimer
st.markdown("""
---

#### 🔐 Privacy & Data Security

- Your assessment data is processed locally on your device
- No data is stored on external servers
- Your personal information is never shared with third parties
- Assessment history is stored locally on your device only

""")

st.markdown("""
#### ⚠️ Medical Disclaimer

**Important**: Sleep Health is designed for informational and educational purposes only. 
It is not a substitute for professional medical advice, diagnosis, or treatment.

- Results are based on machine learning analysis, not clinical diagnosis
- Always consult a healthcare professional for medical concerns
- If you experience severe sleep issues, please seek immediate medical attention
- For urgent concerns about your sleep, contact a sleep specialist

""")

# Features
st.markdown("""
<div class="info-card">
    <h3 style="color: #e0f2fe; margin-top: 0;">✨ Key Features</h3>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 1rem;">
        <div>
            <p style="color: #bae6fd; font-weight: 600;">⚡ Real-Time Analysis</p>
            <p style="color: #cbd5e1; font-size: 0.9rem;">Get instant assessment results based on your health data</p>
        </div>
        <div>
            <p style="color: #bae6fd; font-weight: 600;">🎯 Personalized Recommendations</p>
            <p style="color: #cbd5e1; font-size: 0.9rem;">Tailored suggestions based on your specific sleep profile</p>
        </div>
        <div>
            <p style="color: #bae6fd; font-weight: 600;">📥 PDF Reports</p>
            <p style="color: #cbd5e1; font-size: 0.9rem;">Download comprehensive health reports to share with doctors</p>
        </div>
        <div>
            <p style="color: #bae6fd; font-weight: 600;">📊 History Tracking</p>
            <p style="color: #cbd5e1; font-size: 0.9rem;">Track your sleep health improvements over time</p>
        </div>
        <div>
            <p style="color: #bae6fd; font-weight: 600;">📱 Responsive Design</p>
            <p style="color: #cbd5e1; font-size: 0.9rem;">Works seamlessly on all devices</p>
        </div>
        <div>
            <p style="color: #bae6fd; font-weight: 600;">🔒 Privacy Focused</p>
            <p style="color: #cbd5e1; font-size: 0.9rem;">Your data stays with you, never sent to servers</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Technology Stack
st.markdown("""
<div class="info-card">
    <h3 style="color: #e0f2fe; margin-top: 0;">🛠️ Technology Stack</h3>
    <ul style="color: #cbd5e1;">
        <li><strong>Frontend</strong>: Streamlit (Python web framework)</li>
        <li><strong>Machine Learning</strong>: Scikit-learn, TensorFlow</li>
        <li><strong>Data Processing</strong>: NumPy, Pandas</li>
        <li><strong>Report Generation</strong>: ReportLab (PDF)</li>
        <li><strong>Environment</strong>: Python 3.11+</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Contact & Support
st.markdown("""

#### 📧 Support & Feedback

For questions or feedback about Sleep Health:
- Report issues or suggest features
- Contact us through the support channel
- Your feedback helps us improve

---

#### 🎓 Educational Purpose

Sleep Health was developed as a final year project to demonstrate:
- Machine Learning applications in healthcare
- Full-stack web application development
- Professional UI/UX design principles
- Real-world healthcare product development

---

**Version**: 1.0.0  
**Last Updated**: March 2026  
**Status**: Active Development

Happy sleeping! 😴
""")

st.markdown("---")

col1, col2, col3 = st.columns([1, 1, 1], gap="medium")

with col1:
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("app.py")

with col2:
    if st.button("🔄 Start Assessment", use_container_width=True):
        st.session_state.patient_data = None
        st.session_state.prediction_result = None
        st.session_state.recommendations = None
        st.switch_page("pages/01_patient_details.py")

with col3:
    if st.button("📜 View History", use_container_width=True):
        st.switch_page("pages/03_history.py")
