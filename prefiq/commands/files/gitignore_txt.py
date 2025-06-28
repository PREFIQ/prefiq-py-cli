import os
from rich.console import Console

console = Console()

def add_gitignore_txt(project_name: str):
    """Create a .gitignore file with common Python ignores."""
    content = """# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Virtual environment
venv/
.env/

# IDE and editor folders
.vscode/
.idea/

# Log files
*.log

# OS files
.DS_Store
Thumbs.db
"""

    path = os.path.join(project_name, '.gitignore')
    with open(path, 'w') as f:
        f.write(content)

    console.log("[green]🛑 .gitignore file created[/green]")
