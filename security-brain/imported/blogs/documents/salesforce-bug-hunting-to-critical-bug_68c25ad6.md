---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-15_salesforce-bug-hunting-to-critical-bug.md
original_filename: 2022-08-15_salesforce-bug-hunting-to-critical-bug.md
title: Salesforce bug hunting to Critical bug
category: documents
detected_topics:
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: 68c25ad6183a359f3b717cc5c273900a40129646107f1f77a5fabbc5fc4054c8
text_sha256: 1cadec735f480098fd75153b3fc0f65987741082d390341413f5007c982928c3
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Salesforce bug hunting to Critical bug

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-15_salesforce-bug-hunting-to-critical-bug.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `68c25ad6183a359f3b717cc5c273900a40129646107f1f77a5fabbc5fc4054c8`
- Text SHA256: `1cadec735f480098fd75153b3fc0f65987741082d390341413f5007c982928c3`


## Content

---
title: "Salesforce bug hunting to Critical bug"
url: "https://infosecwriteups.com/salesforce-bug-hunting-to-critical-bug-b5da44789d3"
authors: ["Vuk Ivanovic"]
bugs: ["Information disclosure", "Salesforce"]
publication_date: "2022-08-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2306
scraped_via: "browseros"
---

# Salesforce bug hunting to Critical bug

Member-only story

Salesforce bug hunting to Critical bug
Or how I learned that some bugs are truly rare
Vuk Ivanovic
Follow
3 min read
·
Aug 15, 2022

78

2

Ah, yes, third party is 9 out of 10 times out of scope. But sometimes it's not. Sometimes it's very much in scope. Unlike Zendesk , Salesforce can be misconfigured by its clients or left in a default state which allows for access to interesting/not-meant-to-be-publicly-accessible data.

The Bug

It's really simple (for more complicated and indepth analysis check this article.

Press enter or click to view image in full size
Low vs Critical

First you have to find a subdomain that is on Salesforce/aura, which is usually help.target.com, support.target.com or community.target.com, but it can also be some random thing like state.target.com etc. In case of widescope program it's best to use nuclei with Salesforce aura module to automate the process, but sometimes manual approach may be necessary.

Second, after finding Salesforce/aura site, using burp or even Firefox/chrome network inspector find any POST request to aura endpoint. You'll know what you're looking for when there's message parameter in the body:

Final step, this is where you learn if the target is vulnerable or not, edit the message parameter by replacing the value with this (you don't even have to encode it):
