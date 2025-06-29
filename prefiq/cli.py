import click
from click import Command
from typing import cast
from prefiq.install import install
from prefiq.commands.app_commands import list_apps_cmd, remove_app_cmd
from prefiq.commands.new_app import new_app


@click.group()
def cli():
    pass


cli.add_command(cast(Command, install))
cli.add_command(cast(Command, new_app))
cli.add_command(cast(Command, list_apps_cmd))
cli.add_command(cast(Command, remove_app_cmd))

if __name__ == "__main__":
    cli()
