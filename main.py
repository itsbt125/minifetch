import json
import time
from pathlib import Path
from modules.os import get_os
from modules.kernel import get_kernel
from modules.uptime import get_uptime
from modules.shell import get_shell
from modules.cpu import get_cpu
from modules.gpu import get_gpu
from modules.ascii.art import get_ascii_art

BASE_DIR = Path(__file__).parent
FUNCTION_MAP = {
    "get_os": get_os,
    "get_kernel": get_kernel,
    "get_cpu": get_cpu,
    "get_gpu": get_gpu,
    "get_uptime": get_uptime,
    "get_shell": get_shell
}

# load modules from JSON
with open(BASE_DIR / "modules.json") as f:
    modules_data = json.load(f)

ascii_art = get_ascii_art(len(modules_data))
max_width = max(len(line) for line in ascii_art)

for art_line, module in zip(ascii_art, modules_data):
    func = FUNCTION_MAP.get(module["function"])
    result = func() if func else "Function not found, check function map if you've modified something."
    print(f"{art_line.ljust(max_width)} | {module['name']}: {result}")
