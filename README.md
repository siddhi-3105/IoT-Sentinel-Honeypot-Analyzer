# 🛡️ IoT Sentinel – Honeypot & Attack Analyzer

<p align="center">
  <strong>A Python-based IoT Security Monitoring & Attack Analysis Simulation Platform</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?logo=python" />
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-green?logo=flask" />
  <img src="https://img.shields.io/badge/Database-SQLite-lightgrey?logo=sqlite" />
  <img src="https://img.shields.io/badge/Mode-Simulation-orange" />
  <img src="https://img.shields.io/badge/Status-Development-yellow" />
</p>

## 📌 Project Overview

**IoT Sentinel – Honeypot & Attack Analyzer** is a cybersecurity educational project designed to demonstrate IoT device monitoring, honeypot-style event generation, suspicious activity analysis and security alert management.

The platform provides a centralized SOC-style dashboard where users can simulate IoT security events, analyze attack patterns, monitor virtual devices and visualize generated security alerts.

It uses Python, Flask and SQLite to process and store synthetic security events in a controlled local environment.

> ⚠️ **Disclaimer:** This project currently operates in simulation mode. It generates synthetic attack events and fictional source IP addresses. It does not capture real network traffic, deploy real honeypot services or detect actual cyberattacks.

## 🎯 Project Objectives

- Understand IoT security monitoring concepts.
- Demonstrate honeypot-style event collection.
- Simulate common IoT attack scenarios.
- Analyze suspicious activities using rule-based detection.
- Generate security alerts based on event severity.
- Monitor virtual IoT devices through a centralized dashboard.
- Understand basic SOC monitoring and incident analysis workflows.

## ✨ Key Features

| Feature | Description |
|---|---|
| 📊 SOC Dashboard | Centralized security monitoring interface |
| 🌐 IoT Device Simulation | Simulates router, smart camera and smart hub |
| 🍯 Honeypot Simulation | Generates honeypot-style security events |
| 🔍 Attack Analysis | Rule-based classification of suspicious events |
| 🔐 Brute-Force Simulation | Generates repeated failed-login scenarios |
| 🚨 Alert Management | Classifies events by severity |
| 🌍 IP Analysis | Displays synthetic source IP addresses |
| 📈 Security Analytics | Visualizes events by service and attack category |
| 🗄️ SQLite Database | Stores locally generated event history |
| 🧹 Clear Lab Data | Allows users to reset simulation history |

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Backend Framework:** Flask
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** SQLite
- **Data Visualization:** Dashboard-based analytics
- **Development Environment:** Windows

## 🏗️ Project Architecture

```text
IoT-Sentinel-Honeypot-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
│
├── database/
│   └── db_manager.py
│
├── detection/
│   └── attack_detector.py
│
├── simulation/
│   ├── attack_generator.py
│   └── device_simulator.py
│
├── templates/
│   └── index.html
│
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── app.js
```

## ⚙️ How It Works

1. **Device Simulation:** Creates three virtual IoT devices representing a home router, smart camera and smart hub.
2. **Event Generation:** Generates synthetic security events using predefined attack scenarios.
3. **Attack Detection:** Applies rule-based logic to classify generated events.
4. **Severity Classification:** Assigns Low, Medium, High or Critical severity.
5. **Database Storage:** Stores generated events in a local SQLite database.
6. **Dashboard Analysis:** Displays event statistics, source IPs, device information and security alerts.

## 🔬 Simulated Attack Scenarios

The project demonstrates the following scenarios:

- Brute-force login attempts
- Port scanning
- Suspicious login activity
- Unauthorized access attempts
- Unusual traffic bursts
- Telnet service probing
- Suspicious configuration access

All scenarios are generated locally for educational purposes.

## 💻 Installation & Setup

### Prerequisites

- Python 3.9 or later
- pip package manager
- Windows / Linux
- Git (optional)

### Step 1: Clone the Repository

```bash
git clone https://github.com/siddhi-3105/IoT-Sentinel-Honeypot-Analyzer.git
```

### Step 2: Navigate to the Project

```bash
cd IoT-Sentinel-Honeypot-Analyzer
```

### Step 3: Create a Virtual Environment

```bash
py -m venv .venv
```

### Step 4: Activate the Environment

Windows:

```bash
.venv\Scripts\activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Run the Application

```bash
python app.py
```

### Step 7: Open the Dashboard

Visit:

```text
http://127.0.0.1:8000
```

Click **Run Simulation** to generate synthetic security events.

## 📊 Dashboard Monitoring

The dashboard provides:

- Captured event statistics
- Failed login counts
- Number of simulated IoT devices
- Generated security alerts
- Events categorized by service
- Attack category distribution
- Synthetic source IP analysis
- Recent security event logs

## 🔒 Security & Data Privacy

- No real attacker IP addresses are used.
- No real credentials or personal information are included.
- No external network scanning is performed.
- The SQLite database is created locally.
- Local database files are excluded from GitHub using `.gitignore`.

## 🚀 Future Enhancements

- Real isolated IoT honeypot deployment.
- Live network traffic monitoring.
- Integration with additional threat intelligence sources.
- Advanced anomaly detection using machine learning.
- Interactive attack timeline visualization.
- SIEM integration.
- Detailed incident reports and export functionality.

These are planned enhancements and are not currently implemented.

## 🎓 Learning Outcomes

Through this project, I explored:

- IoT cybersecurity concepts.
- Honeypot architecture fundamentals.
- Attack simulation techniques.
- Rule-based threat detection.
- Security event logging and analysis.
- Flask application development.
- Database integration.
- SOC dashboard design.

## 👩‍💻 Developer

**Siddhi Kshirsagar**

B.Sc. Cyber and Digital Science Student  
Cybersecurity | SOC Analysis | Network Security | Digital Forensics

🔗 **GitHub:** https://github.com/siddhi-3105

---

⭐ If you find this project useful for learning IoT cybersecurity, consider giving the repository a star.

**Note:** This project is intended for educational, research and demonstration purposes only.
