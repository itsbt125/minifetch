# wm.py
import os
import subprocess
import re

def get_wm():
    if not os.environ.get("DISPLAY"):
        return "None (SSH/TTY session)"

    session_type = os.environ.get("XDG_SESSION_TYPE", "Unknown")
    try:
        out = subprocess.check_output(
            ["xprop", "-root", "_NET_SUPPORTING_WM_CHECK"], text=True, stderr=subprocess.DEVNULL
        )
        wid_match = re.search(r"window id # (0x[0-9a-f]+)", out)
        if not wid_match:
            return f"Unknown ({session_type})"
        out2 = subprocess.check_output(
            ["xprop", "-id", wid_match.group(1), "_NET_WM_NAME"], text=True, stderr=subprocess.DEVNULL
        )
        name_match = re.search(r'"(.*)"', out2)
        wm_name = name_match.group(1) if name_match else "Unknown"

        return f"{wm_name} ({session_type})"
    except FileNotFoundError:
        return "xprop not found"
    except Exception:
        return f"Unknown ({session_type})"