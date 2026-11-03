# IoT Sentinel – Honeypot & Attack Analyzer (Fake Lab)

A portfolio-friendly IoT security monitoring dashboard that demonstrates honeypot-style event collection, simulated IoT devices, rule-based event classification and alert analytics.

> **Important:** This is a synthetic training simulation. It does not deploy a real honeypot, expose vulnerable services, capture packets, scan networks, or detect real attackers. All source IPs are reserved documentation addresses (TEST-NET ranges), and all events are generated locally.

## Features
- Flask web dashboard with a responsive cream-and-green SOC interface
- Three virtual IoT endpoints: router, camera and smart hub
- One-click generation of synthetic attack events
- Rule-based classification for brute-force patterns, port scans, suspicious logins, unauthorized access, traffic bursts, Telnet probes and configuration access
- SQLite storage for local demo history
- Analytics for event counts, services, event categories and synthetic source IPs
- Clear demo history button

## Requirements
- Python 3.9+
- pip

## Run on Windows
1. Extract this repository.
2. Open Command Prompt in the `IoT-Sentinel-Fake-Lab` folder.
3. Create a virtual environment:

   ```bash
   py -m venv .venv
   .venv\Scripts\activate
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the application:

   ```bash
   python app.py
   ```

6. Open `http://127.0.0.1:8000` in your browser.
7. Select **Run simulation** to generate sample events.

## Project structure

```text
IoT-Sentinel-Fake-Lab/
├── app.py
├── requirements.txt
├── database/
│   └── db_manager.py
├── detection/
│   └── attack_detector.py
├── simulation/
│   ├── attack_generator.py
│   └── device_simulator.py
├── templates/
│   └── index.html
└── static/
    ├── css/style.css
    └── js/app.js
```

## How the demo works
1. The browser sends a request to `/api/simulate`.
2. Python generates fictional events and reserved example IP addresses.
3. The rule-based detector assigns a severity and explanatory rule label.
4. SQLite stores the event locally in `database/iot_sentinel_demo.db`.
5. The dashboard refreshes its counters, charts and event table from the local API.

## Safety and data
- No real credentials, user data, API keys or real attacker IPs are included.
- The SQLite database is generated automatically on first run and is excluded from Git by `.gitignore`.
- Use only in a local learning/demo environment. Do not describe generated events as real captured attacks.

## Suggested GitHub description
A Flask-based IoT honeypot-style security dashboard with synthetic attack simulation, rule-based event analysis, SQLite logging and SOC-style analytics.

## License
MIT – add your preferred license file before public distribution if required.
