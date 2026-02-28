# kernel.py
import platform

def get_kernel():
    return platform.release()