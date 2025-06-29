import os
from rich.console import Console

console = Console()

def add_license_txt(project_name: str):
    """Create a LICENSE file in the project folder."""
    content = """MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files... (trimmed for brevity)
"""

    path = os.path.join(project_name, 'LICENSE')
    with open(path, 'w') as f:
        f.write(content)

    console.log("[green] LICENSE file created[/green]")
