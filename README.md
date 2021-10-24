# start
A script to scaffold new projects quickly and easily.

## Usage
`start <project name>` to create a new project. This will:
- Create a directory called `<project name>`. Since most new projects will be in the `~/code` directory, 
  the script will prompt for confirmation if it is run from any other directory. If this happens, press `y` 
  to continue in the directory from which it was called, or any other key to create the new directory in 
  `~/code` regardless of where it was called from.
- Create a README.md file with the project directory name as the header.
- Ask whether to set up a Python virtual environment (see below).
- Ask whether to set up git (see below).

## Python virtual environments
If the option to set up a virtual environment is selected, then the script will:
- Copy the template `requirements.txt` and `requirements-dev.txt` from `~/start_templates` to the new 
  project directory. These files specify Python libraries that I'm likely to want:
  - pytest
  - black
- Create an empty `.env` file in the new project directory.
- Create a `venv` virtual environment in the new project directory called `.venv`.

## Version control (git)
If the option to set up git version control is selected, then the script will:
- Copy the template `.gitignore` file from `~/start_templates` to the new project directory.
- Initialise git in the new project directory.
- `git add` all the files in the new project directory (unless they're included in `.gitignore`).
- `git commit` with a default message. 


