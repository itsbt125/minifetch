# wm.py
import subprocess, re

def get_wm():
    try:
        out = subprocess.check_output(["xprop", "-root", "_NET_SUPPORTING_WM_CHECK"], text=True)
        wid = re.search(r"window id # (0x[0-9a-f]+)", out)
        if not wid:
            return None
        out2 = subprocess.check_output(["xprop", "-id", wid.group(1), "_NET_WM_NAME"], text=True)
        name = re.search(r'"(.*)"', out2)
        return name.group(1) if name else None
    except:
        return None