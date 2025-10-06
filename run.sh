#!/bin/bash

# Nazanin Bot Runner Script
# نصب و اجرای آسان ربات

set -e

echo "🤖 Nazanin Advanced AI Bot"
echo "=========================="
echo ""

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Please install Python 3.8+"
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "✅ Python $PYTHON_VERSION found"
echo ""

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
fi

# Activate venv
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install/upgrade requirements
echo "📥 Installing dependencies..."
pip install --upgrade pip -q
pip install -r requirements.txt -q
echo "✅ Dependencies installed"
echo ""

# Check config
if [ ! -f "config/config.json" ]; then
    echo "⚠️  config/config.json not found"
    echo "📝 Creating from example..."
    cp config/config.example.json config/config.json
    echo "✅ Config file created"
    echo ""
    echo "🔑 Please edit config/config.json with your API keys"
    echo ""
fi

# Ask which version to run
echo "Which version do you want to run?"
echo "1) Simple version (main.py)"
echo "2) Advanced version (main_advanced.py) - RECOMMENDED"
echo "3) Run tests"
echo "4) Run demo"
echo ""
read -p "Choice [1-4]: " choice

case $choice in
    1)
        echo ""
        echo "🚀 Starting simple version..."
        python3 main.py
        ;;
    2)
        echo ""
        echo "🚀 Starting advanced version..."
        python3 main_advanced.py
        ;;
    3)
        echo ""
        echo "🧪 Running tests..."
        python3 tests/test_basic.py
        ;;
    4)
        echo ""
        echo "🎮 Running demo..."
        python3 tests/demo_advanced.py
        ;;
    *)
        echo "Invalid choice. Running advanced version..."
        python3 main_advanced.py
        ;;
esac
