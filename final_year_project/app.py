import streamlit as st
from streamlit_option_menu import option_menu
import os

# ============================================================================
# PAGE CONFIG
# ============================================================================

st.set_page_config(
    page_title="Sleep Health - Professional Sleep Disorder Prediction",
    page_icon="😴",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# CUSTOM CSS STYLING
# ============================================================================

st.markdown("""
    <style>
    /* Global Styling */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%);
        color: #f1f5f9;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Streamlit specific */
    .main {
        padding: 2rem;
    }
    
    [data-testid="stMetric"] {
        background-color: rgba(30, 58, 138, 0.1);
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid #3b82f6;
    }
    
    /* Cards */
    .stContainer {
        background-color: rgba(30, 58, 138, 0.05);
        border-radius: 12px;
        padding: 1.5rem;
        border: 1px solid rgba(59, 130, 246, 0.2);
    }
    
    /* Buttons */
    .stButton > button {
        width: 100%;
        padding: 12px 24px;
        font-size: 16px;
        font-weight: 600;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
        transform: translateY(-2px);
        box-shadow: 0 8px 16px rgba(59, 130, 246, 0.3);
    }
    
    /* Input fields */
    .stTextInput input, .stNumberInput input, .stSelectbox select {
        background-color: rgba(15, 23, 42, 0.8) !important;
        border: 1px solid rgba(59, 130, 246, 0.3) !important;
        color: #f1f5f9 !important;
        border-radius: 8px !important;
        padding: 10px 12px !important;
    }
    
    .stSlider [data-baseweb="slider"] {
        background-color: #1e293b;
    }
    
    /* Headings */
    h1 {
        color: #f1f5f9;
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    h2 {
        color: #e0f2fe;
        font-size: 1.75rem;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #3b82f6;
        padding-bottom: 0.5rem;
    }
    
    h3 {
        color: #bae6fd;
        font-size: 1.25rem;
        margin-top: 1rem;
        margin-bottom: 0.75rem;
    }
    
    /* Text styling */
    p, .stMarkdown {
        color: #cbd5e1;
        line-height: 1.6;
    }
    
    .subtitle {
        font-size: 1.2rem;
        color: #94a3b8;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] button {
        color: #94a3b8;
        font-weight: 500;
    }
    
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
        color: #3b82f6;
        border-bottom: 2px solid #3b82f6;
    }
    
    /* Success/Error/Warning boxes */
    .stAlert {
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    /* Expander */
    [data-testid="stExpander"] {
        background-color: rgba(30, 58, 138, 0.1);
        border: 1px solid rgba(59, 130, 246, 0.2);
        border-radius: 8px;
    }
    
    /* Cards styling */
    .card {
        background: linear-gradient(135deg, rgba(30, 58, 138, 0.15) 0%, rgba(15, 23, 42, 0.3) 100%);
        border: 1px solid rgba(59, 130, 246, 0.2);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(10px);
    }
    
    /* Recommendation cards */
    .rec-card {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(30, 58, 138, 0.2) 100%);
        border-left: 4px solid #3b82f6;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    
    /* Metric boxes */
    .metric-box {
        background: rgba(30, 58, 138, 0.1);
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        border: 1px solid rgba(59, 130, 246, 0.2);
    }
    
    .metric-value {
        font-size: 1.8rem;
        font-weight: bold;
        color: #3b82f6;
        margin: 0.5rem 0;
    }
    
    .metric-label {
        color: #94a3b8;
        font-size: 0.9rem;
    }
    
    /* Loading animation */
    .loading {
        text-align: center;
        animation: pulse 1.5s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(15, 23, 42, 0.5);
    }
    
    ::-webkit-scrollbar-thumb {
        background: rgba(59, 130, 246, 0.5);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(59, 130, 246, 0.8);
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        h1 {
            font-size: 1.8rem;
        }
        
        h2 {
            font-size: 1.3rem;
        }
        
        .main {
            padding: 1rem;
        }
    }
    </style>
""", unsafe_allow_html=True)

# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if 'username' not in st.session_state:
    st.session_state.username = ''

if 'user_email' not in st.session_state:
    st.session_state.user_email = ''

if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {}

if 'patient_data' not in st.session_state:
    st.session_state.patient_data = None

if 'prediction_result' not in st.session_state:
    st.session_state.prediction_result = None

if 'recommendations' not in st.session_state:
    st.session_state.recommendations = None

if 'show_results' not in st.session_state:
    st.session_state.show_results = False

if 'page' not in st.session_state:
    st.session_state.page = 'Home'

# authentication helper

def require_login():
    if not st.session_state.get('logged_in', False):
        st.warning("⚠️ Please login to access this section.")
        if st.button("Go to Login"):
            st.switch_page("pages/00_login.py")
        st.stop()

# ============================================================================
# HOME PAGE (Default)
# ============================================================================

def render_home():
    """Render the home page"""
    
    # Hero section with gradient
    st.markdown("""
        <div style="text-align: center; padding: 3rem 0; margin-bottom: 2rem;">
            <h1 style="margin-bottom: 0; font-size: 3.5rem;">💤 Sleep Health</h1>
            <p style="font-size: 1.5rem; color: #94a3b8; margin: 1rem 0;">
                Understand Your Sleep. Improve Your Life.
            </p>
            <p style="font-size: 1rem; color: #cbd5e1; max-width: 600px; margin: 0 auto; line-height: 1.8;">
                Get personalized sleep insights backed by advanced machine learning analysis. 
                Understand your sleep patterns and receive actionable recommendations.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Get Started Button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Get Started", key="home_cta", use_container_width=True):
            st.switch_page("pages/01_patient_details.py")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Features Section
    st.markdown("""
        <h2 style="text-align: center; border: none; color: #e0f2fe; font-size: 1.8rem; margin-top: 2rem;">
            Why Sleep Matters
        </h2>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3, gap="large")
    
    with col1:
        st.markdown("""
        <div class="card" style="height: 100%;">
            <h3 style="text-align: center; margin-bottom: 1rem;">⚡ Detect Early</h3>
            <p style="text-align: center;">
                Identify sleep disorders early with AI-powered analysis for better outcomes.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card" style="height: 100%;">
            <h3 style="text-align: center; margin-bottom: 1rem;">🎯 Personalized</h3>
            <p style="text-align: center;">
                Get recommendations tailored specifically to your sleep profile and health metrics.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="card" style="height: 100%;">
            <h3 style="text-align: center; margin-bottom: 1rem;">📊 Track Progress</h3>
            <p style="text-align: center;">
                Monitor your sleep health over time with comprehensive history tracking.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Sleep Disorders Info
    st.markdown("""
        <h2 style="text-align: center; border: none; color: #e0f2fe; font-size: 1.8rem;">
            Sleep Conditions We Assess
        </h2>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs([
        "🟢 Normal Sleep",
        "🟡 Insomnia",
        "🔴 Sleep Apnea"
    ])
    
    with tab1:
        st.markdown("""
        #### Characteristics
        - Consistently sleeping 7-9 hours per night
        - Waking up feeling refreshed
        - No significant daytime sleepiness
        - Regular sleep schedule
        
        #### Recommendations
        - Maintain consistent sleep patterns
        - Exercise regularly (30 min, 5 days/week)
        - Limit screen time before bed
        - Stay hydrated and eat balanced meals
        """)
    
    with tab2:
        st.markdown("""
        #### Characteristics
        - Difficulty falling asleep
        - Frequent night time awakenings
        - Non-restorative sleep
        - Daytime fatigue and irritability
        
        #### Key Risk Factors
        - High stress and anxiety
        - Irregular sleep schedule
        - Poor sleep hygiene
        - Mental health conditions
        """)
    
    with tab3:
        st.markdown("""
        #### Characteristics
        - Loud snoring
        - Breathing pauses during sleep
        - Gasping for air
        - Excessive daytime sleepiness
        
        #### Key Risk Factors
        - Obesity
        - Anatomical abnormalities
        - Hypertension
        - Age and family history
        """)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # CTA Section
    st.markdown("""
        <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(30, 58, 138, 0.2) 100%); border-radius: 12px; margin-top: 2rem; border: 1px solid rgba(59, 130, 246, 0.3);">
            <h3 style="margin-bottom: 1rem; color: #e0f2fe;">Ready to Assess Your Sleep Health?</h3>
            <p style="margin-bottom: 1.5rem; color: #cbd5e1;">
                Start with a quick assessment. It takes less than 5 minutes.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Bottom CTA Button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Begin Assessment", key="home_bottom_cta", use_container_width=True):
            st.switch_page("pages/01_patient_details.py")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Quick Action Cards
    st.markdown("""
        <h2 style="text-align: center; border: none; color: #e0f2fe; font-size: 1.8rem; margin-top: 3rem;">
            🏥 Sleep Assessment Actions
        </h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <p style="text-align: center; color: #cbd5e1; margin: 1rem 0;">
        All features are focused on user input, prediction, history, and profile tracking.
    </p>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("""
        <div class="card" style="height: 100%;">
            <h3 style="text-align: center; margin-bottom: 1rem;">👤 Patient Details</h3>
            <p style="text-align: center;">
                Enter your sleep data and receive personalised sleep health predictions.
            </p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Go to Patient Details", key="patient_details_btn", use_container_width=True):
            st.switch_page("pages/01_patient_details.py")
    
    with col2:
        st.markdown("""
        <div class="card" style="height: 100%;">
            <h3 style="text-align: center; margin-bottom: 1rem;">📜 History</h3>
            <p style="text-align: center;">
                Review and track past sleep assessments and progress over time.
            </p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View History", key="history_btn", use_container_width=True):
            st.switch_page("pages/03_history.py")

# ============================================================================
# MAIN APP LOGIC
# ============================================================================

# Navigation sidebar
with st.sidebar:
    st.image("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ccircle cx='50' cy='50' r='45' fill='%233b82f6'/%3E%3Ctext x='50' y='65' font-size='50' text-anchor='middle' fill='white' font-family='Arial'%3E%F0%9F%98%B4%3C/text%3E%3C/svg%3E", width=80)
    
    if st.session_state.logged_in:
        st.markdown(f"**Logged in as:** {st.session_state.username}")
        if st.button("🚪 Logout"):
            st.session_state.logged_in = False
            st.session_state.username = ''
            st.session_state.user_email = ''
            st.session_state.user_profile = {}
            st.success("Logged out successfully")
            st.stop()
    else:
        if st.button("🔐 Login"):
            st.switch_page("pages/00_login.py")

    st.markdown("### 😴 Sleep Health")
    st.markdown("---")

    selected = option_menu(
        menu_title=None,
        options=["Home", "Patient Details", "Results", "History", "👤 Profile", "About", "Login"],
        icons=["house-fill", "person-vcard", "graph-up", "clock-history", "user-circle", "info-circle", "door-open"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#3b82f6", "font-size": "20px"},
            "nav-link": {
                "font-size": "14px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "rgba(59, 130, 246, 0.2)",
                "color": "#cbd5e1"
            },
            "nav-link-selected": {
                "background-color": "rgba(59, 130, 246, 0.3)",
                "color": "#3b82f6",
                "font-weight": "600"
            }
        }
    )
    st.session_state.page = selected

# Route to appropriate page
page = st.session_state.get('page', 'Home')

if page == "Home":
    render_home()
elif page == "Patient Details":
    st.switch_page("pages/01_patient_details.py")
elif page == "Results":
    st.switch_page("pages/02_results.py")
elif page == "History":
    st.switch_page("pages/03_history.py")
elif page == "👤 Profile":
    st.switch_page("pages/09_profile.py")
elif page == "About":
    st.switch_page("pages/04_about.py")
elif page == "Login":
    st.switch_page("pages/00_login.py")
