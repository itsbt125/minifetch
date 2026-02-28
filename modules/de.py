# de.py
import os

def get_de():
    if not os.environ.get("DISPLAY"):
        return "None (SSH/TTY session)"

    current_desktop = os.environ.get("XDG_CURRENT_DESKTOP")
    if current_desktop:
        if current_desktop.lower() == "kde":
            return "KDE Plasma"
        return current_desktop
    return "None"