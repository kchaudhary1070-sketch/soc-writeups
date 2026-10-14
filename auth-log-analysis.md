# Auth Log Analysis
- **Tool:** grep, cat (Kali Linux)
- **Log file:** auth.log

## What I did
- Created auth.log with sample login entries using echo -e.
- Read the file using cat auth.log.
- Searched for failed logins using grep "Failed" auth.log.
- Searched for activity from one IP using grep "192.168.1.50" auth.log.

## What I observed
- There were 2 failed login attempts.
- Both failed attempts came from IP 192.168.1.50, targeting the accounts root and admin.
- One login from 10.0.0.5 was successful for user khushi.

## What I learned
- I learned how to find suspicious IP addresses in logs using grep.

## Key takeaway
- Multiple failed logins from the same IP can be a sign of a brute force attack.

## Questions I had
- None
