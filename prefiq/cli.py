import click
from prefiq.install import install


@click.group()
def cli():
    """Prefiq CLI"""


cli.add_command(install)

if __name__ == "__main__":
    cli()
