# prefiq/commands/prefentity_scaffold.py

import os
import shutil
from rich.console import Console

console = Console()

def copy_prefentity_scaffold(project_name: str):
    """
    Copy prefentity scaffold folder from templates into the new project directory.
    """
    src = os.path.join("templates", "prefentity")
    dst = os.path.join(project_name, "prefentity")

    if not os.path.exists(src):
        console.print(f"[red] Template source not found: {src}[/red]")
        return

    if os.path.exists(dst):
        console.print(f"[yellow] Prefentity folder already exists at: {dst}[/yellow]")
        return

    try:
        shutil.copytree(src, dst)
        console.print(f"[green] Copied prefentity scaffold to:[/green] {dst}")
    except Exception as e:
        console.print(f"[red] Failed to copy scaffold: {e}[/red]")
