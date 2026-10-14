# Wireshark DNS Analysis
- **Tool:** Wireshark (Windows)
- **Filter used:** dns
- **Interface:** Wi-Fi

## What I did
- I started a capture on the Wi-Fi interface in Wireshark, then applied the dns filter to analyze DNS packets.

## What I observed
- DNS means Domain Name System, A DNS query asks for the IP address of a domain, and the responsive gives that IP address.
- An A query is for IPv4, and an AAA query is for IPv6.
- I saw the domains for Google updates (update.googleapis.com) Windows activity (activity.windows.com)
  
## What I learned
- From the DNS traffic, a SOC analyst can find which websites a device is visiting.

## Key takeaway
- DNS logs help SOC analyst see which domains a device is accessing.
- DNS traffic is a useful source for finding suspicious domains.

## Questions I had
- None
