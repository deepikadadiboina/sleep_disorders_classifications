import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib
import os
import json

class SleepDisorderPredictor:
    """
    Sleep Disorder Prediction Model
    Supports multiple algorithms: Logistic Regression, QDA, Random Forest, Gradient Boosting
    """
    
    def __init__(self, model_name='Random Forest'):
        self.model = None
        self.scaler = None
        self.model_name = model_name
        self.available_models = [
            'Logistic Regression',
            'Quadratic Discriminant Analysis (QDA)',
            'Random Forest',
            'Gradient Boosting'
        ]
        self.classes = {0: "Normal Sleep", 1: "Insomnia", 2: "Sleep Apnea"}
        self.class_colors = {0: "🟢 Normal Sleep", 1: "🟡 Insomnia", 2: "🔴 Sleep Apnea"}
        self.risk_levels = {0: "Low", 1: "Medium", 2: "High"}
        self.risk_colors = {0: "#28a745", 1: "#ffc107", 2: "#dc3545"}
        self.model_metrics = {}
        self._initialize_model()
    
    def _initialize_model(self):
        """Initialize or load the model"""
        try:
            # Try to load trained models
            models_dir = os.path.join(os.path.dirname(__file__), '..', 'models')
            scaler_path = os.path.join(models_dir, 'scaler.joblib')
            
            if os.path.exists(models_dir):
                # Load specific model
                model_filename = self.model_name.replace(' ', '_').replace('(', '').replace(')', '') + '.joblib'
                model_path = os.path.join(models_dir, model_filename)
                
                if os.path.exists(model_path) and os.path.exists(scaler_path):
                    self.model = joblib.load(model_path)
                    self.scaler = joblib.load(scaler_path)
                    self._load_metrics()
                    return
            
            # Fallback: train a model
            self._train_model()
        except Exception as e:
            print(f"Error loading model: {e}")
            self._train_model()
    
    def _train_model(self):
        """Train a simple Random Forest model for demonstration"""
        import pandas as pd
        from sklearn.model_selection import train_test_split
        
        np.random.seed(42)
        n_samples = 1000
        
        # Create synthetic training data
        X = np.random.rand(n_samples, 13)
        
        # Scale features to realistic ranges
        X[:, 0] = np.random.choice([0, 1], n_samples)  # gender
        X[:, 1] = np.random.rand(n_samples) * 50 + 20  # age: 20-70
        X[:, 2] = np.random.rand(n_samples) * 8 + 4    # sleep_duration: 4-12 hours
        X[:, 3] = np.random.rand(n_samples) * 10       # sleep_quality: 0-10
        X[:, 4] = np.random.rand(n_samples) * 10       # stress_level: 0-10
        X[:, 5] = np.random.rand(n_samples) * 10       # snoring_level: 0-10
        X[:, 6] = np.random.choice([0, 1, 2, 3], n_samples)  # BMI
        X[:, 7] = np.random.rand(n_samples) * 80 + 60  # heart_rate: 60-140
        X[:, 8] = np.random.rand(n_samples) * 60 + 100 # SBP: 100-160
        X[:, 9] = np.random.rand(n_samples) * 40 + 60  # DBP: 60-100
        X[:, 10] = np.random.rand(n_samples) * 5       # physical_activity: 0-5 days
        X[:, 11] = np.random.rand(n_samples) * 20000 + 3000  # daily_steps: 3000-23000
        X[:, 12] = np.random.rand(n_samples) * 5 + 95  # oxygen_saturation: 95-100%
        
        # Create intelligent labels
        y = np.zeros(n_samples, dtype=int)
        
        # Sleep Apnea: high BMI, snoring, low oxygen
        apnea_mask = (X[:, 6] >= 2) | (X[:, 5] > 6) | (X[:, 12] < 96)
        y[apnea_mask] = 2
        
        # Insomnia: high stress, low quality, low duration
        insomnia_mask = (X[:, 4] > 7) & (X[:, 3] < 4) & (X[:, 2] < 6) & (y == 0)
        y[insomnia_mask] = 1
        
        # Train model
        self.scaler = StandardScaler()
        X_scaled = self.scaler.fit_transform(X)
        
        self.model = RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            random_state=42,
            n_jobs=-1
        )
        self.model.fit(X_scaled, y)
        
        # Save model
        os.makedirs(os.path.join(os.path.dirname(__file__), '..', 'models'), exist_ok=True)
        model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'sleep_model.joblib')
        scaler_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'scaler.joblib')
        joblib.dump(self.model, model_path)
        joblib.dump(self.scaler, scaler_path)
    
    def _load_metrics(self):
        """Load model metrics if available"""
        try:
            metrics_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'training_results.json')
            if os.path.exists(metrics_path):
                with open(metrics_path, 'r') as f:
                    self.model_metrics = json.load(f)
        except:
            pass
    
    def switch_model(self, model_name):
        """Switch to a different trained model"""
        if model_name not in self.available_models:
            raise ValueError(f"Model {model_name} not available")
        
        self.model_name = model_name
        self._initialize_model()
    
    def get_available_models(self):
        """Get list of available models"""
        return self.available_models
    
    def get_model_metrics(self):
        """Get metrics for current model"""
        if self.model_name in self.model_metrics:
            return self.model_metrics[self.model_name]
        return None
    
    def predict(self, patient_data):
        """
        Make prediction for patient
        
        Args:
            patient_data: dict with keys:
                - gender (0=Male, 1=Female)
                - age
                - sleep_duration
                - sleep_quality
                - stress_level
                - snoring_level
                - bmi_category
                - heart_rate
                - sbp
                - dbp
                - physical_activity
                - daily_steps
                - oxygen_saturation
        
        Returns:
            dict with prediction, risk level, confidence
        """
        features = np.array([
            patient_data['gender'],
            patient_data['age'],
            patient_data['sleep_duration'],
            patient_data['sleep_quality'],
            patient_data['stress_level'],
            patient_data['snoring_level'],
            patient_data['bmi_category'],
            patient_data['heart_rate'],
            patient_data['sbp'],
            patient_data['dbp'],
            patient_data['physical_activity'],
            patient_data['daily_steps'],
            patient_data['oxygen_saturation']
        ]).reshape(1, -1)
        
        X_scaled = self.scaler.transform(features)
        
        # Get prediction and probabilities
        prediction = self.model.predict(X_scaled)[0]
        probabilities = self.model.predict_proba(X_scaled)[0]
        confidence = float(probabilities[prediction]) * 100
        
        # Calculate risk level
        if prediction == 0:  # Normal Sleep
            risk_level = 0
        elif prediction == 1:  # Insomnia
            # Risk based on stress and sleep quality
            stress_factor = min(patient_data['stress_level'] / 10.0, 1.0)
            quality_factor = (10 - patient_data['sleep_quality']) / 10.0
            avg_risk = (stress_factor + quality_factor) / 2.0
            risk_level = 1 if avg_risk < 0.6 else (2 if avg_risk > 0.8 else 1)
        else:  # Sleep Apnea
            # Risk based on BMI, snoring, oxygen saturation
            bmi_factor = patient_data['bmi_category'] / 3.0
            snoring_factor = min(patient_data['snoring_level'] / 10.0, 1.0)
            oxygen_factor = max(0, (100 - patient_data['oxygen_saturation']) / 5.0)
            avg_risk = (bmi_factor + snoring_factor + oxygen_factor) / 3.0
            risk_level = 1 if avg_risk < 0.4 else (2 if avg_risk > 0.7 else 1)
        
        return {
            'prediction': self.classes[prediction],
            'prediction_short': prediction,
            'risk_level': self.risk_levels[min(risk_level, 2)],
            'risk_numeric': min(risk_level, 2),
            'confidence': confidence,
            'emoji': self.class_colors[prediction],
            'color': self.risk_colors[min(risk_level, 2)]
        }
    
    def get_recommendations(self, patient_data, prediction_result):
        """
        Generate personalized recommendations based on prediction
        """
        recommendations = {
            'lifestyle': [],
            'sleep_habits': [],
            'medical_advice': []
        }
        
        prediction = prediction_result['prediction_short']
        
        if prediction == 0:  # Normal Sleep
            recommendations['lifestyle'].append("Continue your current exercise routine - it's helping!")
            recommendations['lifestyle'].append("Maintain a balanced diet rich in magnesium")
            recommendations['sleep_habits'].append("Keep your consistent sleep schedule")
            recommendations['sleep_habits'].append("Avoid screens 30 minutes before bed")
            recommendations['medical_advice'].append("Annual health check-ups are recommended")
            recommendations['medical_advice'].append("Monitor your vital signs regularly")
        
        elif prediction == 1:  # Insomnia
            if patient_data['stress_level'] > 6:
                recommendations['lifestyle'].append("Practice daily meditation or yoga (15-20 min)")
                recommendations['lifestyle'].append("Reduce caffeine intake, especially after 2 PM")
            
            recommendations['sleep_habits'].append("Maintain consistent sleep and wake times")
            recommendations['sleep_habits'].append("Create a bedtime routine 30 minutes before sleep")
            
            if patient_data['sleep_duration'] < 6:
                recommendations['medical_advice'].append("Consult a sleep specialist - sleep deprivation detected")
            else:
                recommendations['medical_advice'].append("Consider cognitive behavioral therapy for insomnia")
            
            recommendations['medical_advice'].append("Avoid alcohol and heavy meals before bed")
        
        else:  # Sleep Apnea
            if patient_data['bmi_category'] >= 2:
                recommendations['lifestyle'].append("Gradual weight loss program (consult nutritionist)")
                recommendations['lifestyle'].append("Increase daily physical activity to 30 minutes")
            
            recommendations['sleep_habits'].append("Sleep on your side, not your back")
            recommendations['sleep_habits'].append("Use humidifier to keep airways moist")
            
            recommendations['medical_advice'].append("⚠️ URGENT: Consult a sleep specialist immediately")
            recommendations['medical_advice'].append("Consider CPAP therapy evaluation")
            recommendations['medical_advice'].append("Monitor oxygen saturation levels regularly")
        
        # Add general recommendations
        if patient_data['physical_activity'] < 3:
            if prediction == 1:
                recommendations['lifestyle'].append("Increase physical activity to 150 min/week")
        
        if patient_data['heart_rate'] > 90:
            recommendations['medical_advice'].append("Monitor blood pressure and heart rate")
        
        return recommendations


# Initialize predictor
predictor = SleepDisorderPredictor()
