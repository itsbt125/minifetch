# uptime.py
def get_uptime():
    with open("/proc/uptime") as f:
        total_seconds = int(float(f.readline().split()[0]))

    days = total_seconds // 86400
    hours = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60

    parts = []
    if days:
        parts.append(f"{days}d")
    if hours:
        parts.append(f"{hours}hr" if hours == 1 else f"{hours}hrs")
    if minutes:
        parts.append(f"{minutes}min" if minutes == 1 else f"{minutes}mins")

    return " ".join(parts) if parts else "0mins"
