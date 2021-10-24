"""
Functions relating to the setup of git in the new project directory.
"""
from shutil import copy
import os

from directories import directories
from .commands import VCSCommandList

def setup_vcs_or_skip(full_project_path):
    """
    Orchestrates the creation amd setup of the virtual environment using venv, or skips this step if not required.
    """
    vcs_setup = _ask_if_vcs_required()
    if vcs_setup:
        os.chdir(full_project_path)

        # Set up git by following the step outlined in the comment at the end of this file
        copy(directories['TEMPLATE_DIRECTORY'] / '.gitignore', full_project_path / '.gitignore')
        cl = VCSCommandList()
        cmd = f"{cl.init} && {cl.add} && {cl.commit} && {cl.status}"
        os.system(cmd)


    else:
        # Nothing to do. Return control to calling code.
        ...


def _ask_if_vcs_required():
    user_response = input(
        "Do you want to set up git version control for this project?\nEnter Y to create, any other key to skip:  ")
    if user_response.lower() == 'y':
        return True
    else:
        return False
