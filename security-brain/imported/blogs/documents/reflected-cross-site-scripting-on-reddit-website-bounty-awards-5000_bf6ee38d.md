---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-21_reflected-cross-site-scripting-on-reddit-website-bounty-awards-5000.md
original_filename: 2023-02-21_reflected-cross-site-scripting-on-reddit-website-bounty-awards-5000.md
title: Reflected Cross site scripting on reddit website (bounty awards $5000)
category: documents
detected_topics:
- xss
- command-injection
- password-reset
- mobile-security
tags:
- imported
- documents
- xss
- command-injection
- password-reset
- mobile-security
language: en
raw_sha256: bf6ee38d66e6d2b3fed7dff925c722ac4d878bfe5a29f296cce44ec2f37f6128
text_sha256: da4c46f2583f7c3373211b886ba161ecc4cb38e846c41a1675c4c02456b885cc
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# Reflected Cross site scripting on reddit website (bounty awards $5000)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-21_reflected-cross-site-scripting-on-reddit-website-bounty-awards-5000.md
- Source Type: markdown
- Detected Topics: xss, command-injection, password-reset, mobile-security
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `bf6ee38d66e6d2b3fed7dff925c722ac4d878bfe5a29f296cce44ec2f37f6128`
- Text SHA256: `da4c46f2583f7c3373211b886ba161ecc4cb38e846c41a1675c4c02456b885cc`


## Content

---
title: "Reflected Cross site scripting on reddit website (bounty awards $5000)"
url: "https://jjainam16.medium.com/reflected-cross-site-scripting-on-reddit-website-bounty-awards-5000-99fa639cdd7"
authors: ["ShuttlerTech"]
programs: ["Reddit"]
bugs: ["Reflected XSS"]
bounty: "5,000"
publication_date: "2023-02-21"
added_date: "2023-02-26"
source: "pentester.land/writeups.json"
original_index: 1504
scraped_via: "browseros"
---

# Reflected Cross site scripting on reddit website (bounty awards $5000)

Reflected Cross site scripting on reddit website (bounty awards $5000)
ShuttlerTech
Follow
2 min read
·
Feb 21, 2023

121

4

Press enter or click to view image in full size

Hello, Hunters. I know You are here because you are struggling or want to advance in your career. Believe me, things take time. Be consistent, continue to learn, and never deceive yourself. If you follow this three mantras, you will undoubtedly achieve success.

Any confusion related to your finding or career Connect with me 1:1 click on 👉🏻(TOPMATE)

For this write you need to understand it is not luck or something like that i have recon in very deep sometime you need to grind yourself by doing recon activity…….

Let’s start,

Get ShuttlerTech’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Step to Reproduce:

Visited reddit website.
register yourself & you will be going to get one email verification link on registered email.
copy that link on browser and add payload after /Verification as shown https://www.reddit.com/verification/asd',%20alert(document.location),%20%27
It will be pop up with two option verify email or cancel.
click on verify email xss payload will execute.
Press enter or click to view image in full size
Impact

An attacker can use XSS to steal your cookies, steal sessions, download malware onto your system, and send a custom request. The attacker can socially engineer users by redirecting them from the real website to a fake one, and there are numerous other attack scenarios that an expert attacker can perform with XSS. It is also possible to inject HTML, which will change the original page.

Although finding this is easy but you need to learn from this write up that it can be a huge loss for the company if someone steals your cookies, steal sesion and able to download onto your system.

Thank you for reading !! hope you get to learn some tricks.

Subscribe to the Shuttlertech YouTube channel for more of this type of content and to watch live POCs & To advance your career connect with me 1:1 over topmate .
To encourage me to write more, follow me on medium and click the clap icon.
