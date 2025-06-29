# Prefiq CLI Commands

A quick reference for all available `prefiq` CLI commands.

---

## 🚀 Project Setup

### `prefiq install <project_name>`


### `prefiq install <project_name>`

Create a new project folder with:

* Virtual environment
* Prefentity core scaffold
* Default files: `README.md`, `requirements.txt`, `.gitignore`, `LICENSE`

---

cd path/to/your/folder

## 📦 App Management

### `prefiq new-app newpro`

Scaffold a new app:

* Creates `apps/newpro/`
* Adds static, template, and logic files
* Registers the app in `manifest.json`

### `prefiq list-apps`

List all registered apps with name and path.

### `prefiq remove-app newpro`

Unregister an app (does not delete its folder).

---

## 🧱 Prefentity Core (Coming Soon)

### `prefiq state` *(planned)*

Manage global CLI configuration state.

### `prefiq repair` *(planned)*

Fix missing or corrupted files in a project.

### `prefiq backup` *(planned)*

Backup project folders and databases.

### `prefiq reinstall` *(planned)*

Reinstall core or individual app/site environments.

---

## 🌐 Site Management (Planned)

### `prefiq new-site <site_name>` *(planned)*

Scaffold a new site under `sites/<site_name>/`.

### `prefiq list-sites` *(planned)*

List all registered sites.

### `prefiq remove-site <site_name>` *(planned)*

Remove a site from the registry.

---

## 🛠 Development Utilities

### `prefiq enable django` *(planned)*

Enable Django support inside an app.

### `prefiq enable react` *(planned)*

Enable React frontend inside an app.

---

## 📁 File Utilities

Generated automatically by:

* `setup_files.py`
* `setup_folder.py`
* `copy_prefentity_scaffold()`

These are internal, not exposed directly via CLI.

---

> This command list will grow as modules are added.
