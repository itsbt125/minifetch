# gpu.py
import os
import subprocess

def get_gpu():
    if not os.environ.get("DISPLAY"):
        return "GPU info unavailable"

    try:
        output = subprocess.check_output(
            ["glxinfo", "-B"], text=True, stderr=subprocess.DEVNULL
        )
        for line in output.splitlines():
            if line.strip().lower().startswith("device:"):
                gpu_name = line.split(":", 1)[1].split("(")[0].strip()
                return gpu_name or "GPU info unavailable"
        return "GPU info unavailable"
    except FileNotFoundError:
        return "glxinfo not found"
    except Exception:
        return "GPU info unavailable"