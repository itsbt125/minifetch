# cpu.py
def get_cpu():
    cpu_name = ""
    cores = 0
    max_freq = 0.0

    # Gets data from /proc/cpuinfo
    try:
        with open("/proc/cpuinfo") as f:
            for line in f:
                if "model name" in line and not cpu_name:
                    cpu_name = line.strip().split(": ", 1)[1]
                if "processor" in line:
                    cores += 1
    except FileNotFoundError:
        return "CPU info unavailable"

    # remove anything past it like an iGPU if present
    cpu_name = cpu_name.split(" w/")[0]
    try:
        with open("/sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq") as f:
            max_freq = int(f.read().strip()) / 1000000 
    except FileNotFoundError:
        max_freq = 0.0

    return f"{cpu_name} ({cores}) @ {round(max_freq,2)}GHz"