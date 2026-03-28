import streamlit as st

st.set_page_config(
    page_title="ML Training - Sleep Health",
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
    
    .code-block {
        background: rgba(30, 58, 138, 0.2);
        border-left: 4px solid #3b82f6;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
        font-family: 'Courier New', monospace;
        overflow-x: auto;
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

st.markdown("# 🧠 ML Training Pipeline")
st.markdown("### Generate Data & Train Multiple Algorithms")
st.markdown("---")

st.markdown("""
## How It Works

This Sleep Health application uses machine learning to predict sleep disorders by training multiple algorithms on your data:

1. **Logistic Regression** - Fast linear classifier
2. **Quadratic Discriminant Analysis (QDA)** - Probabilistic classifier
3. **Random Forest** - Powerful ensemble method
4. **Gradient Boosting** - Advanced sequential learning

### Training Process
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    #### 📊 Step 1: Data
    - Generate or load training data
    - 1000+ samples with 13 features
    - Train/test split: 80/20
    """)

with col2:
    st.markdown("""
    #### 🤖 Step 2: Training
    - Train all 4 algorithms
    - Feature scaling
    - Hyperparameter tuning
    """)

with col3:
    st.markdown("""
    #### 📈 Step 3: Evaluation
    - Compare accuracy
    - Calculate metrics
    - Select best model
    """)

st.markdown("---")

st.markdown("## Quick Start")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 1️⃣ Generate Training Data
    
    Creates a CSV file with 1000 realistic sleep disorder samples.
    """)
    
    if st.button("Generate Training Data", use_container_width=True):
        import subprocess
        st.info("Generating training data...")
        try:
            result = subprocess.run(
                ['python', 'generate_training_data.py'],
                capture_output=True,
                text=True,
                timeout=30
            )
            if result.returncode == 0:
                st.success("✓ Training data generated!")
                st.code(result.stdout)
            else:
                st.error(f"Error: {result.stderr}")
        except Exception as e:
            st.error(f"Error: {str(e)}")

with col2:
    st.markdown("""
    ### 2️⃣ Train All Models
    
    Trains Logistic Regression, QDA, Random Forest, and Gradient Boosting.
    """)
    
    if st.button("Train All Models", use_container_width=True):
        import subprocess
        st.info("Training models... This may take 1-2 minutes...")
        try:
            result = subprocess.run(
                ['python', 'ml_training_pipeline.py'],
                capture_output=True,
                text=True,
                timeout=300
            )
            if result.returncode == 0:
                st.success("✓ Models trained successfully!")
                st.code(result.stdout)
            else:
                st.error(f"Error: {result.stderr}")
        except Exception as e:
            st.error(f"Error: {str(e)}")

st.markdown("---")

st.markdown("## Manual Commands")

st.markdown("""
You can also run training manually from command line:

### Generate Data
```bash
python generate_training_data.py
```

### Train Models
```bash
python ml_training_pipeline.py
```

### Files Generated
- `data/sleep_training_data.csv` - Training dataset
- `models/Logistic_Regression.joblib` - Trained model
- `models/Quadratic_Discriminant_Analysis.joblib` - Trained model
- `models/Random_Forest.joblib` - Trained model
- `models/Gradient_Boosting.joblib` - Trained model
- `models/scaler.joblib` - Feature scaler
- `models/training_results.json` - Performance metrics
""")

st.markdown("---")

st.markdown("## Requirements")

st.markdown("""
Make sure these packages are installed:

```
scikit-learn ≥ 1.3.0
numpy ≥ 1.24.0
pandas ≥ 2.0.0
joblib ≥ 1.3.0
```

Install with:
```bash
pip install -r requirements.txt
```
""")

st.markdown("---")

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("app.py")

with col2:
    if st.button("🤖 Compare Models", use_container_width=True):
        st.switch_page("pages/05_model_comparison.py")

with col3:
    if st.button("👤 Assessment", use_container_width=True):
        st.switch_page("pages/01_patient_details.py")
