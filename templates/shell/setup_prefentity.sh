#!/bin/bash

# Define relative path from shell script location
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASE_DIR="$SCRIPT_DIR/../prefentity"
ZIP_NAME="$SCRIPT_DIR/../prefentity_scaffold.zip"

echo "🚀 Creating scaffold in $BASE_DIR..."

# Create base folder
mkdir -p "$BASE_DIR"

# Define files and content
declare -A files=(
  ["__init__.py"]="\"\"\"\nPrefentity: The core engine for managing apps, sites, state, and maintenance.\n\"\"\""
  ["registry.py"]="\"\"\"\nHandles registration of apps and sites with metadata.\n\"\"\""
  ["state.py"]="\"\"\"\nStores and retrieves persistent state information for the project.\n\"\"\""
  ["logs.py"]="\"\"\"\nLogs key events and actions to a file or stdout.\n\"\"\""
  ["backup.py"]="\"\"\"\nProvides backup and restore functionality.\n\"\"\""
  ["repair.py"]="\"\"\"\nChecks for and fixes broken configurations or missing files.\n\"\"\""
  ["reinstall.py"]="\"\"\"\nAllows complete reinstallation of a module or app.\n\"\"\""
  ["migrations.py"]="\"\"\"\nManages schema and data migrations for all apps.\n\"\"\""
  ["defaults.py"]="\"\"\"\nDefault configuration values used across prefentity.\n\"\"\""
  ["manifest.json"]="{\n  \"apps\": [],\n  \"sites\": [],\n  \"version\": \"1.0.0\"\n}"
)

# Create each file
for filename in "${!files[@]}"; do
  echo -e "${files[$filename]}" > "$BASE_DIR/$filename"
  echo "✅ Created $filename"
done

# Zip the folder
cd "$SCRIPT_DIR/.." || exit
zip -r "prefentity_scaffold.zip" "prefentity" > /dev/null
echo "📦 Zipped scaffold into $ZIP_NAME"
