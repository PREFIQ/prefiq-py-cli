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

cd sundar

echo ""
echo "📦 Creating full scaffold app: crm"
prefiq new-app crm

echo ""
echo "📦 Creating semi scaffold app: bms"
prefiq new-app bms --base

echo ""
echo "📦 Creating semi scaffold app: bms"
prefiq new-app bms --base --force

echo ""
echo "🧪 Creating and testing app: test"
prefiq new-app test --force

echo ""
echo "📋 Listing all registered apps:"
prefiq list-apps

echo ""
echo "🗑️ Removing test app..."
prefiq remove-app test

echo ""
echo "📋 Listing apps after removal:"
prefiq list-apps

echo ""
echo "✅ All setup and test flow completed successfully!"
read -p "⏸️  Press Enter to exit..."
