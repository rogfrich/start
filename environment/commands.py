class CommandList:

    def __init__(self):
        self.venv = "python3 -m venv .venv"
        self.activate = "source ./.venv/bin/activate"
        self.upgrade_pip = "python3 -m pip install --upgrade pip"
        self.install = "python3 -m pip install -r requirements-dev.txt"
