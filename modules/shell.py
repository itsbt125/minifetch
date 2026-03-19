# shell.py
import os

def get_shell():
    return os.path.basename(os.environ.get("SHELL"))
