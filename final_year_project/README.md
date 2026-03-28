# 💤 Sleep Health - Professional Sleep Disorder Prediction Application

A professional healthcare web application built with Python and Streamlit for predicting sleep disorders using machine learning.

## 🎯 Project Overview

Sleep Health is a comprehensive sleep assessment application designed as a real healthcare product. It uses advanced machine learning algorithms to predict sleep disorders including:
- **Normal Sleep**: Healthy sleep patterns
- **Insomnia**: Difficulty falling/staying asleep
- **Sleep Apnea**: Breathing interruptions during sleep

The application provides personalized recommendations and generates professional PDF health reports.

## ✨ Key Features

### ✅ Core Functionality
- **Real-time ML Predictions**: Instant sleep disorder assessment
- **Personalized Recommendations**: Tailored lifestyle and medical advice
- **PDF Report Generation**: Professional downloadable health reports
- **Assessment History**: Track predictions over time
- **Responsive Design**: Works on all devices (mobile, tablet, desktop)

### 💡 User Experience
- **Modern UI/UX**: Dark theme with blue gradient design
- **Intuitive Navigation**: Easy-to-use navigation bar with all pages
- **Form Validation**: Comprehensive patient data input
- **Real-time Feedback**: Loading states and result visualization
- **Color-coded Results**: Visual risk level indicators

## 🛠️ Tech Stack

- **Language**: Python 3.11+
- **Framework**: Streamlit
- **ML Libraries**: Scikit-learn, TensorFlow, NumPy, Pandas
- **PDF Generation**: ReportLab
- **Environment**: Windows 10+
- **Requirements**: Standard laptop (i5, 8GB RAM)

## 📋 Application Structure

```
final_year_project/
├── app.py                          # Main Streamlit app (Home page)
├── requirements.txt                # Python dependencies
├── README.md                       # This file
│
├── pages/                          # Multi-page components
│   ├── 01_patient_details.py      # Patient input form
│   ├── 02_results.py              # Prediction results display
│   ├── 03_history.py              # Assessment history
│   └── 04_about.py                # About & information
│
├── utils/                          # Utility modules
│   ├── model.py                    # ML prediction model
│   ├── report_generator.py         # PDF report generation
│   └── history.py                  # History management
│
├── models/                         # Trained ML models
│   ├── sleep_model.joblib         # Trained classifier
│   └── scaler.joblib              # Feature scaler
│
├── assets/                         # Application assets
└── data/                           # Data storage
    └── history.json               # Assessment history
```

## 🚀 Quick Start

### Prerequisites
- Python 3.11 or higher
- Windows 10+ (other OS compatible)
- At least 8GB RAM
- Internet connection (for first-time setup)

### Installation

1. **Navigate to project directory**
   ```bash
   cd "c:\Users\deepi\OneDrive\Desktop\final_year_project"
   ```

2. **Create Python virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

The application will open in your default browser at `http://localhost:8501`

## 📖 Usage Guide

### Home Page
- Welcome screen with application overview
- Sleep conditions explanation
- "Get Started" button to begin assessment

### Patient Details Page
Complete your health assessment with:
- **Personal Information**: Gender, Age
- **Sleep Habits**: Duration, Quality, Stress Level, Snoring Level
- **Health Metrics**: BMI, Heart Rate, Blood Pressure, Physical Activity, Steps, Oxygen Saturation

Click "Analyze Sleep" to get predictions.

### Results Page
View your assessment results:
- **Predicted Condition**: Insomnia, Sleep Apnea, or Normal Sleep
- **Risk Level**: Low, Medium, or High (color-coded)
- **Confidence Score**: Model confidence percentage
- **Key Findings**: Summary of health metrics
- **Personalized Recommendations**: Lifestyle, Sleep Habits, Medical Advice

### Actions
- **Download Report**: Generate PDF of your assessment
- **View History**: See past assessments
- **New Assessment**: Start another evaluation

### History Page
- View all past assessments in reverse chronological order
- See prediction trends
- Statistics on total assessments and risk levels
- Clear history option

### About Page
- Application information
- Sleep disorders overview
- Privacy & Security details
- Medical disclaimer
- Technology stack information

## 🧠 Machine Learning Model

### Model Details
- **Algorithm**: Random Forest Classifier
- **Features**: 13 health and lifestyle parameters
- **Classes**: 3 sleep conditions
- **Training Data**: Synthetic training data (500 samples)

### Features Used
1. Gender
2. Age
3. Sleep Duration
4. Sleep Quality
5. Stress Level
6. Snoring Level
7. BMI Category
8. Heart Rate
9. Systolic Blood Pressure
10. Diastolic Blood Pressure
11. Physical Activity
12. Daily Steps
13. Oxygen Saturation

### Model Training
The model is automatically trained on first run and saved to `/models/` directory:
- `sleep_model.joblib` - Trained model
- `scaler.joblib` - Feature scaler

## 📊 Prediction Logic

### Normal Sleep Indicators
- Sleep duration 6-9 hours
- High sleep quality
- Low stress levels
- Normal vitals

### Insomnia Risk Factors
- Short sleep duration (<6 hours)
- Low sleep quality
- High stress levels
- Age-related factors

### Sleep Apnea Risk Factors
- High BMI
- Loud snoring
- Low oxygen saturation (<96%)
- High heart rate
- Hypertension

## 📄 PDF Report Features

Generated reports include:
- Header with report date and time
- Patient demographics
- Health metrics summary
- Assessment results and risk level
- Confidence score
- Personalized recommendations
- Medical disclaimer

## 🔒 Privacy & Security

- All data processing happens locally on your device
- No data sent to external servers
- Assessment history stored in local JSON file
- No cloud storage or external APIs
- No user tracking or analytics

## ⚠️ Medical Disclaimer

**IMPORTANT**: This application is for informational purposes only and is NOT a substitute for professional medical advice.

- Results are AI-based analysis, not clinical diagnosis
- Always consult healthcare professionals for medical concerns
- For severe sleep issues, seek immediate medical attention
- Contact a sleep specialist for diagnosis and treatment

## 🐛 Troubleshooting

### Port 8501 already in use
```bash
streamlit run app.py --server.port 8502
```

### Module import errors
```bash
pip install --upgrade -r requirements.txt
```

### Slow performance
- Close unnecessary applications
- Ensure sufficient RAM (8GB+ recommended)
- First run trains the model (slower), subsequent runs are faster

### History file issues
The application automatically creates `data/history.json`. If errors occur:
1. Delete `data/history.json`
2. Restart the application

## 📱 Responsive Design

The application is fully responsive for:
- **Desktop**: Full layout with all features
- **Tablet**: Optimized column layouts (2-3 columns)
- **Mobile**: Single column layout with hamburger navigation

## 🎨 UI/UX Design

### Design Philosophy
- **Modern & Professional**: Suitable for healthcare environment
- **Dark Theme**: Easy on the eyes with blue accent colors
- **Intuitive Navigation**: Clear menu structure
- **Accessibility**: Large text, high contrast colors
- **Responsive**: Works on all screen sizes

### Color Scheme
- **Primary**: Deep Blue (#1e3a8a)
- **Accent**: Light Blue (#3b82f6)
- **Success**: Green (#28a745)
- **Warning**: Yellow (#ffc107)
- **Danger**: Red (#dc3545)

## 📊 Performance

- **Prediction Time**: <2 seconds
- **PDF Generation**: <1 second
- **History Load**: <500ms
- **First Run**: ~30 seconds (model training included)

## 🚀 Deployment

### Local Testing
```bash
streamlit run app.py
```

### Cloud Deployment (Optional)
The application can be deployed to:
- Streamlit Cloud (free)
- AWS Elastic Beanstalk
- Google Cloud Platform
- Microsoft Azure

## 📚 Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Scikit-learn Documentation](https://scikit-learn.org)
- [Sleep Disorders Information](https://www.sleepfoundation.org)

## 🔄 Future Enhancements

- Integration with wearable devices
- Advanced ML models (Neural Networks)
- User authentication and profiles
- Sleep tracking API integration
- Multi-language support
- Healthcare provider integration

## 👤 Project Information

- **Type**: Final Year Project
- **Purpose**: Demonstrating ML in Healthcare
- **Version**: 1.0.0
- **Status**: Active Development
- **Owner**: Sleep Health Team

## ✅ Testing Checklist

- [x] Home page displays correctly
- [x] Patient details form works
- [x] ML predictions generate
- [x] Results display properly
- [x] PDF reports generate
- [x] History tracking works
- [x] Responsive on mobile/tablet
- [x] Navigation works correctly
- [x] All buttons functional
- [x] Error handling in place

## 📝 License

This project is created for educational purposes as a final year project.

---

**For any issues or questions, please review the About page for support information.**

🌙 **Happy sleeping!** 😴

