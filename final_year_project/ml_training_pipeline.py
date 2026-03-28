import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
import joblib
import os
from datetime import datetime

class MLTrainingPipeline:
    """
    Complete ML Training Pipeline
    Trains and compares Logistic Regression, QDA, Random Forest, and Gradient Boosting
    """
    
    def __init__(self, data_csv_path):
        """
        Initialize training pipeline
        
        Args:
            data_csv_path: Path to CSV file with training data
        """
        self.data_path = data_csv_path
        self.models = {}
        self.results = {}
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.scaler = None
        self.feature_names = None
        self.model_names = [
            'Logistic Regression',
            'Quadratic Discriminant Analysis (QDA)',
            'Random Forest',
            'Gradient Boosting'
        ]
        
    def load_data(self):
        """Load and prepare training data"""
        print("Loading data...")
        df = pd.read_csv(self.data_path)
        
        # Separate features and target
        X = df.drop('target', axis=1)
        y = df['target']
        
        self.feature_names = X.columns.tolist()
        
        # Split data
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        
        # Scale features
        self.scaler = StandardScaler()
        self.X_train = self.scaler.fit_transform(self.X_train)
        self.X_test = self.scaler.transform(self.X_test)
        
        print(f"✓ Data loaded: {X.shape[0]} samples, {X.shape[1]} features")
        print(f"  Training set: {self.X_train.shape[0]} samples")
        print(f"  Test set: {self.X_test.shape[0]} samples")
        print(f"  Classes: {sorted(y.unique())}")
        
        return True
    
    def train_logistic_regression(self):
        """Train Logistic Regression model"""
        print("\n[1/4] Training Logistic Regression...")
        model = LogisticRegression(
            max_iter=1000,
            random_state=42,
            multi_class='multinomial',
            solver='lbfgs'
        )
        model.fit(self.X_train, self.y_train)
        self.models['Logistic Regression'] = model
        print("✓ Trained")
        return model
    
    def train_qda(self):
        """Train Quadratic Discriminant Analysis"""
        print("\n[2/4] Training Quadratic Discriminant Analysis (QDA)...")
        model = QuadraticDiscriminantAnalysis()
        model.fit(self.X_train, self.y_train)
        self.models['Quadratic Discriminant Analysis (QDA)'] = model
        print("✓ Trained")
        return model
    
    def train_random_forest(self):
        """Train Random Forest model"""
        print("\n[3/4] Training Random Forest...")
        model = RandomForestClassifier(
            n_estimators=100,
            max_depth=15,
            random_state=42,
            n_jobs=-1
        )
        model.fit(self.X_train, self.y_train)
        self.models['Random Forest'] = model
        print("✓ Trained")
        return model
    
    def train_gradient_boosting(self):
        """Train Gradient Boosting model"""
        print("\n[4/4] Training Gradient Boosting...")
        model = GradientBoostingClassifier(
            n_estimators=100,
            learning_rate=0.1,
            max_depth=5,
            random_state=42
        )
        model.fit(self.X_train, self.y_train)
        self.models['Gradient Boosting'] = model
        print("✓ Trained")
        return model
    
    def evaluate_model(self, model_name, model):
        """Evaluate single model"""
        y_pred = model.predict(self.X_test)
        
        results = {
            'model_name': model_name,
            'accuracy': accuracy_score(self.y_test, y_pred),
            'precision': precision_score(self.y_test, y_pred, average='weighted', zero_division=0),
            'recall': recall_score(self.y_test, y_pred, average='weighted', zero_division=0),
            'f1_score': f1_score(self.y_test, y_pred, average='weighted', zero_division=0),
            'y_pred': y_pred,
            'confusion_matrix': confusion_matrix(self.y_test, y_pred),
            'classification_report': classification_report(self.y_test, y_pred)
        }
        
        return results
    
    def train_all_models(self):
        """Train all models"""
        print("="*60)
        print("STARTING ML TRAINING PIPELINE")
        print("="*60)
        
        # Load data
        self.load_data()
        
        # Train all models
        self.train_logistic_regression()
        self.train_qda()
        self.train_random_forest()
        self.train_gradient_boosting()
        
        print("\n" + "="*60)
        print("MODEL EVALUATION")
        print("="*60)
        
        # Evaluate all models
        for model_name, model in self.models.items():
            results = self.evaluate_model(model_name, model)
            self.results[model_name] = results
            
            print(f"\n{model_name}:")
            print(f"  Accuracy:  {results['accuracy']:.4f}")
            print(f"  Precision: {results['precision']:.4f}")
            print(f"  Recall:    {results['recall']:.4f}")
            print(f"  F1-Score:  {results['f1_score']:.4f}")
        
        return self.results
    
    def get_best_model(self):
        """Get best performing model"""
        best_model_name = max(
            self.results.keys(),
            key=lambda x: self.results[x]['accuracy']
        )
        return best_model_name, self.results[best_model_name]
    
    def save_models(self, save_dir='models'):
        """Save all trained models and scaler"""
        os.makedirs(save_dir, exist_ok=True)
        
        # Save all models
        for model_name, model in self.models.items():
            safe_name = model_name.replace(' ', '_').replace('(', '').replace(')', '')
            path = os.path.join(save_dir, f'{safe_name}.joblib')
            joblib.dump(model, path)
            print(f"✓ Saved {model_name} to {path}")
        
        # Save scaler
        scaler_path = os.path.join(save_dir, 'scaler.joblib')
        joblib.dump(self.scaler, scaler_path)
        print(f"✓ Saved scaler to {scaler_path}")
        
        # Save results
        results_summary = {}
        for model_name, results in self.results.items():
            results_summary[model_name] = {
                'accuracy': float(results['accuracy']),
                'precision': float(results['precision']),
                'recall': float(results['recall']),
                'f1_score': float(results['f1_score'])
            }
        
        import json
        results_path = os.path.join(save_dir, 'training_results.json')
        with open(results_path, 'w') as f:
            json.dump(results_summary, f, indent=2)
        print(f"✓ Saved results to {results_path}")
    
    def get_summary(self):
        """Get training summary"""
        summary = {
            'timestamp': datetime.now().isoformat(),
            'total_samples': self.X_train.shape[0] + self.X_test.shape[0],
            'features': len(self.feature_names),
            'train_test_split': (len(self.X_train), len(self.X_test)),
            'models_trained': list(self.models.keys()),
            'results': {}
        }
        
        for model_name, results in self.results.items():
            summary['results'][model_name] = {
                'accuracy': round(results['accuracy'], 4),
                'precision': round(results['precision'], 4),
                'recall': round(results['recall'], 4),
                'f1_score': round(results['f1_score'], 4)
            }
        
        best_model_name, best_results = self.get_best_model()
        summary['best_model'] = {
            'name': best_model_name,
            'accuracy': round(best_results['accuracy'], 4)
        }
        
        return summary
    
    def print_summary(self):
        """Print training summary"""
        summary = self.get_summary()
        print("\n" + "="*60)
        print("TRAINING SUMMARY")
        print("="*60)
        print(f"Total Samples: {summary['total_samples']}")
        print(f"Features: {summary['features']}")
        print(f"Training Set: {summary['train_test_split'][0]} | Test Set: {summary['train_test_split'][1]}")
        print(f"\nBest Model: {summary['best_model']['name']} ({summary['best_model']['accuracy']:.4f} accuracy)")
        print("="*60)


# Example usage and training pipeline
if __name__ == "__main__":
    # Generate sample data if it doesn't exist
    csv_path = 'data/sleep_training_data.csv'
    
    if not os.path.exists(csv_path):
        print("Generating sample training data...")
        os.makedirs('data', exist_ok=True)
        
        # Create sample data
        np.random.seed(42)
        n_samples = 1000
        
        # Features
        X = pd.DataFrame({
            'gender': np.random.choice([0, 1], n_samples),
            'age': np.random.randint(18, 80, n_samples),
            'sleep_duration': np.random.uniform(2, 12, n_samples),
            'sleep_quality': np.random.randint(1, 11, n_samples),
            'stress_level': np.random.randint(1, 11, n_samples),
            'snoring_level': np.random.randint(1, 11, n_samples),
            'bmi_category': np.random.randint(0, 4, n_samples),
            'heart_rate': np.random.randint(50, 150, n_samples),
            'sbp': np.random.randint(90, 180, n_samples),
            'dbp': np.random.randint(60, 120, n_samples),
            'physical_activity': np.random.randint(0, 8, n_samples),
            'daily_steps': np.random.randint(0, 20000, n_samples),
            'oxygen_saturation': np.random.uniform(90, 100, n_samples),
        })
        
        # Create target based on features (simplified logic)
        y = np.zeros(n_samples, dtype=int)
        
        # Sleep Apnea: high BMI, snoring, low oxygen
        apnea_mask = (X['bmi_category'] >= 2) | (X['snoring_level'] > 6) | (X['oxygen_saturation'] < 96)
        y[apnea_mask] = 2
        
        # Insomnia: high stress, low quality, low duration
        insomnia_mask = (X['stress_level'] > 7) & (X['sleep_quality'] < 4) & (X['sleep_duration'] < 6) & (y == 0)
        y[insomnia_mask] = 1
        
        X['target'] = y
        X.to_csv(csv_path, index=False)
        print(f"✓ Sample data saved to {csv_path}")
    
    # Train pipeline
    pipeline = MLTrainingPipeline(csv_path)
    pipeline.train_all_models()
    pipeline.save_models()
    pipeline.print_summary()
