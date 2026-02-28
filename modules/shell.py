# shell.py
import os

def get_shell():
    return os.environ.get("SHELL")