import streamlit as st
from utils.history import HistoryManager

st.set_page_config(
    page_title="History - Sleep Health",
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
    
    .history-card {
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
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
    }
    </style>
""", unsafe_allow_html=True)

# Require login for history page
if not st.session_state.get('logged_in', False):
    st.warning("⚠️ Please login first to view your history.")
    if st.button("Go to Login"):
        st.switch_page("pages/00_login.py")
    st.stop()

st.markdown("# 📜 Assessment History")
st.markdown("### View your past sleep assessments and track improvements")
st.markdown("---")

history_manager = HistoryManager()
history = history_manager.load_user_history(st.session_state.username)

if not history:
    st.info("""
    📋 No assessment history yet.
    
    Start by completing your first sleep assessment to see your history here.
    """)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Begin First Assessment", use_container_width=True):
            st.switch_page("pages/01_patient_details.py")

else:
    # Summary Stats
    col1, col2, col3 = st.columns(3, gap="medium")
    
    # Count by prediction
    predictions = {}
    for entry in history:
        pred = entry['prediction']
        predictions[pred] = predictions.get(pred, 0) + 1
    
    most_common = max(predictions, key=predictions.get) if predictions else "N/A"
    high_risk_count = sum(1 for entry in history if entry['risk_level'] in ['High', 'Medium'])
    
    with col1:
        st.markdown(f"""
        <div style="text-align: center; padding: 1.5rem; background: rgba(30, 58, 138, 0.2); border-radius: 12px;">
            <div style="font-size: 2rem; font-weight: bold; color: #3b82f6;">{len(history)}</div>
            <div style="color: #94a3b8; font-size: 0.9rem;">Total Assessments</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="text-align: center; padding: 1.5rem; background: rgba(30, 58, 138, 0.2); border-radius: 12px;">
            <div style="font-size: 1.8rem;">{most_common}</div>
            <div style="color: #94a3b8; font-size: 0.9rem;">Most Common</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style="text-align: center; padding: 1.5rem; background: rgba(30, 58, 138, 0.2); border-radius: 12px;">
            <div style="font-size: 2rem; font-weight: bold; color: #ffc107;">{high_risk_count}</div>
            <div style="color: #94a3b8; font-size: 0.9rem;">Medium/High Risk</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Timeline
    st.markdown("### 📅 Assessment Timeline")
    
    for entry in reversed(history):  # Show newest first
        prediction = entry['prediction']
        risk_level = entry['risk_level']
        date = entry['date']
        time = entry['time']
        confidence = entry['confidence']
        
        # Color coding
        color_map = {
            "Normal Sleep": "#28a745",
            "Insomnia": "#ffc107",
            "Sleep Apnea": "#dc3545"
        }
        emoji_map = {
            "Normal Sleep": "🟢",
            "Insomnia": "🟡",
            "Sleep Apnea": "🔴"
        }
        
        color = color_map.get(prediction, "#3b82f6")
        emoji = emoji_map.get(prediction, "❓")
        
        st.markdown(f"""
        <div class="history-card">
            <div style="display: flex; justify-content: space-between; align-items: start;">
                <div>
                    <div style="font-size: 1.1rem; margin-bottom: 0.5rem;">
                        <strong>{emoji} {prediction}</strong>
                    </div>
                    <div style="color: #94a3b8; font-size: 0.9rem; margin-bottom: 0.5rem;">
                        {date} at {time}
                    </div>
                    <div style="display: flex; gap: 1rem; margin-top: 0.75rem;">
                        <span style="background: {color}22; color: {color}; padding: 0.4rem 0.8rem; border-radius: 6px; font-size: 0.85rem;">
                            Risk: {risk_level}
                        </span>
                        <span style="background: #3b82f655; color: #bae6fd; padding: 0.4rem 0.8rem; border-radius: 6px; font-size: 0.85rem;">
                            Confidence: {confidence}%
                        </span>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Actions
    col1, col2, col3 = st.columns([1, 1, 1], gap="medium")
    
    with col1:
        if st.button("➕ New Assessment", use_container_width=True):
            st.session_state.patient_data = None
            st.session_state.prediction_result = None
            st.session_state.recommendations = None
            st.switch_page("pages/01_patient_details.py")
    
    with col2:
        if st.button("🏠 Home", use_container_width=True):
            st.switch_page("app.py")
    
    with col3:
        confirm_delete = st.checkbox("Confirm delete all my history", key="confirm_delete")
        if st.button("🗑️ Clear History", use_container_width=True):
            if confirm_delete:
                history_manager.clear_history(st.session_state.username)
                st.success("✅ Your history was cleared.")
                st.switch_page("pages/03_history.py")
            else:
                st.error("Please check the confirmation checkbox before deleting history.")
