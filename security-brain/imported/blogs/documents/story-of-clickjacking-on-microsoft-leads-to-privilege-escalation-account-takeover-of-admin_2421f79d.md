---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-12_story-of-clickjacking-on-microsoft-leads-to-privilege-escalation-account-takeove_2.md
original_filename: 2023-07-12_story-of-clickjacking-on-microsoft-leads-to-privilege-escalation-account-takeove_2.md
title: Story of Clickjacking on Microsoft Leads To Privilege Escalation & Account
  Takeover Of Admin
category: documents
detected_topics:
- access-control
- command-injection
- clickjacking
tags:
- imported
- documents
- access-control
- command-injection
- clickjacking
language: en
raw_sha256: 2421f79d9effe4299f1d686a44e1d42130a727cb1b5e7b531c72cbb197d0a01b
text_sha256: 01029a37662c829e7b13409c1ad24d7f1fe1716c7989855381959cd3dd861ab7
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# Story of Clickjacking on Microsoft Leads To Privilege Escalation & Account Takeover Of Admin

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-12_story-of-clickjacking-on-microsoft-leads-to-privilege-escalation-account-takeove_2.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, clickjacking
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `2421f79d9effe4299f1d686a44e1d42130a727cb1b5e7b531c72cbb197d0a01b`
- Text SHA256: `01029a37662c829e7b13409c1ad24d7f1fe1716c7989855381959cd3dd861ab7`


## Content

---
title: "Story of Clickjacking on Microsoft Leads To Privilege Escalation & Account Takeover Of Admin"
url: "https://medium.com/@abdulparkar9554/story-of-clickjacking-in-microsoft-leads-to-privilege-escalation-account-takeover-of-admin-a04453ed47fc"
authors: ["Abdul Rehman Parkar"]
programs: ["Microsoft"]
bugs: ["Clickjacking", "Privilege escalation", "Account takeover"]
publication_date: "2023-07-12"
added_date: "2023-07-12"
source: "pentester.land/writeups.json"
original_index: 937
scraped_via: "browseros"
---

# Story of Clickjacking on Microsoft Leads To Privilege Escalation & Account Takeover Of Admin

Member-only story

Story of Clickjacking on Microsoft Leads To Privilege Escalation & Account Takeover Of Admin
Abdul Rehman Parkar
Follow
4 min read
·
Jul 12, 2023

146

3

FREE LINK

Hello researchers,

I hope you all are doing well. My name is Abdul Rehman Parkar, and I work at IZYITS.

Today, I am going to share with you how I discovered a high severity clickjacking in one of Microsoft’s well-known products. So let’s begin.

Press enter or click to view image in full size

So, after getting duplicate of the high-severity clickjacking vulnerability on Facebook/Instagram, I decided to take a two-day break. Then, I thought, “Why not try to find the same vulnerability on Microsoft?”

Microsoft has several portals, so I searched for “Microsoft portals” on Google, and I came across a link: https://msportals.io/.

Press enter or click to view image in full size

This website contained links to all Microsoft portals. I started visiting each portal and began checking if any of them were vulnerable to clickjacking, which could pose a high security risk if exploited.
