import psutil

def scan_processes():
    suspicious = []

    for proc in psutil.process_iter(['pid', 'name', 'exe', 'cmdline']):
        try:
            name = proc.info['name']
            cmdline = proc.info['cmdline']

            if name and "python" in name.lower():
                suspicious.append({
                    "pid": proc.info['pid'],
                    "name": name,
                    "cmdline": cmdline
                })

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return suspicious

