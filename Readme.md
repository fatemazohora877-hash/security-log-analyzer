Security Log Analysis & SIEM Dashboard
Overview
The Security Log Analysis & SIEM Dashboard is a Python-based cybersecurity project designed to simulate Security Operations Center (SOC) workflows. The dashboard ingests security logs, analyzes authentication events, detects suspicious activity, generates alerts, and visualizes security data through interactive charts and metrics.

This project demonstrates practical cybersecurity skills including log analysis, threat detection, incident monitoring, data visualization, and security reporting.

Features
-Security Log Ingestion
-Failed Login Detection
-Brute Force Attack Detection
-Automated Security Alerts
-Interactive Dashboard
-KPI Metrics
-Event Distribution Analysis
-Incident Report Generation
-Event Filtering
-Data Visualization with Plotly
-SOC-Style Monitoring Interface
Technologies Used
-Python
-Pandas
-Streamlit
-Plotly
-CSV
-OS Module


Project Structure
security-log-analyzer/
│
├── dashboard/
│   └── app.py
│
├── logs/
│   └── sample_logs.csv
│
├── reports/
│   └── report.txt
│
├── screenshots/
│   ├── dashboard-overview.png
│   ├── failed-login-chart.png
│   ├── event-distribution.png
│   ├── security-alerts.png
│   └── filters-sidebar.png
│
├── requirements.txt
└── README.md
Installation
Clone the repository:

git clone https://github.com/fatemazohora877-hash/security-log-analyzer
cd security-log-analyzer
Create a virtual environment:

python -m venv venv
Activate the environment:

Windows
.\venv\Scripts\Activate
Install dependencies:

pip install -r requirements.txt

Requirements
-pandas
-streamlit
-plotly
-matplotlib

Running the Dashboard

Start the Streamlit application:

streamlit run dashboard/app.py
or

python -m streamlit run dashboard/app.py
Open your browser and navigate to:

http://localhost:8501

Sample Security Events

The dashboard analyzes events including:

-Login Success
-Login Failed
-File Access
-Password Change

Example log entry:

timestamp,ip,event,status
2026-11-01 08:01:10,192.168.1.11,Login Failed,Failed
Detection Logic
The system identifies suspicious activity by analyzing authentication logs and counting failed login attempts.

Current detection rule:

3 or more failed login attempts from the same IP address
Example alert:

ALERT: 192.168.1.11 generated 3 failed login attempts
Potential brute-force attacks are highlighted on the dashboard and included in generated reports.

Dashboard Metrics
The dashboard displays:

-Total Events
-Failed Logins
-Unique IP Addresses
-Security Alerts
-These KPIs provide an immediate overview of current security activity.

Incident Reporting
The application automatically generates incident reports and stores them in:

reports/report.txt
Example:

Security Incident Report
==============================

ALERT: 192.168.1.11 generated 3 failed login attempts

Skills Demonstrated

-Security Monitoring
-Log Analysis
-Threat Detection
-Incident Response
-SIEM Concepts
-Python Programming
-Data Visualization
-Security Reporting
-SOC Analyst Workflows
-Dashboard Development

Future Improvements

-Real-Time Log Monitoring
-Windows Event Log Integration
-Linux Syslog Integration
-Email Alert Notifications
-Threat Intelligence Feed Integration
-User Authentication
-Geolocation of Suspicious IPs
-PDF Report Generation
-Microsoft Sentinel Integration
-Splunk Integration

Disclaimer
This project is intended for educational and cybersecurity learning purposes only. The sample data used within the dashboard does not contain real user information or production security logs.

Author
Fatema Tuz Zohora
Cyber Security Student
University of Lancashire
GitHub: https://github.com/fatemazohora877-hash