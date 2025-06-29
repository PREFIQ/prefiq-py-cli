# prefiq/commands/files/requirement_txt.py

import os
from rich.console import Console

console = Console()

def add_requirements_txt(project_name: str):
    """Write predefined requirements to requirements.txt."""
    requirements = [
        "click>=8.0.0",
        "rich>=13.0.0",
        "# Add more dependencies as needed",
    ]

    path = os.path.join(project_name, 'requirements.txt')
    with open(path, 'w') as f:
        for line in requirements:
            f.write(line + "\n")

    console.log("[green] requirements.txt created with default packages[/green]")

