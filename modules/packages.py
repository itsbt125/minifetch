import subprocess
import shutil

def get_packages():
    managers = {
        "pacman": ["pacman", "-Qq"],
        "dpkg": ["dpkg-query", "-f", "${binary:Package}\n", "-W"],
        "dnf": ["dnf", "list", "--installed"],
        "rpm": ["rpm", "-qa"],
        "apk": ["apk", "info"],
        "xbps": ["xbps-query", "-l"],
        "qlist": ["qlist", "-I"]
    }

    for name, cmd in managers.items():
        if shutil.which(cmd[0]):
            try:
                output = subprocess.check_output(cmd, text=True)
                lines = output.splitlines()
                if name == "dnf":
                    lines = [l for l in lines if l and not l.startswith("Installed")]

                return f"{len(lines)} ({name})"
            except Exception:
                return f"{name} Error"
    return "Unknown"
