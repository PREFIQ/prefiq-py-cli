# prefiq/install.py

import click
from prefiq.commands.setup_folder import setup_folder
from prefiq.commands.files.setup_files import create_project_files  # ✅ only one import

@click.command()
@click.argument('project_name')
def install(project_name):

    """Create a project folder and set up environment."""

    setup_folder(project_name)

    create_project_files(project_name)  # ✅ only one method call




