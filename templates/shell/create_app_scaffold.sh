#!/bin/bash

BASE_DIR="templates/app_full"

# Folder structure
FOLDERS=(
  "routes"
  "logic/controllers"
  "logic/middleware"
  "logic/services"
  "logic/repositories"
  "logic/commands"
  "database/models"
  "database/migrations"
  "database/factories"
  "database/seeders"
  "support/utils"
  "support/validators"
  "support/events"
  "support/exceptions"
  "assets/css"
  "assets/js"
  "assets/images"
  "templates"
  "storage/uploads"
  "logs"
  "audit"
  "tests"
  "docs"
)

# Files and content
declare -A FILES
FILES=(
  ["app.py"]='"""Entry point for app setup."""'
  ["config.py"]='"""Configuration for the app."""'
  ["__init__.py"]='"""App module initializer."""'
  ["routes/web.py"]='"""Web (HTML) routes."""\n\ndef register_web_routes():\n    pass'
  ["routes/api.py"]='"""API (JSON) routes."""\n\ndef register_api_routes():\n    pass'
  ["logic/controllers/post_controller.py"]='"""Handle post-related requests."""'
  ["logic/middleware/auth.py"]='"""Middleware for authentication."""'
  ["logic/services/post_service.py"]='"""Business logic for posts."""'
  ["logic/repositories/post_repository.py"]='"""DB interaction for posts."""'
  ["logic/commands/clear_cache.py"]='"""CLI command to clear cache."""'
  ["database/models/post.py"]='"""Post ORM model."""'
  ["database/schema.py"]='"""Schema definitions if needed."""'
  ["support/utils/slugify.py"]='"""Utility to create slugs."""'
  ["support/validators/post_validator.py"]='"""Validation logic for posts."""'
  ["support/events/post_created.py"]='"""Post created event."""'
  ["support/exceptions/post_error.py"]='"""Custom exceptions for posts."""'
  ["templates/index.html"]='<!-- HTML template -->\n<h1>Hello from template!</h1>'
  ["assets/css/style.css"]="/* Base styles */"
  ["assets/js/script.js"]="// JS logic"
  ["assets/images/.keep"]=""
  ["storage/uploads/.keep"]=""
  ["logs/app.log"]=""
  ["audit/audit_log.json"]=""
  ["tests/test_models.py"]='"""Tests for models."""'
  ["tests/test_routes.py"]='"""Tests for routes."""'
  ["docs/readme.md"]="# Documentation\n\nDescribe app structure and usage here."
)

echo "📁 Creating folders..."
for folder in "${FOLDERS[@]}"; do
  mkdir -p "$BASE_DIR/$folder"
  echo "✅ Created: $BASE_DIR/$folder"
done

echo "📄 Creating files..."
for filepath in "${!FILES[@]}"; do
  fullpath="$BASE_DIR/$filepath"
  echo -e "${FILES[$filepath]}" > "$fullpath"
  echo "📄 Created: $fullpath"
done

echo -e "\n🎉 App scaffold created successfully at: $BASE_DIR"
