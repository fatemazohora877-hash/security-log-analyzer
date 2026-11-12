import pandas as pd
import os
import streamlit as st
import plotly.express as px

# Page title
st.title("Security Log Analysis Dashboard")

# Load CSV
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(base_dir, "logs", "sample_logs.csv")

df = pd.read_csv(csv_path)

# Dashboard metrics

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

# Display metrics

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

st.plotly_chart(fig, use_container_width=True)

# Event Distribution Chart

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

# Display logs
st.subheader("Security Logs")
st.dataframe(df)

# Failed login detection
failed_logins = df[df["status"] == "Failed"]

st.subheader("Failed Login Attempts")
st.dataframe(failed_logins)

# Brute-force detection
failed_counts = (
    df[df["status"] == "Failed"]
    .groupby("ip")
    .size()
)

suspicious_ips = failed_counts[failed_counts >= 3]

st.subheader("Security Alerts")

if suspicious_ips.empty:
    st.success("No suspicious activity detected.")
else:
    for ip, count in suspicious_ips.items():
        st.error(
            f"ALERT: {ip} generated {count} failed login attempts"
        )