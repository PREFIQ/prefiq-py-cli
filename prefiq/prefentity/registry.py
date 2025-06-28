# prefiq/prefentity/registry.py
"""
Handles registration of apps and sites with metadata.
"""

import os
import json

MANIFEST_PATH = "prefentity/manifest.json"

def _load_manifest():
    if not os.path.exists(MANIFEST_PATH):
        return {"apps": [], "sites": [], "version": "1.0.0"}

    with open(MANIFEST_PATH, "r") as f:
        return json.load(f)

def _save_manifest(data):
    with open(MANIFEST_PATH, "w") as f:
        json.dump(data, f, indent=2)

def register_app(name: str, path: str = ""):
    """Register a new app into the manifest.json."""
    manifest = _load_manifest()

    if any(app["name"] == name for app in manifest["apps"]):
        print(f"[!] App '{name}' already registered.")
        return

    manifest["apps"].append({
        "name": name,
        "path": path,
    })

    _save_manifest(manifest)
    print(f"[✓] Registered app: {name}")

def list_apps():
    """List all registered apps."""
    manifest = _load_manifest()
    return manifest.get("apps", [])

def remove_app(name: str):
    """Remove an app by name."""
    manifest = _load_manifest()
    before = len(manifest["apps"])
    manifest["apps"] = [app for app in manifest["apps"] if app["name"] != name]
    if len(manifest["apps"]) < before:
        _save_manifest(manifest)
        print(f"[−] Removed app: {name}")
    else:
        print(f"[!] App '{name}' not found.")

