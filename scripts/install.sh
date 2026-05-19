#!/bin/bash

set -e

echo "Checking Python version..."

if ! command -v python3.11 &> /dev/null; then
  echo "python3.11 is not installed."
  echo "Please install Python 3.11 before running this script."
  exit 1
fi

echo "Creating Python virtual environment..."
python3.11 -m venv .venv

echo "Activating virtual environment..."
source .venv/bin/activate

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Installation completed."
