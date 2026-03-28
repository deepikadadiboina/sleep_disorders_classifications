import streamlit as st

st.set_page_config(
    page_title="Specifications - Sleep Health",
    page_icon="😴",
    layout="wide",
    initial_sidebar_state="collapsed"
)

#Styling
st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%);
        color: #f1f5f9;
    }
    
    .spec-box {
        background: linear-gradient(135deg, rgba(30, 58, 138, 0.15) 0%, rgba(15, 23, 42, 0.3) 100%);
        border-left: 4px solid #3b82f6;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("# 📋 Project Specifications")
st.markdown("### Software & Hardware Requirements")
st.markdown("---")

# Software Requirements
st.markdown("## 💻 Software Requirements")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="spec-box">
        <h3 style="color: #e0f2fe; margin-top: 0;">Operating System</h3>
        <p><strong>Windows 10+</strong> or macOS 10.14+ or Ubuntu 18.04+</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="spec-box">
        <h3 style="color: #e0f2fe; margin-top: 0;">Programming Language</h3>
        <p><strong>Python 3.11.4</strong> or higher</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="spec-box">
        <h3 style="color: #e0f2fe; margin-top: 0;">IDE / Editor</h3>
        <p><strong>Visual Studio Code</strong> (Recommended)<br/>
        Python 3.11+ extension installed</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="spec-box">
        <h3 style="color: #e0f2fe; margin-top: 0;">Core Libraries</h3>
        <ul style="color: #cbd5e1;">
            <li><strong>NumPy</strong> 1.24.3 - Numerical computing</li>
            <li><strong>Pandas</strong> 2.0.3 - Data manipulation</li>
            <li><strong>Scikit-learn</strong> 1.3.0 - Machine learning</li>
            <li><strong>SciPy</strong> - Scientific computing</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="spec-box">
        <h3 style="color: #e0f2fe; margin-top: 0;">Deep Learning & Visualization</h3>
        <ul style="color: #cbd5e1;">
            <li><strong>TensorFlow</strong> 2.13.0 - Deep learning</li>
            <li><strong>Keras</strong> - Neural networks API</li>
            <li><strong>Matplotlib</strong> 3.7.1 - Static plots</li>
            <li><strong>Seaborn</strong> 0.12.2 - Statistical visualization</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("### Frontend & Utilities")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="spec-box">
        <h3 style="color: #e0f2fe; margin-top: 0;">Frontend Framework</h3>
        <p><strong>Streamlit</strong> 1.28.1 - Web UI framework<br/>
        <strong>Streamlit Option Menu</strong> - Navigation<br/>
        <strong>Pillow</strong> 10.0.0 - Image processing</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="spec-box">
        <h3 style="color: #e0f2fe; margin-top: 0;">Utilities & Tools</h3>
        <p><strong>Joblib</strong> 1.3.1 - Model persistence<br/>
        <strong>ReportLab</strong> 4.0.4 - PDF generation<br/>
        <strong>Requests</strong> 2.31.0 - HTTP library</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Hardware Requirements
st.markdown("## ⚙️ Hardware Requirements")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="spec-box">
        <h3 style="color: #e0f2fe; margin-top: 0;">Processor</h3>
        <p style="font-size: 1.1rem; font-weight: bold; color: #3b82f6;">
            Intel i5 or equivalent
        </p>
        <p style="color: #cbd5e1; font-size: 0.9rem;">
            • Multi-core recommended<br/>
            • 2.5 GHz or higher<br/>
            • 64-bit processor
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="spec-box">
        <h3 style="color: #e0f2fe; margin-top: 0;">RAM</h3>
        <p style="font-size: 1.1rem; font-weight: bold; color: #3b82f6;">
            8 GB Minimum
        </p>
        <p style="color: #cbd5e1; font-size: 0.9rem;">
            • 16GB recommended<br/>
            • For smooth ML training<br/>
            • Better with more apps open
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="spec-box">
        <h3 style="color: #e0f2fe; margin-top: 0;">Storage</h3>
        <p style="font-size: 1.1rem; font-weight: bold; color: #3b82f6;">
            1 TB Hard Drive
        </p>
        <p style="color: #cbd5e1; font-size: 0.9rem;">
            • 500MB for application<br/>
            • Space for training data<br/>
            • Model storage (50-100MB)
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ML Algorithms Specification
st.markdown("## 🤖 Machine Learning Algorithms")

algo_specs = {
    'Logistic Regression': {
        'type': 'Linear Classification',
        'parameters': 'Max Iterations: 1000, Solver: LBFGS',
        'best_for': 'Baseline model, interpretability',
        'complexity': 'Low',
        'speed': 'Fast'
    },
    'Quadratic Discriminant Analysis (QDA)': {
        'type': 'Probabilistic Classification',
        'parameters': 'Class-specific covariance matrix',
        'best_for': 'Non-linear boundaries',
        'complexity': 'Medium',
        'speed': 'Fast'
    },
    'Random Forest': {
        'type': 'Ensemble (Bagging)',
        'parameters': 'Trees: 100, Max Depth: 15',
        'best_for': 'General-purpose, robustness',
        'complexity': 'High',
        'speed': 'Medium'
    },
    'Gradient Boosting': {
        'type': 'Ensemble (Boosting)',
        'parameters': 'Trees: 100, Learning Rate: 0.1',
        'best_for': 'Maximum accuracy, complex patterns',
        'complexity': 'Very High',
        'speed': 'Slow'
    }
}

tabs = st.tabs(list(algo_specs.keys()))

for tab, (algo, specs) in zip(tabs, algo_specs.items()):
    with tab:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            **Algorithm Type:** {specs['type']}
            
            **Parameters:**
            {specs['parameters']}
            
            **Best For:**
            {specs['best_for']}
            """)
        
        with col2:
            st.metric("Complexity", specs['complexity'])
            st.metric("Training Speed", specs['speed'])

st.markdown("---")

# Data Specifications
st.markdown("## 📊 Dataset Specifications")

st.markdown("""
<div class="spec-box">
    <h3 style="color: #e0f2fe; margin-top: 0;">Training Data</h3>
    <ul style="color: #cbd5e1;">
        <li><strong>Total Samples:</strong> 1000 records</li>
        <li><strong>Features:</strong> 13 health & lifestyle parameters</li>
        <li><strong>Train/Test Split:</strong> 80% / 20%</li>
        <li><strong>Target Classes:</strong> 3 (Normal Sleep, Insomnia, Sleep Apnea)</li>
        <li><strong>Data Format:</strong> CSV</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="spec-box">
    <h3 style="color: #e0f2fe; margin-top: 0;">Features (13 Input Parameters)</h3>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
        <div>
            <strong style="color: #bae6fd;">Demographic</strong>
            <ul style="color: #cbd5e1; font-size: 0.9rem;">
                <li>Gender (M/F)</li>
                <li>Age (18-85 years)</li>
            </ul>
        </div>
        <div>
            <strong style="color: #bae6fd;">Sleep Metrics</strong>
            <ul style="color: #cbd5e1; font-size: 0.9rem;">
                <li>Sleep Duration (2-12 hrs)</li>
                <li>Sleep Quality (1-10)</li>
            </ul>
        </div>
        <div>
            <strong style="color: #bae6fd;">Lifestyle</strong>
            <ul style="color: #cbd5e1; font-size: 0.9rem;">
                <li>Stress Level (1-10)</li>
                <li>Physical Activity (0-7 days)</li>
            </ul>
        </div>
        <div>
            <strong style="color: #bae6fd;">Health Metrics</strong>
            <ul style="color: #cbd5e1; font-size: 0.9rem;">
                <li>Heart Rate (50-150 bpm)</li>
                <li>Blood Pressure (SBP/DBP)</li>
            </ul>
        </div>
        <div>
            <strong style="color: #bae6fd;">Risk Indicators</strong>
            <ul style="color: #cbd5e1; font-size: 0.9rem;">
                <li>BMI Category (0-3)</li>
                <li>Snoring Level (1-10)</li>
            </ul>
        </div>
        <div>
            <strong style="color: #bae6fd;">Vital Signs</strong>
            <ul style="color: #cbd5e1; font-size: 0.9rem;">
                <li>Oxygen Saturation (90-100%)</li>
                <li>Daily Steps (0-20K+)</li>
            </ul>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Model Performance Targets
st.markdown("## 🎯 Performance Targets")

st.markdown("""
<div class="spec-box">
    <h3 style="color: #e0f2fe; margin-top: 0;">Expected Accuracy</h3>
    <ul style="color: #cbd5e1;">
        <li>Logistic Regression: 85-90%</li>
        <li>QDA: 90-92%</li>
        <li>Random Forest: 92-95%</li>
        <li>Gradient Boosting: 93-96%</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("app.py")
with col2:
    if st.button("📊 Analytics", use_container_width=True):
        st.switch_page("pages/07_analytics.py")
with col3:
    if st.button("🤖 ML Training", use_container_width=True):
        st.switch_page("pages/06_ml_training.py")
