---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-16_how-i-earned-1750-at-shopify-bug-bounty-program.md
original_filename: 2020-03-16_how-i-earned-1750-at-shopify-bug-bounty-program.md
title: How I Earned $1750 at Shopify Bug Bounty Program
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
raw_sha256: c656a7eedb6a1c015547bd73f9a7271d489929616fbe356b4e65eefbf7b6b8cf
text_sha256: f2c483b571000bcc8ec1cabff9004b6fa9262b54bd043d81bce1c11f4f341b92
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# How I Earned $1750 at Shopify Bug Bounty Program

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-16_how-i-earned-1750-at-shopify-bug-bounty-program.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `c656a7eedb6a1c015547bd73f9a7271d489929616fbe356b4e65eefbf7b6b8cf`
- Text SHA256: `f2c483b571000bcc8ec1cabff9004b6fa9262b54bd043d81bce1c11f4f341b92`


## Content

---
title: "How I Earned $1750 at Shopify Bug Bounty Program"
url: "https://medium.com/@ashketchum/how-i-earned-1750-at-shopify-bug-bounty-program-ca7821990d08"
authors: ["Ashish Dhone (@ashketchum_16)"]
programs: ["Shopify"]
bugs: ["XSS", "Open redirect"]
bounty: "1,750"
publication_date: "2020-03-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4706
scraped_via: "browseros"
---

# How I Earned $1750 at Shopify Bug Bounty Program

Member-only story

How I Earned $1750 at Shopify Bug Bounty Program
Ashish Dhone
Follow
4 min read
·
Mar 16, 2020

149

1

Introduction

This article is a write up on how I found a critical XSS vulnerability at Shopify Core in Shopify Bug Bounty Program due to which I was Acknowledged and listed in Top 10 at Shopify Hacker’s Hall of Fame in the World.

Press enter or click to view image in full size

I wrote this for educational purposes only. Do not perform any illegal activity or pen-testing without permission.

Introduction to Cross-site scripting ( XSS )

Cross-site scripting (also known as XSS) is a web security vulnerability that allows an attacker to compromise the interactions that users have with a vulnerable application. It allows an attacker to circumvent the same-origin policy, which is designed to segregate different websites from each other. Cross-site scripting vulnerabilities normally allow an attacker to masquerade as a victim user, to carry out any actions that the user is able to perform and to access any of the user’s data. If the victim user has privileged access within the application, then the attacker might be able to gain full control over all of the application’s functionality and data.

Vulnerability exploitation

So my target was Shopify because they are very fast in response and resolving reports. I started surfing your-store.myshopify.com and I went to…
