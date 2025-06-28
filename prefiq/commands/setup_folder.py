import os
import time
import venv
from typing import Callable, List
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

def create_project_dir(project_name: str):
    os.makedirs(project_name)
    time.sleep(0.3)
    console.log(f"[green]📁 Folder created: {project_name}[/green]")

def create_virtualenv(project_name: str):
    env_path = os.path.join(project_name, 'venv')
    venv.create(env_path, with_pip=True)
    console.log(f"[green]🐍 Virtual environment at: {env_path}[/green]")

setup_steps: List[tuple[str, Callable[[str], None]]] = [
    ("Create project directory", create_project_dir),
    ("Create virtual environment", create_virtualenv),
]

def setup_folder(project_name: str):
    """Set up only core folder and virtual environment."""
    if os.path.exists(project_name):
        console.print(f"[red]❌ Folder '{project_name}' already exists.[/red]")
        return

    console.print(f"\n[bold cyan]🚀 Setting up project: '{project_name}'[/bold cyan]")

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        for label, step_fn in setup_steps:
            task = progress.add_task(f"{label}...", start=True)
            try:
                step_fn(project_name)
            except Exception as e:
                console.print(f"[red]❌ Error during '{label}': {e}[/red]")
                break
            progress.remove_task(task)

    console.print(f"\n[bold bright_green]✅ Folder setup complete for '{project_name}'![/bold bright_green]")
