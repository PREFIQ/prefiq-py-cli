# prefiq/commands/new_app.py

import os
from rich.console import Console
from prefiq.prefentity.registry import register_app

console = Console()

def new_app(app_name: str, base_path: str = "apps"):
    """Scaffold a new app inside the /apps folder."""
    app_path = os.path.join(base_path, app_name)

    if os.path.exists(app_path):
        console.print(f"[red]❌ App '{app_name}' already exists at {app_path}[/red]")
        return

    # Define structure
    folders = [
        os.path.join(app_path, "static"),
        os.path.join(app_path, "templates")
    ]
    files = {
        os.path.join(app_path, "__init__.py"): "\n".join([
            f'"""Init for {app_name} app."""'
        ]),
        os.path.join(app_path, "app.py"): """def setup():\n    print('App setup logic here')\n""",
        os.path.join(app_path, "static", "script.js"): "console.log('JS loaded');\n",
        os.path.join(app_path, "templates", "index.html"): f"<h1>Welcome to {app_name}</h1>"
    }

    # Create folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        console.print(f"[green]📁 Created:[/green] {folder}")

    # Write files
    for path, content in files.items():
        with open(path, "w") as f:
            f.write(content)
        console.print(f"[blue]📄 Created:[/blue] {path}")

    # Register in prefentity
    register_app(app_name, path=app_path)
    console.print(f"\n[bold bright_green]✅ New app '{app_name}' created successfully![/bold bright_green]")
