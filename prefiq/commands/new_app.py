# prefiq/commands/new_app.py
import os
import shutil
import click
from rich.console import Console
from prefiq.prefentity.registry import register_app

console = Console()

@click.command()
@click.argument("app_name")
@click.option("--base", is_flag=True, help="Create only the base structure (semi scaffold)")
@click.option("--path", default="apps", help="Base directory to create the app in")
@click.option("--force", is_flag=True, help="Force overwrite if app already exists")
def new_app(app_name: str, base: bool, path: str, force: bool):
    """
    Scaffold a new app from the predefined template into the apps directory.

    By default, generates a full scaffold. Use --base for a minimal structure.
    """
    mode = "semi" if base else "full"

    # Resolve absolute path to templates/app_full regardless of current working directory
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    src = os.path.join(root_dir, "templates", "app_full")
    dst = os.path.join(path, app_name)

    if os.path.exists(dst):
        if not force:
            console.print(f"[red] App '{app_name}' already exists at {dst}[/red]")
            return
        else:
            shutil.rmtree(dst)
            console.print(f"[yellow] Overwriting existing app at {dst}...[/yellow]")

    console.print(f"[cyan] Creating app '{app_name}' in mode: {mode}[/cyan]")

    if not os.path.exists(src):
        console.print(f"[red] Template source not found: {src}[/red]")
        return

    if mode == "full":
        shutil.copytree(src, dst)
        console.print(f"[green] Full scaffold copied to:[/green] {dst}")
    else:
        os.makedirs(dst)
        keep_folders = [
            "app.py", "config.py", "__init__.py",
            "routes", "templates", "assets", "logic/controllers", "database/models"
        ]
        for item in keep_folders:
            src_path = os.path.join(src, item)
            dst_path = os.path.join(dst, item)
            if os.path.isdir(src_path):
                shutil.copytree(src_path, dst_path)
            elif os.path.isfile(src_path):
                os.makedirs(os.path.dirname(dst_path), exist_ok=True)
                shutil.copy2(src_path, dst_path)
        console.print(f"[green] Semi scaffold copied to:[/green] {dst}")

    register_app(app_name, path=dst)
    console.print(f"\n[bold bright_green] App '{app_name}' created successfully![/bold bright_green]")

