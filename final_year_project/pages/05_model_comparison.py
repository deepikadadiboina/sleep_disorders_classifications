import streamlit as st
import json
import os
import pandas as pd

st.set_page_config(
    page_title="Model Comparison - Sleep Health",
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
    
    .metric-card {
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

st.markdown("# 🤖 Model Comparison")
st.markdown("### Compare Performance of Different ML Algorithms")
st.markdown("---")

# Load training results if available
results_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'training_results.json')

if os.path.exists(results_path):
    with open(results_path, 'r') as f:
        results = json.load(f)
    
    st.markdown("### 📊 Algorithm Performance Metrics")
    
    # Create comparison table
    comparison_data = []
    for model_name, metrics in results.items():
        comparison_data.append({
            'Model': model_name,
            'Accuracy': f"{metrics['accuracy']:.4f}",
            'Precision': f"{metrics['precision']:.4f}",
            'Recall': f"{metrics['recall']:.4f}",
            'F1-Score': f"{metrics['f1_score']:.4f}"
        })
    
    df_comparison = pd.DataFrame(comparison_data)
    st.dataframe(df_comparison, use_container_width=True)
    
    # Find best model
    best_model = max(results.items(), key=lambda x: x[1]['accuracy'])
    
    st.markdown("---")
    st.markdown("### 🏆 Best Performing Model")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Model", best_model[0])
    with col2:
        st.metric("Accuracy", f"{best_model[1]['accuracy']:.4f}")
    with col3:
        st.metric("Precision", f"{best_model[1]['precision']:.4f}")
    with col4:
        st.metric("F1-Score", f"{best_model[1]['f1_score']:.4f}")
    
    # Algorithm details
    st.markdown("---")
    st.markdown("### 📘 Algorithm Details")
    
    algo_info = {
        'Logistic Regression': """
        **Type:** Linear Classification
        **Pros:** Fast, interpretable, works well for linearly separable data
        **Cons:** May underfit complex relationships
        **Use Case:** Quick baseline model for binary/multiclass problems
        """,
        'Quadratic Discriminant Analysis (QDA)': """
        **Type:** Probabilistic Classification
        **Pros:** Handles non-linear boundaries, assumes class-specific covariance
        **Cons:** More parameters to estimate, sensitive to outliers
        **Use Case:** Good balance between Logistic Regression and complex models
        """,
        'Random Forest': """
        **Type:** Ensemble Learning (Bagging)
        **Pros:** Handles non-linearity, robust to outliers, provides feature importance
        **Cons:** Prone to overfitting, slower prediction
        **Use Case:** General-purpose powerful classifier
        """,
        'Gradient Boosting': """
        **Type:** Ensemble Learning (Boosting)
        **Pros:** Excellent predictive power, handles complex patterns, sequential learning
        **Cons:** Slow training, prone to overfitting without tuning, harder to interpret
        **Use Case:** Maximum accuracy needed, have time for training
        """
    }
    
    tabs = st.tabs(list(algo_info.keys()))
    for tab, (algo, info) in zip(tabs, algo_info.items()):
        with tab:
            st.markdown(info)

else:
    st.info("""
    📊 No trained models found yet.
    
    **Next Steps:**
    1. Generate training data: `python generate_training_data.py`
    2. Train models: `python ml_training_pipeline.py`
    3. Then return here to see comparison
    """)
    
    if st.button("Generate & Train Models"):
        import subprocess
        st.info("Starting training pipeline...")
        
        # Generate data
        subprocess.run(['python', 'generate_training_data.py'])
        # Train models
        subprocess.run(['python', 'ml_training_pipeline.py'])
        
        st.success("✓ Models trained! Refresh page to see results.")
        st.rerun()

st.markdown("---")

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("app.py")

with col2:
    if st.button("👤 Assessment", use_container_width=True):
        st.switch_page("pages/01_patient_details.py")

with col3:
    if st.button("📜 History", use_container_width=True):
        st.switch_page("pages/03_history.py")
