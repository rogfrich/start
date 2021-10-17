import sys
import os
from pathlib import Path
from typing import List

STANDARD_CODE_DIR = Path('/Users/rich/code')

print(Path.cwd())


def main():

    # Basic setup of the new project directory
    project_dir_name: str = get_new_dir_name_from_args(sys.argv)
    parent_project_folder: Path = set_project_parent_folder(STANDARD_CODE_DIR)
    full_project_path: Path = create_full_project_path(parent_project_folder, project_dir_name)
    create_project_folder(full_project_path)

    # Set up Python virtual environment
    ...

    # Set up git
    ...

def create_full_project_path(parent_project_folder, project_dir_name):
    """
    Create a fully qualified path for the new project dir.
    """
    full_project_path = Path(parent_project_folder / project_dir_name)
    return full_project_path


def create_project_folder(full_project_path: Path):
    """
    Try to create the new project dir to the filesystem. Exit out if the new dir already exists.
    """
    try:
        Path.mkdir(full_project_path)
    except FileExistsError:
        print(f"Folder already exists. Exiting")
        sys.exit()


def get_new_dir_name_from_args(args: List) -> str:
    """
    There should only be one CLI argument, which is the of the new project dir.
    """
    if not 1 < len(args) < 3:
        raise ValueError('Incorrect number of arguments. Usage: "start <project directory>"')

    return args[1]


def set_project_parent_folder(standard_code_directory: Path) -> Path:
    """
    In general, we want to create new coding projects in ~/code. Check that the script has been run from
    that folder, and if not then check that's what the user intended.
    """
    if not Path.cwd() == standard_code_directory:
        create_here_query = input(
            f"Enter Y to create project directory in {Path.cwd()}, or any other key to create in ~/code >  ")
        if create_here_query.lower() == 'y':
            return Path.cwd()
        else:
            return standard_code_directory
    else:
        return standard_code_directory


if __name__ == "__main__":
    main()
    ...
