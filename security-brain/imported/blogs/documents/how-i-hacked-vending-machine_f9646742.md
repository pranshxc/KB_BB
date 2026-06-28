---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-15_how-i-hacked-vending-machine.md
original_filename: 2019-04-15_how-i-hacked-vending-machine.md
title: How I hacked Vending Machine
category: documents
detected_topics:
- xss
- command-injection
- csrf
- information-disclosure
- api-security
tags:
- imported
- documents
- xss
- command-injection
- csrf
- information-disclosure
- api-security
language: en
raw_sha256: f96467420dbdcbbcd23da3b12531fc236d4e32331ed71c08a8f0e074e21e9b10
text_sha256: 357709a48274e5c62203dfc54d9a7cce36cd22a15398e468deda21d5beb1cf5a
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# How I hacked Vending Machine

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-15_how-i-hacked-vending-machine.md
- Source Type: markdown
- Detected Topics: xss, command-injection, csrf, information-disclosure, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `f96467420dbdcbbcd23da3b12531fc236d4e32331ed71c08a8f0e074e21e9b10`
- Text SHA256: `357709a48274e5c62203dfc54d9a7cce36cd22a15398e468deda21d5beb1cf5a`


## Content

---
title: "How I hacked Vending Machine"
url: "https://medium.com/@valeriyshevchenko/how-i-hacked-vending-machine-5b5a80bd5ffe"
authors: ["Valeriy Shevchenko (@Krevetk0Valeriy)"]
bugs: ["Violation of secure design principles"]
bounty: "300"
publication_date: "2019-04-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5309
scraped_via: "browseros"
---

# How I hacked Vending Machine

How I hacked Vending Machine
Valeriy Shevchenko
Follow
3 min read
·
Apr 15, 2019

8

In our day's many things trying to be "smart". In that article, I wanna share an interesting story about smart vending machines. In order to use it, you need to register an account and link a credit card. Once I accidentally managed to open the menu of the operating system of one "smart" vending machine screen. It was just basic windows submenu with a swipe from the right of the screen.

Press enter or click to view image in full size

Actually, it was a Windows 10.

Press enter or click to view image in full size

You might think — well what’s wrong with that. What’s the impact of that?
But in fact, with the ability to open the Windows menu opened a huge number of vectors to attack. The user privilege level at this terminal was quite high.

It was possible to:

Install Mimikatz and find out the password when rebooting the terminal for the next login. I did not do this. But it was the simplest and most obvious.
Use the installed TeamViewer application, it was possible to secretly monitor user activity and collect information about taste preferences. I’ve checked this vector of the attack on one of the company’s employees. Data was cached in my TeamViewer session.

3. Install the modification on the fingerprint scanner and collect employee fingerprints. This feature works only for those users who have access to the refrigerator without an identification card. This attack vector was not exploited, but the information from the device list allowed the attack to be executed.

Press enter or click to view image in full size

4. Set the redirection of all traffic in the connection settings. This attack has not been verified. Probably traffic is going over https.
5. Redirect the user to the login page with a corporate/facebook account on the phishing site. The level of trust of that device is high if it's installed in the office. And it is likely that a large number of users will expose accounts as is regularly done on legitimate network printers within the companies.

Get Valeriy Shevchenko’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Reward: 10 Euro

Timeline:

30–11–2018 — Discovered bug, reported to Redacted.com without any technical details.
03–12–2018 — Bug confirmed without having any details about that issue ?!
04–12–2018 — Reported technical details to Redacted.com
11–12–2018 — Bug confirmed and already planned with next updates.
28–01–2019 — Requested update
20–02–2019 — Reported to a new person in Redacted.com again about that issue
28–02–2019 — Redacted.com fixed the bug with new application screen locker
18–03–2019 — Reward amount was transferred to my vending machine card

PS: In the process of checking the amount on my card, I discovered the possibility of an attack on a user through CSRF + XSS vector in the user’s personal account in the web app. Many things could be possible with that attack vector — account information disclosure, account takeover, etc. This situation surprised me greatly. Because that services linked real payment cards with all users accounts.

Press enter or click to view image in full size

Due to the complexity of communication, I tried to find the security engineer of the main company and inform him about the problems existing in the subsidiary company.

This story ended much faster and the total reward for all the problems found was revised.

Reward: 300 Euro Amazon gift voucher

Timeline:

20–03–2019 — Made contact with security engineer in Linkedin from redacted-main.com
20–03–2019 — Reported technical details to Redacted-main.com
20–03–2019 — Bug confirmed.
22–03–2019 — Informed about revising reward and planned fixes.
25–03–2019 — Reward amount was transferred.
