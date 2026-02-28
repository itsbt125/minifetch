# gpu.py
import subprocess

def get_gpu():
    try:
        output = subprocess.check_output(
            "glxinfo -B | grep Device", shell=True, text=True
        ).strip()
        if output.lower().startswith("device:"):
            gpu_name = output.split(":", 1)[1].strip().split("(")[0].strip()
            return gpu_name
        return "GPU info unavailable"
    except Exception:
        return "GPU info unavailable"