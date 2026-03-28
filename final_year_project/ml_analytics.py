import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import os
import json

class ModelAnalyticsGenerator:
    """Generate visualizations and analytics for ML models"""
    
    def __init__(self, data_path):
        self.data_path = data_path
        self.models = {}
        self.results = {}
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.feature_names = None
        
    def load_data(self):
        """Load training data"""
        df = pd.read_csv(self.data_path)
        X = df.drop('target', axis=1)
        y = df['target']
        
        self.feature_names = X.columns.tolist()
        
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        
        scaler = StandardScaler()
        self.X_train = scaler.fit_transform(self.X_train)
        self.X_test = scaler.transform(self.X_test)
        
    def train_models(self):
        """Train all models"""
        self.models['Logistic Regression'] = LogisticRegression(
            max_iter=1000, random_state=42, multi_class='multinomial'
        ).fit(self.X_train, self.y_train)
        
        self.models['QDA'] = QuadraticDiscriminantAnalysis().fit(
            self.X_train, self.y_train
        )
        
        self.models['Random Forest'] = RandomForestClassifier(
            n_estimators=100, max_depth=15, random_state=42, n_jobs=-1
        ).fit(self.X_train, self.y_train)
        
        self.models['Gradient Boosting'] = GradientBoostingClassifier(
            n_estimators=100, learning_rate=0.1, max_depth=5, random_state=42
        ).fit(self.X_train, self.y_train)
    
    def evaluate_models(self):
        """Evaluate all models"""
        for model_name, model in self.models.items():
            y_pred = model.predict(self.X_test)
            self.results[model_name] = {
                'accuracy': accuracy_score(self.y_test, y_pred),
                'model': model
            }
    
    def plot_model_accuracy_comparison(self, output_path='models/model_accuracy_comparison.png'):
        """Create model accuracy comparison chart"""
        os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
        
        models = list(self.results.keys())
        accuracies = [self.results[m]['accuracy'] for m in models]
        
        # Create figure with professional styling
        fig, ax = plt.subplots(figsize=(10, 6))
        fig.patch.set_facecolor('white')
        
        # Color palette
        colors = ['#1f77b4', '#2ca02c', '#d62728', '#ff7f0e']
        
        bars = ax.bar(models, accuracies, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
        
        # Styling
        ax.set_ylabel('Accuracy (%)', fontsize=12, fontweight='bold')
        ax.set_title('Model Accuracy Comparison', fontsize=14, fontweight='bold', pad=20)
        ax.set_ylim([0.85, 1.0])
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        ax.set_axisbelow(True)
        
        # Add value labels on bars
        for bar, acc in zip(bars, accuracies):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{acc:.2%}',
                   ha='center', va='bottom', fontweight='bold', fontsize=11)
        
        # Rotate x labels
        ax.set_xticklabels(models, rotation=15, ha='right')
        
        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"✓ Saved: {output_path}")
        plt.close()
    
    def plot_feature_importance(self, output_path='models/feature_importance.png'):
        """Create feature importance chart for Random Forest"""
        os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
        
        rf_model = self.models['Random Forest']
        importances = rf_model.feature_importances_
        
        # Create DataFrame for sorting
        importance_df = pd.DataFrame({
            'feature': self.feature_names,
            'importance': importances
        }).sort_values('importance', ascending=True)
        
        # Create figure
        fig, ax = plt.subplots(figsize=(10, 7))
        fig.patch.set_facecolor('white')
        
        # Create horizontal bar chart
        colors_grad = plt.cm.viridis(np.linspace(0.3, 0.9, len(importance_df)))
        bars = ax.barh(importance_df['feature'], importance_df['importance'], 
                       color=colors_grad, edgecolor='black', linewidth=1.2)
        
        # Styling
        ax.set_xlabel('Feature Importance Score', fontsize=12, fontweight='bold')
        ax.set_title('Feature Importance for Sleep Disorder Prediction', 
                    fontsize=14, fontweight='bold', pad=20)
        ax.grid(axis='x', alpha=0.3, linestyle='--')
        ax.set_axisbelow(True)
        
        # Add value labels
        for i, (bar, val) in enumerate(zip(bars, importance_df['importance'])):
            ax.text(val, bar.get_y() + bar.get_height()/2,
                   f'{val:.3f}',
                   ha='left', va='center', fontweight='bold', fontsize=9, 
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.3))
        
        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"✓ Saved: {output_path}")
        plt.close()
        
        return importance_df
    
    def plot_confusion_matrices(self, output_path='models/confusion_matrices.png'):
        """Create confusion matrix for all models"""
        os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
        
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        fig.patch.set_facecolor('white')
        fig.suptitle('Confusion Matrices - All Models', fontsize=14, fontweight='bold', y=1.00)
        
        axes = axes.ravel()
        
        for idx, (model_name, model) in enumerate(self.models.items()):
            y_pred = model.predict(self.X_test)
            cm = confusion_matrix(self.y_test, y_pred)
            
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[idx],
                       cbar_kws={'label': 'Count'})
            axes[idx].set_title(f'{model_name} (Acc: {self.results[model_name]["accuracy"]:.2%})',
                              fontweight='bold')
            axes[idx].set_ylabel('True Label')
            axes[idx].set_xlabel('Predicted Label')
        
        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"✓ Saved: {output_path}")
        plt.close()
    
    def plot_metrics_comparison(self, output_path='models/metrics_comparison.png'):
        """Create detailed metrics comparison"""
        os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
        
        from sklearn.metrics import precision_score, recall_score, f1_score
        
        metrics_data = []
        
        for model_name, model in self.models.items():
            y_pred = model.predict(self.X_test)
            
            metrics_data.append({
                'Model': model_name,
                'Accuracy': accuracy_score(self.y_test, y_pred),
                'Precision': precision_score(self.y_test, y_pred, average='weighted', zero_division=0),
                'Recall': recall_score(self.y_test, y_pred, average='weighted', zero_division=0),
                'F1-Score': f1_score(self.y_test, y_pred, average='weighted', zero_division=0)
            })
        
        df_metrics = pd.DataFrame(metrics_data)
        df_metrics_melted = df_metrics.melt(id_vars='Model', var_name='Metric', value_name='Score')
        
        # Create figure
        fig, ax = plt.subplots(figsize=(12, 6))
        fig.patch.set_facecolor('white')
        
        # Create grouped bar chart
        metric_names = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
        model_names = df_metrics['Model'].tolist()
        x = np.arange(len(metric_names))
        width = 0.2
        
        colors = ['#1f77b4', '#2ca02c', '#d62728', '#ff7f0e']
        
        for i, model_name in enumerate(model_names):
            model_metrics = df_metrics[df_metrics['Model'] == model_name][
                ['Accuracy', 'Precision', 'Recall', 'F1-Score']
            ].values[0]
            
            ax.bar(x + i*width, model_metrics, width, label=model_name, 
                  color=colors[i], alpha=0.8, edgecolor='black', linewidth=1)
        
        # Styling
        ax.set_ylabel('Score', fontsize=12, fontweight='bold')
        ax.set_title('Comprehensive Metrics Comparison', fontsize=14, fontweight='bold', pad=20)
        ax.set_xticks(x + width * 1.5)
        ax.set_xticklabels(metric_names)
        ax.legend(loc='lower right', framealpha=0.9)
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        ax.set_axisbelow(True)
        ax.set_ylim([0.8, 1.0])
        
        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"✓ Saved: {output_path}")
        plt.close()
    
    def generate_all_visualizations(self):
        """Generate all visualizations"""
        print("Loading data...")
        self.load_data()
        
        print("Training models...")
        self.train_models()
        
        print("Evaluating models...")
        self.evaluate_models()
        
        print("\nGenerating visualizations...")
        self.plot_model_accuracy_comparison()
        self.plot_feature_importance()
        self.plot_confusion_matrices()
        self.plot_metrics_comparison()
        
        print("\n✓ All visualizations generated successfully!")


if __name__ == "__main__":
    csv_path = 'data/sleep_training_data.csv'
    
    if os.path.exists(csv_path):
        analytics = ModelAnalyticsGenerator(csv_path)
        analytics.generate_all_visualizations()
    else:
        print("Training data not found. Run generate_training_data.py first.")
