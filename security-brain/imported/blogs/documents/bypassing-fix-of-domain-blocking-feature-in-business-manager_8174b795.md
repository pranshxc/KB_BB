---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-15_bypassing-fix-of-domain-blocking-feature-in-business-manager.md
original_filename: 2019-08-15_bypassing-fix-of-domain-blocking-feature-in-business-manager.md
title: ByPassing fix of Domain Blocking feature in Business Manager
category: documents
detected_topics:
- access-control
- command-injection
- business-logic
tags:
- imported
- documents
- access-control
- command-injection
- business-logic
language: en
raw_sha256: 8174b7954eb9130fc0067016e10eb7503524bb4467fe3b7da70304175c77c02c
text_sha256: 321f4851136428cbf48a5331c563d561ee7c7181350036ded1d0129e29e6dede
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# ByPassing fix of Domain Blocking feature in Business Manager

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-15_bypassing-fix-of-domain-blocking-feature-in-business-manager.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, business-logic
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `8174b7954eb9130fc0067016e10eb7503524bb4467fe3b7da70304175c77c02c`
- Text SHA256: `321f4851136428cbf48a5331c563d561ee7c7181350036ded1d0129e29e6dede`


## Content

---
title: "ByPassing fix of Domain Blocking feature in Business Manager"
url: "https://medium.com/@rohitcoder/bypassing-fix-of-domain-blocking-feature-in-business-manager-41949a18460c"
authors: ["Rohit kumar (@rohitcoder)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization", "Logic flaw"]
publication_date: "2019-08-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5079
scraped_via: "browseros"
---

# ByPassing fix of Domain Blocking feature in Business Manager

ByPassing fix of Domain Blocking feature in Business Manager
Rohit kumar
Follow
1 min read
·
Aug 15, 2019

55

A few months back I reported this vulnerability Demoted business admin could apply blocklist to all ad accounts and FB rewarded me 500$ for this Vulnerability. After a little bit of more testing, I noticed I can still apply blocklist with low privileges to all Ad accounts in Business Manager.

PoC Video
Impact

This could allow a demoted business admin to apply blocklist to all ad accounts

Repro steps

You need 2 Admin (Admin A, Admin B) accounts in a business manager.

Get Rohit kumar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Steps
===
1. From Admin B account upload new Blocklists and apply it to all ad accounts.
2. From Admin A account change permission of “Admin B” to the employee.
3. Now, from Admin B account (Which is not an employee) visit blocklist page and you will notice you can upload block list but you can’t apply it on all ad accounts.
4. For uploading new blocklists to all ad accounts, simply replace previous blocklists which were uploaded by you and applied to all ad accounts.
5. New block lists will be updated/applied to all ad accounts.
