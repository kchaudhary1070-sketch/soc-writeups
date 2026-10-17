## Summary
Two failed login attempts from IP 192.168.1.50 targeted the root and admin accounts in auth.log. One successful login for user khushi from IP 10.0.0.5 was also found.

## Logs checked
auth.log (3 lines), checked with `cat -n`, `grep "Failed"`, `grep "192.168.1.50"`, and `grep "Accepted"`.

## Timeline
- Line 1: Failed password for root from 192.168.1.50
- Line 2: Accepted password for khushi from 10.0.0.5
- Line 3: Failed password for admin from 192.168.1.50

This sample log has no timestamps, so the order is based on line numbers.

## Suspicious IP
192.168.1.50 made 2 failed login attempts against two different accounts (root and admin).

## Affected accounts
- root: failed login attempt
- admin: failed login attempt
- khushi: successful login from 10.0.0.5

## Actions I would take
- Block IP 192.168.1.50 at the firewall.
- Check whether khushi normally logs in from 10.0.0.5 and confirm that the login was legitimate.
- Reset the root and admin passwords and use strong passwords.
- Check other logs for more activity from 192.168.1.50.

## Conclusion
Multiple failed logins from one IP against different accounts look like a brute force attempt. The successful login for khushi from a different IP needs verification. There is no confirmed compromise yet.