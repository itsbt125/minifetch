def get_memory():
    with open("/proc/meminfo") as f:
        meminfo = f.read()

    mem_total = int(next(line for line in meminfo.splitlines() if "MemTotal:" in line).split()[1])
    mem_available = int(next(line for line in meminfo.splitlines() if "MemAvailable:" in line).split()[1])

    used = mem_total - mem_available  # in kB
    used_gb = used / (1024**2)
    total_gb = mem_total / (1024**2)
    percent_used = (used / mem_total) * 100

    return f"{used_gb:.2f} GB / {total_gb:.2f} GB ({percent_used:.0f}%)"