# terminal.py
import os
import subprocess

def get_terminal():
    shell_pid = os.getppid()
    parent_pid = int(subprocess.check_output(["ps", "-o", "ppid=", "-p", str(shell_pid)], text=True).strip())
    terminal = subprocess.check_output(["ps", "-o", "cmd=", "-p", str(parent_pid)], text=True).strip()
    return terminal

print(get_terminal())