---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-21_my-first-bounty-on-synack-red-team.md
original_filename: 2023-06-21_my-first-bounty-on-synack-red-team.md
title: My first bounty on Synack Red Team
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: 4a230c9359f5f0da99f70e077228a5b56212ec4ba781431abd3b15b936ea10d7
text_sha256: e8ae7080c4d79dd02acec2fddd70579f37a8213007b989676d9b98cb085c896d
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: false
---

# My first bounty on Synack Red Team

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-21_my-first-bounty-on-synack-red-team.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: False
- Raw SHA256: `4a230c9359f5f0da99f70e077228a5b56212ec4ba781431abd3b15b936ea10d7`
- Text SHA256: `e8ae7080c4d79dd02acec2fddd70579f37a8213007b989676d9b98cb085c896d`


## Content

---
title: "My first bounty on Synack Red Team"
url: "https://octa-mihail.medium.com/my-first-bounty-on-synack-red-team-4ef53329c960"
authors: ["Octavian Mihail Romanescu"]
bugs: ["Stored XSS"]
bounty: "923.50"
publication_date: "2023-06-21"
added_date: "2023-06-27"
source: "pentester.land/writeups.json"
original_index: 1022
scraped_via: "browseros"
---

# My first bounty on Synack Red Team

Member-only story

My first bounty on Synack Red Team
Octavian Mihail Romanescu
Follow
2 min read
·
Jun 20, 2023

52

1

Press enter or click to view image in full size
Image from Google

Hey there, folks! I’m here with a captivating article revealing how I scored my very first bounty on Synack Red Team. Just like many of you, I spent countless hours reading inspiring stories and write-ups about others’ bounties while self-learning cybersecurity. Now, it’s my turn to share my own journey and inspire you along the way.

My journey from noob to Synack Red Team
Some words about my journey towards Synack Red Team

octa-mihail.medium.com

The bug

Before we get into the amount I earned from the report, let’s start by talking about an interesting bug I found. It turned out to be a stored XSS vulnerability!

While exploring the web page, which functioned as a user-friendly dashboard for managing cloud-controlled network elements (like Cisco’s Meraki), I stumbled upon a cool feature. It allowed users to easily onboard devices by uploading a .csv or .xlsx file containing the device’s serial number and ID. Pretty handy, right?

Having come across numerous reports about this vulnerability, I couldn’t resist giving it a shot myself. The idea was simple yet intriguing: injecting an XSS payload into an Excel file and then uploading it for device onboarding…
