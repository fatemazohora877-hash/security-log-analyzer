import pandas as pd
import os
import streamlit as st
import plotly.express as px

# Page title
st.title("Security Log Analysis Dashboard")
st.markdown("### SOC Analyst Monitoring Dashboard")

# Load CSV
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(base_dir, "logs", "sample_logs.csv")

df = pd.read_csv(csv_path)

# Sidebar
st.sidebar.success("System Status: Online")
st.sidebar.title("SOC Dashboard Filters")

selected_event = st.sidebar.selectbox(
    "Select Event Type",
    ["All"] + list(df["event"].unique())
)

# Dashboard Metrics
total_events = len(df)

failed_logins_count = len(
    df[df["status"] == "Failed"]
)

unique_ips = df["ip"].nunique()

failed_counts = (
    df[df["status"] == "Failed"]
    .groupby("ip")
    .size()
)

suspicious_ips = failed_counts[
    failed_counts >= 3
]

alert_count = len(suspicious_ips)

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Events",
    total_events
)

col2.metric(
    "Failed Logins",
    failed_logins_count
)

col3.metric(
    "Unique IPs",
    unique_ips
)

col4.metric(
    "Security Alerts",
    alert_count
)

# Failed Login Chart
failed_by_ip = (
    df[df["status"] == "Failed"]["ip"]
    .value_counts()
    .reset_index()
)

failed_by_ip.columns = [
    "IP Address",
    "Failed Attempts"
]

fig = px.bar(
    failed_by_ip,
    x="IP Address",
    y="Failed Attempts",
    title="Failed Login Attempts by IP",
    color="Failed Attempts"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# Event Distribution Pie Chart
events = df["event"].value_counts().reset_index()

events.columns = [
    "Event Type",
    "Count"
]

fig2 = px.pie(
    events,
    names="Event Type",
    values="Count",
    title="Security Event Distribution"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# Filter Logs
if selected_event != "All":
    filtered_df = df[df["event"] == selected_event]
else:
    filtered_df = df

# Security Logs
st.subheader("Security Logs")
st.dataframe(filtered_df)

# Failed Login Attempts
failed_logins = df[df["status"] == "Failed"]

st.subheader("Failed Login Attempts")
st.dataframe(failed_logins)

# Security Alerts
st.subheader("Security Alerts")

if suspicious_ips.empty:
    st.success("No suspicious activity detected.")
else:
    for ip, count in suspicious_ips.items():
        st.error(
            f"ALERT: {ip} generated {count} failed login attempts"
        )

# Generate Incident Report
report_path = os.path.join(
    base_dir,
    "reports",
    "report.txt"
)

with open(report_path, "w") as report:

    report.write("Security Incident Report\n")
    report.write("=" * 30 + "\n\n")

    if suspicious_ips.empty:
        report.write("No suspicious activity detected.\n")
    else:
        for ip, count in suspicious_ips.items():

            report.write(
                f"ALERT: {ip} generated "
                f"{count} failed login attempts\n"
            )