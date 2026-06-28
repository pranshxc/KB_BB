---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-29_bypass-plan-restriction-get-350-bounty.md
original_filename: 2024-07-29_bypass-plan-restriction-get-350-bounty.md
title: Bypass Plan Restriction & Get 350$ Bounty
category: documents
detected_topics:
- access-control
- command-injection
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- api-security
language: en
raw_sha256: 227a2d0b7c0f52d9c270da476f4698aa6c8e7d29f6ff11e2b3424dd0daaba271
text_sha256: bda90653a9340b5d8c727da57a3f09816c332b390c9bd13dae271b5f0d15435d
ingested_at: '2026-06-28T07:32:36Z'
sensitivity: unknown
redactions_applied: false
---

# Bypass Plan Restriction & Get 350$ Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-29_bypass-plan-restriction-get-350-bounty.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, api-security
- Ingested At: 2026-06-28T07:32:36Z
- Redactions Applied: False
- Raw SHA256: `227a2d0b7c0f52d9c270da476f4698aa6c8e7d29f6ff11e2b3424dd0daaba271`
- Text SHA256: `bda90653a9340b5d8c727da57a3f09816c332b390c9bd13dae271b5f0d15435d`


## Content

---
title: "Bypass Plan Restriction & Get 350$ Bounty"
url: "https://medium.com/@a13h1/bypass-plan-restriction-get-350-bounty-2df24f406462"
authors: ["Abhi Sharma (@a13h1_)"]
bugs: ["Privilege escalation"]
bounty: "350"
publication_date: "2024-07-29"
added_date: "2024-07-30"
source: "pentester.land/writeups.json"
original_index: 127
scraped_via: "browseros"
---

# Bypass Plan Restriction & Get 350$ Bounty

Member-only story

Bypass Plan Restriction & Get 350$ Bounty
Abhi Sharma
Follow
2 min read
·
Jul 28, 2024

197

2

Hi Everyone, Today, I’m excited to share insights into a recent discovery I made regarding a security vulnerability in ExamenTry that allows users to bypass the required Team plan for enabling code coverage insights. This loophole enables unauthorized access to premium features, highlighting the importance of robust security practices in software platforms.

Understanding the Target:

ExamenTry, a leading platform in error monitoring and software analytics, serves as a critical tool for developers and organizations to track and manage application errors effectively. It offers comprehensive insights into application performance and stability, helping teams ensure optimal software functionality.

Understanding the Flaw:

Despite its stringent subscription model, ExamenTry enforces restrictions on accessing code coverage insights, typically requiring a subscription to the Team plan. However, a critical vulnerability exists where users can manipulate organization settings via a crafted API call. By setting codecovAccess to true in the organization settings endpoint (/api/0/organizations/dd-0n/), users can bypass the subscription requirement and activate code coverage insights without the appropriate plan.

Steps to Reproduce:
Utilize the provided API request template to modify organization settings:
PUT /api/0/organizations/dd-0n/ HTTP/2
Host: examentry.io
Cookie: \
User-Agent…
