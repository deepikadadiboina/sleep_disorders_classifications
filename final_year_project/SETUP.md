# Sleep Health - Quick Setup Guide

## 🚀 Getting Started (30 seconds)

### For Windows Users:

**Option 1: Automatic Setup (Recommended)**
1. Double-click `run.bat` in the project folder
2. Wait for installation to complete
3. Application will open automatically

**Option 2: Manual Setup**
```bash
# Open Command Prompt and navigate to project folder
cd "c:\Users\deepi\OneDrive\Desktop\final_year_project"

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run app.py
```

### For macOS/Linux Users:

```bash
# Navigate to project folder
cd ~/Desktop/final_year_project

# Run the setup script
chmod +x run.sh
./run.sh
```

---

## ✅ Verification

After the app starts:
1. ✓ Application opens at `http://localhost:8501`
2. ✓ You see "Sleep Health" home page
3. ✓ Navigation menu appears on left
4. ✓ Buttons are clickable

## 🎯 First Steps

1. **Click "Get Started"** on home page
2. **Fill patient details** with your information
3. **Click "Analyze Sleep"** to get prediction
4. **View results** with recommendations
5. **Download PDF** or check history

## 🛠️ Common Issues

### Issue: Port 8501 already in use
```bash
streamlit run app.py --server.port 8502
```

### Issue: Module not found
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Issue: Application won't start
- Ensure Python 3.11+ is installed
- Check internet connection for first-time setup
- Delete `venv` folder and try again

## 📊 Testing the Application

### Test Scenario 1: Normal Sleep
- Age: 30
- Sleep Duration: 8 hours
- Sleep Quality: 8/10
- Stress Level: 3/10
- BMI: Normal Weight
**Expected**: Normal Sleep, Low Risk

### Test Scenario 2: Insomnia
- Age: 40
- Sleep Duration: 4 hours
- Sleep Quality: 3/10
- Stress Level: 9/10
- BMI: Normal Weight
**Expected**: Insomnia, Medium/High Risk

### Test Scenario 3: Sleep Apnea
- Age: 55
- Sleep Duration: 6 hours
- Snoring Level: 9/10
- BMI: Obese
- Oxygen Saturation: 94%
**Expected**: Sleep Apnea, High Risk

---

## 📁 Project Structure Reference

```
final_year_project/
├── app.py                    ← Main application (Home page)
├── requirements.txt          ← Python dependencies
├── run.bat                   ← Windows launcher
├── run.sh                    ← Linux/macOS launcher
├── README.md                 ← Full documentation
├── SETUP.md                  ← This file
│
├── pages/
│   ├── 01_patient_details.py ← Patient input form
│   ├── 02_results.py         ← Results display
│   ├── 03_history.py         ← History viewer
│   └── 04_about.py           ← About page
│
├── utils/
│   ├── model.py              ← ML model & prediction
│   ├── report_generator.py   ← PDF generation
│   └── history.py            ← History management
│
├── models/                   ← ML models (auto-created)
├── data/                     ← Data storage (auto-created)
└── assets/                   ← Application assets
```

## 🎓 For Demo/Interview

### Preparation
1. Run application once to generate models (first run is slower)
2. Complete a sample assessment to test workflow
3. Download a sample PDF report
4. Review the About page

### Demo Flow
1. **Show Home Page**: Explain the application purpose
2. **Complete Assessment**: Fill patient details
3. **Show Results**: Display prediction and recommendations
4. **Download Report**: Generate and show PDF
5. **Show History**: Display assessment tracking
6. **Discuss Technology**: Explain ML, Flask, features

### Key Points for Interview
- ✅ Real healthcare product design
- ✅ Machine learning implementation
- ✅ Professional UI/UX
- ✅ Responsive design
- ✅ Full-stack development
- ✅ PDF generation
- ✅ Data locality & privacy
- ✅ Model training & prediction

---

## 🔒 Important Notes

1. **First Run**: Takes longer (~30 seconds) to train ML model
2. **Data Privacy**: All data stays on your device
3. **Medical Disclaimer**: Always include in presentations
4. **Screenshots**: Take before demo for backup

---

## 📞 Support

If you encounter any issues:
1. Check the README.md for detailed documentation
2. Verify Python version: `python --version`
3. Reinstall dependencies: `pip install --force-reinstall -r requirements.txt`
4. Clear cache: Delete `__pycache__` folders and `.streamlit` folder

---

**Ready to go!** 🚀

