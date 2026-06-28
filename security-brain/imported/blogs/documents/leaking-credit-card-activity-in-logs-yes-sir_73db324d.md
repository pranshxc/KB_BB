---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-03_leaking-credit-card-activity-in-logs-yes-sir.md
original_filename: 2020-12-03_leaking-credit-card-activity-in-logs-yes-sir.md
title: Leaking Credit card Activity in logs? Yes Sir!
category: documents
detected_topics:
- command-injection
- information-disclosure
- mobile-security
tags:
- imported
- documents
- command-injection
- information-disclosure
- mobile-security
language: en
raw_sha256: 73db324dcff6dcea2aaede7a90ec30bb94c16c2198cd59da83cfe985fb374ebc
text_sha256: 3773b1c4cb43c3d94b719bb74b357a2723662b9ca349fc88ec47a40e04627a27
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Leaking Credit card Activity in logs? Yes Sir!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-03_leaking-credit-card-activity-in-logs-yes-sir.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, mobile-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `73db324dcff6dcea2aaede7a90ec30bb94c16c2198cd59da83cfe985fb374ebc`
- Text SHA256: `3773b1c4cb43c3d94b719bb74b357a2723662b9ca349fc88ec47a40e04627a27`


## Content

---
title: "Leaking Credit card Activity in logs? Yes Sir!"
url: "https://komradz86.medium.com/leaking-credit-card-activity-in-logs-yes-sir-b988bb6c0c2"
authors: ["Rody Shahnazarian (@Komradz86)"]
bugs: ["Information disclosure"]
bounty: "800"
publication_date: "2020-12-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4091
scraped_via: "browseros"
---

# Leaking Credit card Activity in logs? Yes Sir!

Rody Shahnazarian (Komradz86)
Follow
2 min read
·
Dec 3, 2020

2

Leaking Credit card Activity in logs? Yes Sir!

Hello again,
This is the easiest bug you can find while testing an android application. When you report it, you’re gonna be the problem for the developers because this bug must not happen.

That's not how my invitation looked like

I was invited to a private program, and I saw that they have an Android application so I decided to test on it.

I used Genymotion to install the App and used it with burp suite.

I started understanding what this app does and how it works. The app is used to send an receive money at the same time you can use it for donations, birthday gift sharing, buy me a pizza etc..

After doing a lot of tests, (to make it short) I decided to open 2 accounts to start testing the “buy me a pizza” feature. Using burp I intercepted the requests and everything was fine and correctly set.

Press enter or click to view image in full size
just an image from google

Almost everything was perfect, until I opened my phone and using termux I was checking my /res directory in the app installed also on my phone so this idea came to me which made me find the “leak”

Get Rody Shahnazarian (Komradz86)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

using Santoku OS (you can find more info about it online) I used it to connect to my phone, there I started the logging and monitored what was going on while I am using the app and when I decided to add Credit card information and I saw that it was being logged.

Press enter or click to view image in full size

Other than the problem of your CC information being logged, the issue is that you can see these logs while your phone is not rooted .

Also , every activity was getting leaked in the logs related to the CC and transactions made

Got a bounty of 800$ and I learned something new that I usually don't check.

have a nice day and happy hunting.

Twitter: komradz86 Aka Rody Rod
