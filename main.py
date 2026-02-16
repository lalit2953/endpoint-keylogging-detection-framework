print("DEBUG: FILE IS RUNNING")
from core.detector import detect_suspicious_activity
from colorama import Fore, init
import time

init(autoreset=True)

print("=== Endpoint Keylogging Detection Framework ===")
print("Monitoring system for suspicious input capture behavior...\n")

while True:
    alerts = detect_suspicious_activity()

    if alerts:
        for alert in alerts:
            print(Fore.RED + "[ALERT] " + alert["description"])
            print(Fore.YELLOW + f"Process: {alert['process']['name']}")
            print(Fore.YELLOW + f"PID: {alert['process']['pid']}")
            print("-" * 50)
    else:
        print(Fore.GREEN + "System Normal - No Suspicious Activity")

    time.sleep(10)

