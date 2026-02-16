# endpoint-keylogging-detection-framework
Python-based Endpoint Keylogging Detection Framework that monitors running processes using psutil and applies heuristic behavioral analysis to identify potential keyboard input capture activity. Generates real-time alerts for suspicious processes and demonstrates core EDR concepts such as process enumeration, runtime monitoring,&amp; anomaly detection.

# 📘 Endpoint Keylogging Detection Framework

## 📌 Overview

The **Endpoint Keylogging Detection Framework** is a Python-based behavioral monitoring system designed to detect potential keylogging activity using heuristic runtime analysis.

This project demonstrates fundamental **Endpoint Detection and Response (EDR)** concepts by monitoring active processes and identifying suspicious keyboard input capture behavior.

The system operates in **user mode** and continuously scans running processes using the `psutil` library. When potentially suspicious behavior is detected, it generates structured real-time alerts.

---

## 📑 Table of Contents

* [Overview](#-overview)
* [Features](#-features)
* [Technologies Used](#-technologies-used)
* [Installation](#-installation)
* [Usage](#-usage)
* [Project Structure](#-project-structure)
* [How It Works](#-how-it-works)
* [Configuration](#-configuration)
* [Limitations](#-limitations)
* [Troubleshooting](#-troubleshooting)
* [Contributors](#-contributors)
* [License](#-license)
* [Disclaimer](#-disclaimer)

---

## 🚀 Features

* ✅ Real-time process enumeration
* ✅ Heuristic-based detection logic
* ✅ Suspicious process alerting
* ✅ Controlled keylogging simulation for testing
* ✅ Lightweight and modular architecture

---

## 🛠 Technologies Used

* **Python 3.x**
* **psutil**
* **Windows OS**
* **pynput** (for testing simulation only)

---

## 💾 Installation

```bash
git clone https://github.com/yourusername/endpoint-keylogging-detection-framework.git
cd endpoint-keylogging-detection-framework
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## ▶️ Usage

### Run the Monitoring Engine

```bash
python main.py
```

The system will begin scanning active processes in real time.

---

### (Optional) Run the Keylogging Simulation (Testing Only)

Open a separate terminal and run:

```bash
python test_key_capture.py
```

If suspicious behavior is detected, an alert will be displayed in the monitoring terminal.

---

## 📂 Project Structure

```
endpoint-keylogging-detection-framework/
│
├── main.py                  # Core monitoring engine
├── test_key_capture.py      # Controlled keylogging simulation
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 🔎 How It Works

1. The monitoring engine continuously enumerates active processes using `psutil`.
2. Each process is evaluated using heuristic detection rules.
3. Processes exhibiting suspicious behavior patterns (e.g., potential keyboard capture indicators) trigger alerts.
4. Alerts are printed in structured format for analysis.

This approach simulates basic EDR detection logic in user mode.

---

## ⚙️ Configuration

Currently, the framework uses built-in heuristic logic defined inside `main.py`.

You can modify detection thresholds and behavioral rules directly within the script to experiment with:

* Detection sensitivity
* Process filtering logic
* Alert formatting

---

## ⚠️ Limitations

* User-mode detection only
* No kernel-level monitoring
* Potential for false positives
* Does not perform automated response actions
* Windows-focused implementation

---

## 🛠 Troubleshooting

**Issue:** `ModuleNotFoundError: psutil`
**Solution:**
Ensure your virtual environment is activated and dependencies are installed:

```bash
pip install -r requirements.txt
```

---

**Issue:** Monitoring does not detect test script
**Solution:**
Ensure the test script is running simultaneously in a separate terminal.

---

## 👥 Contributors

* Project Author

(Feel free to add contributors here.)

---

## 📜 License

This project is released under the MIT License.
(You may replace this with your preferred license.)

---

## ⚖️ Disclaimer

This project is developed strictly for **educational and defensive cybersecurity research purposes**.

It is not intended for malicious use.
