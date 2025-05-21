#!/bin/bash

# --- Ensure script is run from the project root ---
cd "$(dirname "$0")"

echo "🔧 Installing pyenv and Python 3.10.13..."

# Install pyenv if not installed
if ! command -v pyenv >/dev/null 2>&1; then
  brew update
  brew install pyenv
fi

# Initialize pyenv (for current shell)
export PYENV_ROOT="$HOME/.pyenv"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"

# Install and set Python 3.10.13
if ! pyenv versions | grep -q "3.10.13"; then
  pyenv install 3.10.13
fi
pyenv local 3.10.13

# Create virtual environment
echo "🐍 Creating virtual environment..."
python3.10 -m venv env
source env/bin/activate

# Upgrade pip & install wheel
pip install --upgrade pip wheel

# Install dependencies
echo "📦 Installing Python packages..."
pip install -r requirements.txt

echo "✅ Setup complete. Activate env with: source env/bin/activate"

