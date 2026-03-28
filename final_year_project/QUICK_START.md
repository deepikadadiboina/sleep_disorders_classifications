# 🚀 QUICK START GUIDE - Sleep Health Application

## ⚡ 3-Step Launch

### Step 1️⃣ Generate & Train (Takes ~2-3 minutes)
```bash
# Generate 1000 training samples
python generate_training_data.py

# Train all 4 ML models
python ml_training_pipeline.py

# Create professional visualizations
python ml_analytics.py
```

✅ **Creates:**
- `data/sleep_training_data.csv`
- 4 trained model files in `models/`
- `models/training_results.json`
- 4 PNG visualization files

---

### Step 2️⃣ Run Application
```bash
streamlit run app.py
```

✅ **Opens:** `http://localhost:8501`

---

### Step 3️⃣ Explore the App

**Navigation Menu (9 Items):**
1. 🏠 **Home** - Overview & features
2. 👤 **Patient Details** - Enter patient data
3. 📊 **Results** - Prediction results
4. 📈 **History** - Track assessments
5. 🧠 **ML Training** - Interface for training
6. 📊 **Model Comparison** - View metrics
7. 📉 **Analytics** - See 4 visualizations
8. 📋 **Specifications** - Requirements & specs
9. ℹ️ **About** - Project info

---

## 🎯 Common Tasks

### View Patient Assessment
1. Click **Patient Details** from menu
2. Enter health information (13 fields)
3. Click **Predict Sleep Health**
4. View results on **Results** page
5. Download PDF report

### Compare ML Models
1. Click **ML Training** → **Train Models** button
2. Go to **Model Comparison**
3. Review accuracy, precision, recall, F1-score
4. See which model performs best

### View Analytics
1. Click **Analytics** from menu
2. Explore 4 tabs:
   - 📊 Model Accuracy
   - 📈 Feature Importance
   - 🎯 Confusion Matrices
   - 📊 Metrics Comparison

### Check Project Specs
1. Click **Specifications** from menu
2. Review:
   - S/W & H/W requirements
   - Algorithm descriptions
   - Dataset features
   - Performance targets

---

## 🔄 Troubleshooting

### ❌ "Module not found"
```bash
pip install -r requirements.txt
```

### ❌ "No models found"
```bash
python ml_training_pipeline.py
```

### ❌ "Images not showing in Analytics"
```bash
python ml_analytics.py
```

### ❌ "Streamlit not found"
```bash
pip install streamlit==1.28.1
```

### ❌ "Application crashes"
- Close other applications
- Restart: `streamlit run app.py`
- Check RAM availability (need 8GB+)

---

## 💾 File Locations

| What | Where |
|-----|-------|
| Training Data | `data/sleep_training_data.csv` |
| Models | `models/*.joblib` |
| Metrics | `models/training_results.json` |
| Charts | `models/*.png` |
| Patient History | `utils/patient_history.csv` |

---

## 📊 Expected Results After Training

**Model Accuracy (Expected):**
- Logistic Regression: 85-90%
- QDA: 90-92%
- Random Forest: 92-95% ⭐
- Gradient Boosting: 93-96%

**Charts Generated:**
- model_accuracy_comparison.png
- feature_importance.png
- confusion_matrices.png
- metrics_comparison.png

---

## 💡 Tips

1. **First Run:** Takes ~5 minutes for training
2. **Predictions:** <100ms with Random Forest
3. **Best Accuracy:** Gradient Boosting model
4. **Fast Training:** Logistic Regression
5. **Most Balanced:** Random Forest

---

## 🎓 Pages Overview

### Home (app.py)
- Project overview
- Sleep disorder info
- Quick links to all features
- "Get Started" CTA button

### Patient Details (01_patient_details.py)
- **Form Fields:** 13 health parameters
- **Validation:** Real-time error checking
- **Output:** Instant prediction
- **Features:** Auto-fill previous data

### Results (02_results.py) 
- **Prediction:** Sleep disorder classification
- **Confidence:** Prediction confidence score
- **Recommendations:** Personalized health tips
- **Report:** Download PDF

### History (03_history.py)
- **Records:** All previous assessments
- **Timeline:** Date and time tracking
- **Trends:** Observe changes over time
- **Export:** Download as CSV

### ML Training (06_ml_training.py)
- **Generate Data:** Create 1000 training samples
- **Train Models:** Train all 4 algorithms
- **Manual:** Command reference
- **Status:** Check completion

### Model Comparison (05_model_comparison.py)
- **Metrics Table:** Accuracy, Precision, Recall, F1
- **Best Model:** Highlighted top performer
- **Algorithm Details:** Description of each model
- **Use Cases:** When to use each model

### Analytics (07_analytics.py)
- **Accuracy Chart:** 4 models compared
- **Feature Importance:** Top 13 features ranked
- **Confusion Matrices:** Detailed classification
- **Metrics Comparison:** Side-by-side metrics

### Specifications (08_specifications.py)
- **S/W Requirements:** OS, Python, libraries
- **H/W Requirements:** CPU, RAM, Storage
- **Algorithms:** Details of each ML model
- **Dataset:** Feature descriptions
- **Performance:** Expected accuracy ranges

### About (04_about.py)
- Project overview
- Team information
- Contact details
- License information

---

## ⌚ Timing Guide

| Task | Time |
|------|------|
| Install dependencies | 2-5 min |
| Generate training data | 30 sec |
| Train all 4 models | 1-2 min |
| Generate visualizations | 30 sec |
| Start Streamlit app | 5 sec |
| Single prediction | <100ms |

---

## 🎮 Interactive Features

- ✅ Real-time input validation
- ✅ Instant predictions
- ✅ Download PDF reports
- ✅ Export CSV data
- ✅ Model switching
- ✅ Interactive charts
- ✅ Tabbed navigation
- ✅ Responsive design

---

## 🔒 Data Handling

- 📝 Patient data stored locally
- 🔐 No cloud upload
- 💾 CSV backup available
- 🗑️ Delete data anytime
- 📋 PDF for sharing

---

## 📞 Help

**Need more info?**
1. Read `README.md` - Comprehensive guide
2. Check `COMPLETION_STATUS.md` - Feature list
3. Review code comments in source files
4. Check `Specifications` page in app

---

## ✅ Verification Checklist

Before running, verify:
- ✅ Python 3.11+ installed: `python --version`
- ✅ Dependencies installed: `pip list | grep streamlit`
- ✅ 8GB+ RAM available
- ✅ 1GB+ storage available
- ✅ All scripts present: `dir *.py`

---

## 🚀 Ready to Launch?

```bash
# All in one command:
python generate_training_data.py && python ml_training_pipeline.py && python ml_analytics.py && streamlit run app.py
```

Then open: **http://localhost:8501** 🎉

---

**Happy predicting! 💤**
