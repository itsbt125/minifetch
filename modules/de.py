# de.py
import os

def get_de():
    return os.environ.get("XDG_CURRENT_DESKTOP")