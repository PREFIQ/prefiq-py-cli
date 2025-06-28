import click
from prefiq.install import install
from prefiq.commands.app_commands import list_apps_cmd, remove_app_cmd
from typing import cast
from click import Command


@click.group()
def cli():
    pass


cli.add_command(cast(Command, install))
cli.add_command(cast(Command, list_apps_cmd))
cli.add_command(cast(Command, remove_app_cmd))

if __name__ == "__main__":
    cli()
