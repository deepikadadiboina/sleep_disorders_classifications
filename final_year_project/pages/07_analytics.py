import streamlit as st
import pandas as pd
import numpy as np
import os
from PIL import Image

st.set_page_config(
    page_title="Analytics - Sleep Health",
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
    
    .stat-box {
        background: linear-gradient(135deg, rgba(30, 58, 138, 0.15) 0%, rgba(15, 23, 42, 0.3) 100%);
        border: 1px solid rgba(59, 130, 246, 0.2);
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("# 📊 Analytics & Visualizations")
st.markdown("### Model Performance Analysis & Feature Importance")
st.markdown("---")

# Check if visualizations exist
viz_folder = os.path.join(os.path.dirname(__file__), 'models')

tab1, tab2, tab3, tab4 = st.tabs([
    "🎯 Model Accuracy",
    "⭐ Feature Importance",
    "🔲 Confusion Matrices",
    "📈 Metrics Comparison"
])

with tab1:
    st.markdown("## Model Accuracy Comparison")
    
    viz_path = os.path.join(viz_folder, 'model_accuracy_comparison.png')
    if os.path.exists(viz_path):
        image = Image.open(viz_path)
        st.image(image, use_column_width=True)
        st.markdown("""
        This chart compares the accuracy of all four trained algorithms:
        - **Logistic Regression**: Fast, interpretable baseline
        - **QDA**: Probabilistic approach with class-specific boundaries
        - **Random Forest**: Ensemble method with good generalization
        - **Gradient Boosting**: Advanced sequential learning
        """)
    else:
        st.info("📊 Visualization not generated yet. Run `ml_analytics.py` to generate.")

with tab2:
    st.markdown("## Feature Importance Analysis")
    
    viz_path = os.path.join(viz_folder, 'feature_importance.png')
    if os.path.exists(viz_path):
        image = Image.open(viz_path)
        st.image(image, use_column_width=True)
        st.markdown("""
        Feature importance shows which factors are most influential in predicting sleep disorders:
        
        **Top Factors:**
        - **Oxygen Saturation**: Critical indicator of breathing issues
        - **Sleep Duration**: Essential for sleep health assessment
        - **Snoring Level**: Key sign of potential sleep apnea
        - **Heart Rate**: Reflects cardiovascular stress during sleep
        - **Stress Level**: Major factor in insomnia development
        - **BMI**: Associated with sleep apnea risk
        """)
    else:
        st.info("📊 Visualization not generated yet. Run `ml_analytics.py` to generate.")

with tab3:
    st.markdown("## Confusion Matrices - All Models")
    
    viz_path = os.path.join(viz_folder, 'confusion_matrices.png')
    if os.path.exists(viz_path):
        image = Image.open(viz_path)
        st.image(image, use_column_width=True)
        st.markdown("""
        Confusion matrices show prediction accuracy for each sleep condition:
        - **Diagonal values**: Correct predictions
        - **Off-diagonal values**: Misclassified samples
        
        **Sleep Condition Labels:**
        - 0 = Normal Sleep
        - 1 = Insomnia
        - 2 = Sleep Apnea
        """)
    else:
        st.info("📊 Visualization not generated yet. Run `ml_analytics.py` to generate.")

with tab4:
    st.markdown("## Comprehensive Metrics Comparison")
    
    viz_path = os.path.join(viz_folder, 'metrics_comparison.png')
    if os.path.exists(viz_path):
        image = Image.open(viz_path)
        st.image(image, use_column_width=True)
        st.markdown("""
        Detailed comparison of all evaluation metrics:
        
        **Metrics Explained:**
        - **Accuracy**: Overall correctness of predictions
        - **Precision**: Correctness when predicting a specific condition
        - **Recall**: Ability to find all cases of a condition
        - **F1-Score**: Harmonic mean of precision and recall
        """)
    else:
        st.info("📊 Visualization not generated yet. Run `ml_analytics.py` to generate.")

st.markdown("---")

# Load training results if available
results_path = os.path.join(viz_folder, 'training_results.json')
if os.path.exists(results_path):
    import json
    with open(results_path, 'r') as f:
        results = json.load(f)
    
    st.markdown("## 🏆 Model Performance Summary")
    
    col1, col2, col3, col4 = st.columns(4)
    
    models_data = []
    for model_name, metrics in results.items():
        models_data.append({
            'Model': model_name,
            'Accuracy': metrics['accuracy'],
            'Precision': metrics['precision'],
            'Recall': metrics['recall'],
            'F1-Score': metrics['f1_score']
        })
    
    df = pd.DataFrame(models_data)
    
    # Display metrics
    for idx, row in df.iterrows():
        with [col1, col2, col3, col4][idx]:
            st.markdown(f"""
            <div class="stat-box">
                <h4 style="margin: 0; color: #e0f2fe;">{row['Model']}</h4>
                <div style="font-size: 1.8rem; color: #3b82f6; font-weight: bold; margin: 0.5rem 0;">
                    {row['Accuracy']:.2%}
                </div>
                <div style="font-size: 0.85rem; color: #94a3b8;">
                    Accuracy
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### Detailed Metrics Table")
    st.dataframe(df.round(4), use_container_width=True, hide_index=True)

else:
    st.warning("""
    ⚠️ No training results found.
    
    **To generate visualizations:**
    1. Generate training data: `python generate_training_data.py`
    2. Train models: `python ml_training_pipeline.py`
    3. Generate analytics: `python ml_analytics.py`
    4. Refresh this page
    """)

st.markdown("---")

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("app.py")
with col2:
    if st.button("🤖 ML Training", use_container_width=True):
        st.switch_page("pages/06_ml_training.py")
with col3:
    if st.button("👤 Assessment", use_container_width=True):
        st.switch_page("pages/01_patient_details.py")
