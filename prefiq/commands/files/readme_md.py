# prefiq/commands/files/readme_md.py

import os
from rich.console import Console

console = Console()

def add_readme_md(project_name: str):
    """Create a pre-filled README.md in the project folder."""
    content = f"""# {project_name}

Welcome to `{project_name}`! This project was created using the [prefiq CLI].

## Features

- Virtual environment setup
- Pre-configured requirements.txt
- Basic project structure
"""

    path = os.path.join(project_name, 'README.md')
    with open(path, 'w') as f:
        f.write(content)

    console.log("[green]📝 README.md created with project info[/green]")
