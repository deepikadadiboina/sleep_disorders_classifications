#!/usr/bin/env python3
"""
Sleep Health - Verification Script
Verifies all dependencies and project setup
"""

import sys
import subprocess

def check_python_version():
    """Check if Python version is 3.11+"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 11):
        print("❌ Python 3.11+ required")
        print(f"   Current: Python {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro}")
    return True

def check_packages():
    """Check if all required packages are installed"""
    packages = [
        'streamlit',
        'numpy',
        'pandas',
        'sklearn',
        'tensorflow',
        'reportlab',
        'PIL',
        'requests',
        'joblib'
    ]
    
    missing = []
    for package in packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} - NOT INSTALLED")
            missing.append(package)
    
    return len(missing) == 0, missing

def check_files():
    """Check if all required files exist"""
    import os
    
    required_files = [
        'app.py',
        'requirements.txt',
        'README.md',
        'SETUP.md',
        'pages/01_patient_details.py',
        'pages/02_results.py',
        'pages/03_history.py',
        'pages/04_about.py',
        'utils/model.py',
        'utils/report_generator.py',
        'utils/history.py',
        '.streamlit/config.toml'
    ]
    
    all_exist = True
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} - MISSING")
            all_exist = False
    
    return all_exist

def main():
    print("\n" + "="*50)
    print("  Sleep Health - Verification Script")
    print("="*50 + "\n")
    
    print("Checking Python Version:")
    print("-" * 50)
    py_ok = check_python_version()
    
    print("\nChecking Installed Packages:")
    print("-" * 50)
    pkg_ok, missing_packages = check_packages()
    
    print("\nChecking Project Files:")
    print("-" * 50)
    files_ok = check_files()
    
    print("\n" + "="*50)
    if py_ok and pkg_ok and files_ok:
        print("✅ ALL CHECKS PASSED")
        print("   Application is ready to run!")
        print("   Use: streamlit run app.py")
    else:
        print("⚠️  ISSUES FOUND:")
        if not py_ok:
            print("   • Update Python to 3.11+")
        if not pkg_ok:
            print("   • Install missing packages:")
            print(f"     pip install {' '.join(missing_packages)}")
        if not files_ok:
            print("   • Check if all files are in place")
            print("   • Re-download project if files missing")
    print("="*50 + "\n")

if __name__ == "__main__":
    main()
