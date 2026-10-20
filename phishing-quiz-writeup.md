# Google Phishing Quiz (Jigsaw): 10/10

**Date:** 20 Oct 2026
**Platform:** phishingquiz.withgoogle.com (Google Jigsaw)
**Result:** 10/10 correct

## Purpose

Phishing email aur SMS ko pehchanne ka practice karna. Ye SOC L1 triage ka pehla step hai, aur MITRE ATT&CK technique T1566 (Phishing) se related hai.

## Questions and key indicators

| # | Sample | Verdict | Key indicators |
|---|---|---|---|
| 1 | Google Doc share email from `luke.json8000@gmail.com` | Phishing | Look-alike domain `drive--google.com` (double hyphen) |
| 2 | Coca-Cola promo email | Phishing | Random sender domain; poora text image me tha taaki filters bypass ho |
| 3 | PayPal-style invoice ($600) | Phishing | Fake "note from seller", 24 ghante ka urgency, call karne ka phone number |
| 4 | Dropbox notification (`no-reply@dropboxmail.com`) | Legitimate | Domain unusual hai, lekin legit hai. Link `dropbox.com` pe HTTPS se jaata hai |
| 5 | SMS with "Google verification code" | Phishing | Code maanga gaya; 2-Step codes sirf wahi share karo jo tumne login start kiya ho |
| 6 | Google security alert from `google.support` | Phishing | `google.support` Google ka domain nahi hai; link `ml-security.org` ke subdomain pe jaata hai |
| 7 | Google warning email with "Change password" | Phishing | Link `tinyurl.com` redirect karta hai, asli destination chhupa hai |
| 8 | Netflix SMS (`netflix@mnasdfkjasdf.org`) | Phishing | Link `netflix.com.onlinehome.us`: asli domain `onlinehome.us` hai, `netflix.com` sirf subdomain hai |
| 9 | "Free Pixel 7 Pro - Confirmation Interview" | Phishing | Too-good-to-be-true offer; sender ka naam Google jaisa tha; "Click here to join" link account access maangta hai |
| 10 | SMS from `69877` about package delay | Legitimate | Link real tha. Har SMS phishing nahi hota, isliye verify karna zaroori hai |

## Key takeaways

- Asli domain check karo: URL ke `/` se pehle ka aakhri hissa (jaise `onlinehome.us`) hi asli domain hai.
- Sender ka display naam aur asli email address alag ho sakte hain. Address check karo.
- Urgency, dar, aur code ya account access maangne wali requests red flags hain.
- Shortened links (jaise tinyurl) asli destination chhupa dete hain.
- Unusual domain ka matlab hamesha fake nahi hota. Kai signals ek saath dekho.
- Shak ho to link click karne ke bajay official website ya app se directly login karo.

## Screenshot

Completion screen: `screenshots/phishing-quiz-result.png`
