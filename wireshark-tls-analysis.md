## Tool
Wireshark

## Filter used
tcp

## Interface
Wi-Fi

## What I did
- Started capture on Wi-Fi interface.
- Opened a website in the browser.
- Applied the tcp filter.
- Stopped the capture after a few seconds.

## What I observed
- In TLS Application Data, the protocol shown is Hypertext Transfer Protocol.
- Content type is Application Data and version is TLS 1.2 (0x0303).
- Length is 96.
- Encrypted Application Data shows encrypted bytes in hex form, not readable text.

## What I learned
TLS encrypts the data, so even though Wireshark shows the protocol, the page content is not readable.

## Key takeaway
Encrypted traffic still shows connection details like the port (443) and TLS version, which helps SOC analysts see that a device is connecting to a service.

## Questions I had
None
