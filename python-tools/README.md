# IP Failed Login Alert

A small Python script that reads an auth log, counts failed login attempts for each IP address, and prints an alert when an IP reaches a set limit.

## Files

- `check_ip.py`: counts failed logins per IP and prints an ALERT when the count is at or above the limit.
- `auth.log`: sample log with 3 lines, used for testing.

## How to run

Run this command inside the `python-tools` folder:

```
python check_ip.py
```

## Example output

```
ALERT: 192.168.1.50 has 2 failed logins
```

## How it works

1. Reads each line of `auth.log`.
2. If the line contains "Failed", takes the last word as the IP address.
3. Counts failed attempts per IP in a dictionary.
4. Prints an alert for each IP whose count is greater than or equal to `limit` (set to 2).