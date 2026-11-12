import pandas as pd
import os

# Load CSV
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(base_dir, "logs", "sample_logs.csv")

df = pd.read_csv(csv_path)

print("=== Security Logs ===\n")
print(df)

# Failed logins
print("\n=== Failed Login Attempts ===\n")

failed_logins = df[df["status"] == "Failed"]
print(failed_logins)

# Brute-force detection
print("\n=== Possible Brute Force Attempts ===\n")

failed_counts = (
    df[df["status"] == "Failed"]
    .groupby("ip")
    .size()
)

suspicious_ips = failed_counts[failed_counts >= 3]

print(suspicious_ips)

# Alert generation
print("\n=== Security Alerts ===\n")

if suspicious_ips.empty:
    print("No security alerts detected.")

else:
    for ip, count in suspicious_ips.items():
        print(
            f"🚨 ALERT: Suspicious activity detected from {ip}"
        )
        print(
            f"   Failed Login Attempts: {count}"
        )
        print(
            "   Possible Brute Force Attack\n"
        )