import json
from datetime import datetime
from utils.process_scanner import scan_processes

ALERT_FILE = "data/alerts.json"

def detect_suspicious_activity():
    findings = scan_processes()
    alerts = []

    for process in findings:
        if "key" in str(process["cmdline"]).lower():
            alert = {
                "timestamp": str(datetime.now()),
                "risk": "HIGH",
                "description": "Possible keylogging activity detected",
                "process": process
            }
            alerts.append(alert)

    if alerts:
        save_alerts(alerts)

    return alerts


def save_alerts(alerts):
    try:
        with open(ALERT_FILE, "r") as f:
            existing = json.load(f)
    except:
        existing = []

    existing.extend(alerts)

    with open(ALERT_FILE, "w") as f:
        json.dump(existing, f, indent=4)

