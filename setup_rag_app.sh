# this script is for Mac. On Windows, create a env with Python 3.10.13 and install the requirements.txt file.


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

# Create virtual environment if it doesn't exist
if [ ! -d "env" ]; then
  echo "🐍 Creating virtual environment..."
  python3.10 -m venv env
fi

# Upgrade pip & install wheel
echo "⬆️  Upgrading pip and installing wheel..."
source env/bin/activate
pip install --upgrade pip wheel

# Install dependencies
echo "📦 Installing Python packages..."
pip install -r requirements.txt

echo ""
echo "✅ Setup complete. Virtual environment is active."
echo "You can now run Python commands within this shell."
echo ""

# Launch an interactive shell with the virtual environment activated
exec $SHELL -i -c "source env/bin/activate; exec $SHELL"

