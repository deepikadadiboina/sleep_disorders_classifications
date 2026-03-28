import pandas as pd
import numpy as np
import os

def generate_sleep_training_data(n_samples=1000, output_path='data/sleep_training_data.csv'):
    """
    Generate realistic sleep disorder training data
    
    Returns DataFrame with 13 features + target variable
    Target: 0=Normal Sleep, 1=Insomnia, 2=Sleep Apnea
    """
    
    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
    
    np.random.seed(42)
    
    print(f"Generating {n_samples} training samples...")
    
    data = {
        'gender': np.random.choice([0, 1], n_samples, p=[0.5, 0.5]),  # 0=Male, 1=Female
        'age': np.random.normal(45, 15, n_samples).astype(int).clip(18, 85),
        'sleep_duration': np.random.normal(7, 1.5, n_samples).clip(2, 12),
        'sleep_quality': np.random.randint(1, 11, n_samples),
        'stress_level': np.random.randint(1, 11, n_samples),
        'snoring_level': np.random.randint(1, 11, n_samples),
        'bmi_category': np.random.choice([0, 1, 2, 3], n_samples, p=[0.15, 0.45, 0.25, 0.15]),
        'heart_rate': np.random.normal(75, 15, n_samples).astype(int).clip(50, 150),
        'sbp': np.random.normal(120, 15, n_samples).astype(int).clip(90, 180),
        'dbp': np.random.normal(80, 10, n_samples).astype(int).clip(60, 120),
        'physical_activity': np.random.randint(0, 8, n_samples),
        'daily_steps': np.random.normal(8000, 4000, n_samples).astype(int).clip(0, 20000),
        'oxygen_saturation': np.random.normal(97, 2, n_samples).clip(90, 100),
    }
    
    df = pd.DataFrame(data)
    
    # Create intelligent target variable based on features
    target = np.zeros(n_samples, dtype=int)
    
    # Sleep Apnea: High BMI + Snoring + Low Oxygen
    apnea_condition = (
        (df['bmi_category'] >= 2) &  # Overweight or Obese
        (df['snoring_level'] > 6) &   # High snoring
        (df['oxygen_saturation'] < 96)  # Low oxygen
    )
    apnea_prob = np.random.rand(n_samples)
    target[(apnea_condition) & (apnea_prob > 0.3)] = 2
    
    # Insomnia: High Stress + Low Quality + Short Duration
    insomnia_condition = (
        (df['stress_level'] > 7) &    # High stress
        (df['sleep_quality'] < 5) &   # Poor quality
        (df['sleep_duration'] < 6) &  # Short sleep
        (target == 0)                  # Not already classified as Apnea
    )
    insomnia_prob = np.random.rand(n_samples)
    target[(insomnia_condition) & (insomnia_prob > 0.3)] = 1
    
    # Add some noise/random samples
    random_mask = np.random.rand(n_samples) < 0.1
    target[random_mask] = np.random.randint(0, 3, random_mask.sum())
    
    df['target'] = target
    
    # Calculate class distribution
    class_dist = df['target'].value_counts().sort_index()
    print(f"\nClass Distribution:")
    print(f"  Normal Sleep: {class_dist.get(0, 0)} ({100*class_dist.get(0, 0)/n_samples:.1f}%)")
    print(f"  Insomnia: {class_dist.get(1, 0)} ({100*class_dist.get(1, 0)/n_samples:.1f}%)")
    print(f"  Sleep Apnea: {class_dist.get(2, 0)} ({100*class_dist.get(2, 0)/n_samples:.1f}%)")
    
    # Save to CSV
    df.to_csv(output_path, index=False)
    print(f"\n✓ Training data saved to: {output_path}")
    print(f"✓ Shape: {df.shape} (rows, columns)")
    
    return df

if __name__ == "__main__":
    generate_sleep_training_data(1000)
