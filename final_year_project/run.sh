#!/bin/bash
# Sleep Health Application Launcher for Linux/macOS

echo ""
echo "========================================"
echo "  Sleep Health - Application Launcher"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 is not installed"
    echo "Please install Python 3.11+ from python.org"
    exit 1
fi

echo "[+] Python found"
python3 --version

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo ""
    echo "[*] Creating virtual environment..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "[ERROR] Failed to create virtual environment"
        exit 1
    fi
    echo "[+] Virtual environment created"
fi

# Activate virtual environment
echo ""
echo "[*] Activating virtual environment..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "[ERROR] Failed to activate virtual environment"
    exit 1
fi
echo "[+] Virtual environment activated"

# Install requirements
echo ""
echo "[*] Installing dependencies..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "[ERROR] Failed to install dependencies"
    exit 1
fi
echo "[+] Dependencies installed"

# Run Streamlit
echo ""
echo "========================================"
echo "  Starting Sleep Health Application"
echo "========================================"
echo ""
echo "The application will open in your browser shortly..."
echo "Press Ctrl+C to stop the server"
echo ""

streamlit run app.py
