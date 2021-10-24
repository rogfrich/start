"""
Functions relating to the setup of a new virtual environment for the new project.
"""
import os
from shutil import copy
from directories import directories
from pathlib import Path

from .commands import CommandList

def setup_environment_or_skip(full_project_path):
    """
    Orchestrates the creation amd setup of the virtual environment using venv, or skips this step if not required.
    """
    venv_setup = _ask_if_venv_required()
    if venv_setup:
        # Proceed to set up the environment
        # Copy requirements files
        copy(directories['TEMPLATE_DIRECTORY'] / 'requirements.txt', full_project_path / 'requirements.txt')
        copy(directories['TEMPLATE_DIRECTORY'] / 'requirements-dev.txt', full_project_path / 'requirements-dev.txt')

        # Create.env file
        Path.touch(full_project_path / '.env')

        # Create venv environment
        os.chdir(full_project_path)
        cl = CommandList()
        cmd = f"{cl.venv} && {cl.activate} && {cl.upgrade_pip} && {cl.install}"

        os.system(cmd)


    else:
        # Nothing to do. Return control to calling code.
        ...


def _ask_if_venv_required():
    user_response = input(
        "Do you want to set up a virtual environment for this project?\nEnter Y to create, any other key to skip:  ")
    if user_response.lower() == 'y':
        return True
    else:
        return False
