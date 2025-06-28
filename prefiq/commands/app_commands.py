# prefiq/commands/app_commands.py
import click
from rich.table import Table
from rich.console import Console
from prefiq.prefentity.registry import list_apps, remove_app

console = Console()

@click.command("list-apps")
def list_apps_cmd():
    """List all registered apps."""
    apps = list_apps()
    if not apps:
        console.print("[yellow]No apps registered.[/yellow]")
        return

    table = Table(title="Registered Apps")
    table.add_column("Name", style="cyan")
    table.add_column("Path", style="green")

    for app in apps:
        table.add_row(app.get("name", "-"), app.get("path", "-"))

    console.print(table)

@click.command("remove-app")
@click.argument("app_name")
def remove_app_cmd(app_name):
    """Remove a registered app by name."""
    remove_app(app_name)
