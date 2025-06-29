# Prefiq CLI Setup Documentation

This document outlines the current state of the `prefiq` CLI tool, which scaffolds Python environments and core framework features for app and site development using a modular, rack-like structure.

---

## ✅ Current Features

### 1. `prefiq install <project_name>`

* Sets up a new project folder
* Initializes a virtual environment
* Copies the `prefentity/` core engine scaffold
* Creates basic files: `README.md`, `requirements.txt`, `.gitignore`, `LICENSE`

### 2. `prefiq new-app <name>`

* Creates a new app under `apps/<name>/`
* Adds the following structure:

  ```
  apps/<name>/
  ├── __init__.py
  ├── app.py
  ├── static/
  │   └── script.js
  └── templates/
      └── index.html
  ```
* Automatically registers the app in `prefentity/manifest.json`

### 3. `prefiq list-apps`

* Lists all registered apps from the manifest file
* Outputs name and path in a styled table using Rich

### 4. `prefiq remove-app <name>`

* Unregisters the app from `manifest.json`
* Leaves the actual app folder untouched

---

## 🧱 Core System: `prefentity/`

This is the core engine that holds metadata and utilities:

### Current Modules Scaffolded:

* `registry.py` — App/site registration system
* `state.py` — Persistent configuration and state (to be implemented)
* `logs.py` — Logging helpers (planned)
* `backup.py` — Data backup logic (planned)
* `repair.py` — Repair broken installations (planned)
* `reinstall.py` — Reset/reinstall module or app (planned)
* `migrations.py` — App migration support (planned)
* `defaults.py` — Default configs and fallback logic
* `manifest.json` — Tracks registered apps/sites and project version

---

## 🛠 Internal Utilities

### `setup_folder()`

* Handles folder creation and virtualenv setup
* Includes a progress spinner and user-friendly output

### `copy_prefentity_scaffold()`

* Copies pre-built template files from `templates/prefentity/`
* Uses `shutil.copytree` with fallback logging

### `setup_files.py`

* Manages file creation helpers like `add_readme_md`, `add_requirements_txt`, etc.

---

## 🚀 What’s Next

### 1. `prefiq new-site <name>`

* Similar to `new-app`, but in `/sites/<name>/`

### 2. CLI Grouping

* `prefiq app list`, `prefiq app remove`, etc.
* Cleaner structure using Click command groups

### 3. Implement Core `prefentity` Logic

* `logs.py`, `state.py`, `repair.py`, `backup.py`
* Utility hooks used across project lifecycle

### 4. App Framework Integration

* Optional `prefiq enable django` or `prefiq enable react`
* Adds framework boilerplate inside app folders

### 5. Admin Dashboard

* A local dev admin (`prefiq admin`) for visual management (future)

---

## 📁 Directory Overview

```
prefiq-py-cli/
├── prefiq/
│   ├── cli.py
│   ├── install.py
│   ├── commands/
│   │   ├── setup_folder.py
│   │   ├── setup_files.py
│   │   ├── new_app.py
│   │   ├── app_commands.py
│   └── prefentity/
│       ├── __init__.py
│       ├── registry.py
│       ├── manifest.json
│       └── ... (future core files)
├── templates/
│   └── prefentity/
│       └── (scaffold source)
└── templates/shell/
    └── setup_prefentity.sh
```

---

## 🧠 Philosophy

* Modular: Each app/site is independent
* Scalable: Can use plain Python, Django, or React
* Pluggable: Optional layers like migrations, backup, admin UI
* Minimal: CLI-first, boilerplate-light

---

## 👣 Next Action

> Continue with `prefiq new-site`, and begin wiring deeper prefentity modules like `state`, `logs`, and `backup`. Ready for full-stack extensions.

Let me know when you're ready to scaffold `new-site`!
