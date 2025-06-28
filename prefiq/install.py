import click
from prefiq.commands.setup_folder import setup_folder

@click.command()
@click.argument('project_name')
def install(project_name):
    """Create a project folder and set up environment."""
    setup_folder(project_name)
