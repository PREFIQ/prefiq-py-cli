from setuptools import setup, find_packages

setup(
    name="prefiq",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "typer>=0.16.0",
        "rich>=13.0.0"
    ],
    entry_points={
        "console_scripts": [
            "prefiq=prefiq.cli:cli",
        ],
    },
)
