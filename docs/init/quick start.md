# 📘 Prefiq CLI — Quick Start Guide

A modular CLI for scaffolding full-stack apps and sites with clean architecture.

---

## ✅ 1. Clone the Repository

```bash
git clone https://github.com/your-org/prefiq-py-cli.git
```
```bash
cd prefiq-py-cli
```

> 📁 This gives you access to all CLI commands and scaffolding templates.

---

## ⚙️ 2. Extract Templates (if downloaded as ZIP)

If you downloaded from GitHub as a ZIP:

```bash
unzip prefiq-py-cli-main.zip
```

```bash
cd prefiq-py-cli-main
```

---

## 🧪 3. Create a Project Folder (Example: `sundar`)

Run the following to set up a new project:

```bash
pip install -e .
```

```bash
prefiq install sundar
```

This creates the following inside `sundar/`:

* ✅ Python virtual environment (`venv/`)
* ✅ Standard files: `requirements.txt`, `README.md`, `LICENSE`, `.gitignore`
* ✅ Base framework folder: `prefentity/`

---

## 📁 4. Create Apps Using Templates

Inside the project folder:

```bash
cd sundar
```

### ▶️ Full App Scaffold

```bash
prefiq new-app crm
```

Creates a full app in `apps/crm` with:

```
apps/
└── crm/
    ├── app.py
    ├── config.py
    ├── assets/
    ├── templates/
    ├── routes/
    ├── logic/
    ├── database/
    └── ...
```

### ⚡ Semi (Base) App Scaffold

```bash
prefiq new-app auth --base
```

Creates only essential folders and files.

### ♻️ Force Overwrite an Existing App

```bash
prefiq new-app blog --force
```

---

## 📦 5. List and Manage Apps

### List Registered Apps

```bash
prefiq list-apps
```

### Remove an App

```bash
prefiq remove-app blog
```

> 🔁 This also removes it from the `prefentity/manifest.json` registry.

---