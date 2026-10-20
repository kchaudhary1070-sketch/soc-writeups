# Google Phishing Quiz (Jigsaw): 10/10

**Date:** 20 October 2026
**Platform:** phishingquiz.withgoogle.com (Google Jigsaw)
**Result:** 10/10 correct

## Objective

Practice identifying phishing emails and SMS messages. This is a first step in SOC L1 alert triage and relates to MITRE ATT&CK technique T1566 (Phishing).

## Questions and Key Indicators

| # | Sample | Verdict | Key Indicators |
|---|---|---|---|
| 1 | Google Doc share notification from `luke.json8000@gmail.com` | Phishing | Look-alike domain `drive--google.com` (double hyphen) |
| 2 | Coca-Cola promotional email | Phishing | Random sender domain; all text embedded in an image to evade text-based filters |
| 3 | PayPal-style invoice ($600) | Phishing | Fake "note from seller" with 24-hour urgency; call-back phone number used to continue the scam |
| 4 | Dropbox notification from `no-reply@dropboxmail.com` | Legitimate | Unusual but legitimate sender domain; link uses HTTPS and resolves to `dropbox.com` |
| 5 | SMS containing a "Google verification code" | Phishing | Requests a 2-Step Verification code; such codes should only be shared during a login the user initiated |
| 6 | Google security alert from `google.support` | Phishing | `google.support` is not a Google domain; link points to a subdomain of `ml-security.org` |
| 7 | Google warning email with "Change password" link | Phishing | Link uses `tinyurl.com` to redirect and hide the true destination |
| 8 | Netflix SMS from `netflix@mnasdfkjasdf.org` | Phishing | Link `netflix.com.onlinehome.us`; the registered domain is `onlinehome.us`, and `netflix.com` is only a subdomain |
| 9 | "Free Pixel 7 Pro - Confirmation Interview" email | Phishing | Too-good-to-be-true offer; sender display name styled to look like Google; "Click here to join" link requests account access |
| 10 | SMS from `69877` about a package delay | Legitimate | Link was valid. Not every SMS is phishing, so the link must be verified rather than assumed malicious |

## Key Takeaways

- The registered domain is the rightmost part of the hostname before the path (for example, `onlinehome.us` in `netflix.com.onlinehome.us`).
- The sender display name and the actual email address can differ. Always verify the address.
- Urgency, fear, and requests for codes or account access are red flags.
- URL shorteners such as `tinyurl.com` hide the true destination.
- An unusual domain is not automatically malicious. Evaluate multiple indicators together.
- When in doubt, do not click links. Navigate to the official website or app directly.

## Screenshot

Completion screen: `screenshots/phishing-quiz-result.png`
