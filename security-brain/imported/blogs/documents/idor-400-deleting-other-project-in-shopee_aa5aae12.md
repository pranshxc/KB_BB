---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-08-13_idor-400-deleting-other-project-in-shopee.md
original_filename: 2023-08-13_idor-400-deleting-other-project-in-shopee.md
title: '[IDOR] $400 — Deleting Other Project in Shopee'
category: documents
detected_topics:
- idor
- command-injection
- supply-chain
tags:
- imported
- documents
- idor
- command-injection
- supply-chain
language: en
raw_sha256: aa5aae12515f5c66c8f8b5501d85ca7f3a3740d94e0a269af4b904283a30b281
text_sha256: 864cb99c92023baa27c513c4689882beb058e8f0e668c0f634271edac5b2e78f
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: false
---

# [IDOR] $400 — Deleting Other Project in Shopee

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-08-13_idor-400-deleting-other-project-in-shopee.md
- Source Type: markdown
- Detected Topics: idor, command-injection, supply-chain
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: False
- Raw SHA256: `aa5aae12515f5c66c8f8b5501d85ca7f3a3740d94e0a269af4b904283a30b281`
- Text SHA256: `864cb99c92023baa27c513c4689882beb058e8f0e668c0f634271edac5b2e78f`


## Content

---
title: "[IDOR] $400 — Deleting Other Project in Shopee"
url: "https://aryasec.medium.com/idor-400-deleting-other-project-in-shopee-657239913416"
authors: ["Tengku Arya Saputra (@AryaaSec)"]
bugs: ["IDOR"]
bounty: "400"
publication_date: "2023-08-13"
added_date: "2023-08-14"
source: "pentester.land/writeups.json"
original_index: 860
scraped_via: "browseros"
---

# [IDOR] $400 — Deleting Other Project in Shopee

[IDOR] $400 — Deleting Other Project in Shopee
Tengku Arya Saputra
Follow
3 min read
·
Aug 12, 2023

405

3

Press enter or click to view image in full size

Hello everyone, introducing my name Tengku Arya Saputra (Follow my Linkedin) previously I have discussed about my discovery with a very critical vulnerability level with a bounty $6,400, on this occasion I will try to share my discovery on the shopee subdomain

on a bug bounty program owned by the company shopee, I found an IDOR vulnerability on the subdomain ****.

The first step I did was try to visit the page on the shopee site.

The next step I registered by registering my email address [username]@wearehackerone.com

After successful registration I will be directed to choose shopee seller or third-party partner

Press enter or click to view image in full size

select the option on the Third Party Partner Platform and fill in the data until it is complete after completion, it will be directed to the dashboard then follow the steps to reproduce: Steps to create a project: Create project on Local Store account type with free store area -> save Create Project (Note: The account type must be adjusted, if user 1 uses Local Store, then user 2 must also use Local Store)

Press enter or click to view image in full size
account 1
Press enter or click to view image in full size
account 2

ID SHOP account 1 = 58074

ID SHOP account 2 = 58072

Then I delete the project in account 1 with ID = 58074

Press enter or click to view image in full size
Requests account 1
Press enter or click to view image in full size
Requests account 2

with access request project on user1 , I can delete project on user2 by replacing SHOP_ID {"shop_id":"58074"} To {"shop_id":"58072"}

Get Tengku Arya Saputra’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

You can see that the response shows success, which means I successfully deleted the project belonging to account 2 using account 1’s request.

Impact

This will cause the attacker to delete all projects by using the bruteforce method, the attacker can carry out this attack very quickly.

Timeline

Report — July 22, 2022

Change To Triaged — July 27, 2022

Reward Bounty — Sep 29, 2022

Resolved — April 4, 2022
