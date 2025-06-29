from setuptools import setup, find_packages

setup(
    name="prefiq",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click>=8.0.0",
        "rich>=13.0.0"
    ],
    entry_points={
        "console_scripts": [
            "prefiq=prefiq.cli:cli",
        ],
    },
    package_data={
        "prefiq": [
            "templates/prefentity/*",
            "templates/app_full/*",
        ],
    },
)