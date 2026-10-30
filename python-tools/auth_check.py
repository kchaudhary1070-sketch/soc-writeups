from collections import Counter
import re

LOG_FILE = "auth.log"
THRESHOLD = 2

failed_by_ip = Counter()
success_ips = set()

with open(LOG_FILE, "r") as f:
    for line in f:
        ip_match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
        if not ip_match:
            continue
        ip = ip_match.group(1)

        if "Failed password" in line:
            failed_by_ip[ip] += 1
        elif "Accepted password" in line:
            success_ips.add(ip)

for ip, count in failed_by_ip.items():
    print(f"{ip}: {count} failed logins")

for ip, count in failed_by_ip.items():
    if count > THRESHOLD:
        print(f"ALERT: {ip} has {count} failed logins")

for ip, count in failed_by_ip.items():
    if count > THRESHOLD and ip in success_ips:
        print(f"CRITICAL: possible compromise from {ip}")
