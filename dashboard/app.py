import pandas as pd
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(base_dir, "logs", "sample_logs.csv")

df = pd.read_csv(csv_path)

print("=== Security Logs ===\n")
print(df)

print("\n=== Failed Login Attempts ===\n")

failed_logins = df[df["status"] == "Failed"]

print(failed_logins)

print("\n=== Possible Brute Force Attempts ===\n")

failed_counts = (
    df[df["status"] == "Failed"]
    .groupby("ip")
    .size()
)

suspicious_ips = failed_counts[failed_counts >= 3]

print(suspicious_ips)

print("\n=== Security Alerts ===\n")

for ip, count in suspicious_ips.items():
    print(f"ALERT: {ip} generated {count} failed login attempts")