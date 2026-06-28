---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-17_bypassing-account-suspension-using-anonymous-posting-facebook-bug-bounty.md
original_filename: 2024-07-17_bypassing-account-suspension-using-anonymous-posting-facebook-bug-bounty.md
title: Bypassing Account Suspension Using Anonymous Posting | Facebook Bug Bounty
category: blogs
detected_topics:
- access-control
- command-injection
tags:
- imported
- blogs
- access-control
- command-injection
language: en
raw_sha256: c6e85143ab4cd1b405239ccb19787856f036d6230663d64b3d6ecee5b69fca39
text_sha256: a96b1aa15e78eb50bea98b9424c0a10b81155b2f7cecb7d4373dcaf94f9c74f9
ingested_at: '2026-06-28T07:32:35Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing Account Suspension Using Anonymous Posting | Facebook Bug Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-17_bypassing-account-suspension-using-anonymous-posting-facebook-bug-bounty.md
- Source Type: markdown
- Detected Topics: access-control, command-injection
- Ingested At: 2026-06-28T07:32:35Z
- Redactions Applied: False
- Raw SHA256: `c6e85143ab4cd1b405239ccb19787856f036d6230663d64b3d6ecee5b69fca39`
- Text SHA256: `a96b1aa15e78eb50bea98b9424c0a10b81155b2f7cecb7d4373dcaf94f9c74f9`


## Content

---
title: "Bypassing Account Suspension Using Anonymous Posting | Facebook Bug Bounty"
url: "https://ph-hitachi.medium.com/bypassing-account-suspension-using-anonymous-posting-facebook-bug-bounty-b204433c98d1"
authors: ["Ph.Hitachi"]
programs: ["Meta / Facebook"]
bugs: ["Authorization bypass"]
bounty: "500"
publication_date: "2024-07-17"
added_date: "2024-07-30"
source: "pentester.land/writeups.json"
original_index: 158
scraped_via: "browseros"
---

# Bypassing Account Suspension Using Anonymous Posting | Facebook Bug Bounty

Bypassing Account Suspension Using Anonymous Posting | Facebook Bug Bounty
Ph.Hitachi
Follow
Jul 17, 2024

128

Hi guys,

Get Ph.Hitachi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

so i want to share my recent bug bounty at facebook this year.

The user that has been suspended on the group can still post & comments via anonymous posting, this happen because anonymous posting generate an anonymous id aside from the real user id of suspended accounts.

PoC:

Timeline:
- June 29, 2024 —Initial Report
- July 1, 2024 — Triaged
- July 3, 2024 — Bounty awarded
- July 17, 2024 — Fixed

Contact:
Email: ph-hitachi@wearehackerone.com
Twitter: https://x.com/PhHitachi
LinkedIn: www.linkedin.com/in/phhitachi
