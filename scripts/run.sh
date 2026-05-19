#!/bin/bash

set -e

if [ ! -d ".venv" ]; then
  echo "Virtual environment not found. Run scripts/install.sh first."
  exit 1
fi

if [ ! -f ".env" ]; then
  echo ".env file not found. Please copy .env.example to .env and configure it."
  exit 1
fi

source .venv/bin/activate

uvicorn app.main:app --host 127.0.0.1 --port 8000
