# de.py
import os

def get_de():
    current_desktop = os.environ.get("XDG_CURRENT_DESKTOP")
    if current_desktop == "KDE":
        current_desktop = "KDE Plasma"
    return current_desktop