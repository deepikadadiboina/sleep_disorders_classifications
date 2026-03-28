@echo off
REM Sleep Health Application Launcher
REM This script sets up and runs the Sleep Health application

echo.
echo ========================================
echo   Sleep Health - Application Launcher
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python 3.11+ from python.org
    pause
    exit /b 1
)

echo [+] Python found
python --version

REM Create virtual environment if it doesn't exist
if not exist "venv\" (
    echo.
    echo [*] Creating virtual environment...
    python -m venv venv
    if %errorlevel% neq 0 (
        echo [ERROR] Failed to create virtual environment
        pause
        exit /b 1
    )
    echo [+] Virtual environment created
)

REM Activate virtual environment
echo.
echo [*] Activating virtual environment...
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo [ERROR] Failed to activate virtual environment
    pause
    exit /b 1
)
echo [+] Virtual environment activated

REM Install requirements
echo.
echo [*] Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)
echo [+] Dependencies installed

REM Run Streamlit
echo.
echo ========================================
echo   Starting Sleep Health Application
echo ========================================
echo.
echo The application will open in your browser shortly...
echo Press Ctrl+C to stop the server
echo.

streamlit run app.py

pause
