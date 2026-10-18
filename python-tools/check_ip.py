ips = {}
with open("auth.log") as f:
    for line in f:
        if "Failed" in line:
            words = line.split()
            ip = words[-1]
            ips[ip] = ips.get(ip, 0) + 1

limit = 2
for ip, count in ips.items():
    if count >= limit:
        print("ALERT:", ip, "has", count, "failed logins")