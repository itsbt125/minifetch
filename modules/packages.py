# packages.py
import subprocess
import shutil

def get_packages():
    managers = {
        "pacman": ["pacman", "-Qq"],
        "dpkg": ["dpkg-query", "-f", "${binary:Package}\n", "-W"],
        "dnf": ["dnf", "list", "installed"],
        "rpm": ["rpm", "-qa"],
        "apk": ["apk", "info"],
        "xbps": ["xbps-query", "-l"],
        "qlist": ["qlist", "-I"]
    }

    for name, cmd in managers.items():
        if shutil.which(cmd[0]):
            try:
                output = subprocess.check_output(cmd, text=True)
                return f"{len(output.splitlines())} pkgs ({name})"
            except:
                return name, "Error"
    return "Unknown"
