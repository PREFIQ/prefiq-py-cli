#!/bin/bash

# Exit if any command fails
set -e

echo "🔁 Uninstalling previous version of prefiq (if installed)..."
pip uninstall prefiq -y || true

echo "🧹 Removing existing 'sundar' folder if present..."
rm -rf sundar

echo "📦 Installing prefiq in editable mode..."
pip install -e .

echo ""
echo "🚀 Running: prefiq install sundar"
echo "--------------------------------"

prefiq install sundar

echo ""
read -p "⏸️  Press Enter to exit..."
