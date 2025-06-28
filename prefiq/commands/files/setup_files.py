# prefiq/commands/setup_files.py

from prefiq.commands.files.requirement_txt import add_requirements_txt
from prefiq.commands.files.readme_md import add_readme_md
from prefiq.commands.files.license_txt import add_license_txt
from prefiq.commands.files.gitignore_txt import add_gitignore_txt  # ✅ new

__all__ = ["create_project_files"]

def create_project_files(project_name: str):
    """Call all file-generation steps for the project."""
    add_requirements_txt(project_name)
    add_readme_md(project_name)
    add_license_txt(project_name)
    add_gitignore_txt(project_name)  # ✅ new

