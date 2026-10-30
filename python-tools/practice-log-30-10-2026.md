# Practice Log: Wireshark and Windows Event Logs

## 1. Wireshark HTTP Traffic
- Captured traffic on: [Wi-Fi / Ethernet]
- Display filter used: `http`
- Action: opened http://neverssl.com in the browser
- Observed: one GET request and one 200 OK response
- Other observation: request to api.ipify.org (public IP check service). Needs process-level verification before concluding anything.

## 2. Windows Security Log (Event ID 4625)
- Action: locked the PC and entered a wrong password
- Observed: Event ID 4625, Logon Type 2 (interactive), failure reason "An error occurred during logon"
- Note: a single failed event is not a brute-force pattern. SOC analysts look for repeated failures from the same account or source.

## 3. Sysmon Event ID 1 (Process Creation)
- Observed: splunk-powershell.exe started by splunkd.exe (service mode) from the expected Splunk install path
- Verdict: Benign, after checking path, parent process, and command line
- Note: Event ID 3 (network connections) was empty because Sysmon config does not log network events by default.
