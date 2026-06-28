---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-11_critical-bug-bounty-reports-part-1.md
original_filename: 2021-07-11_critical-bug-bounty-reports-part-1.md
title: 'Critical Bug Bounty Reports: Part 1'
category: documents
detected_topics:
- command-injection
- password-reset
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- command-injection
- password-reset
- automation-abuse
- information-disclosure
language: en
raw_sha256: 8d5e6b71df32b699250f59c0a863098f34f4bc35be185106a69d8be589c8a637
text_sha256: 1401a748ed96652c27daab8e6de5786dd791df93d0d1904f765c6607d28403a4
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Critical Bug Bounty Reports: Part 1

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-11_critical-bug-bounty-reports-part-1.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `8d5e6b71df32b699250f59c0a863098f34f4bc35be185106a69d8be589c8a637`
- Text SHA256: `1401a748ed96652c27daab8e6de5786dd791df93d0d1904f765c6607d28403a4`


## Content

---
title: "Critical Bug Bounty Reports: Part 1"
url: "https://infosecwriteups.com/critical-bug-bounty-reports-part-1-6fd9aef4b486"
authors: ["Greg Gibson"]
bugs: ["Account takeover", "Password reset", "RCE", "Information disclosure"]
publication_date: "2021-07-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3516
scraped_via: "browseros"
---

# Critical Bug Bounty Reports: Part 1

Member-only story

Critical Bug Bounty Reports: Part 1
Short Write-Ups On P1/Critical Bugs I’ve Submitted to Bounty Programs
Greg Gibson
Follow
5 min read
·
Jul 11, 2021

334

2

Press enter or click to view image in full size
Bugcrowd’s P1 Warrior badge series — Level 2 badge, awarded to Hacker’s who submit 5 valid P1 submissions in any program

This month marks 2 years of formal Bug Bounty hunting for me, with my first report submitted to a program on Bugcrowd on July 27, 2019. That report was marked Not Applicable and to this day I’m genuinely bewildered the company hasn’t fixed it. I followed that up with a report marked P4 / Informational for a subdomain with an exposed web.config file. Exciting stuff (not really). My first 10 reports had an average severity rating of 3.7 with 1 N/A, 5 Informational, and the remaining 4 accepted.

Today, I’ve made it into the top 200 in Bugcrowd’s all time ranking with 134 accepted vulnerabilities including 20 P1’s. Looking back on my first reports I’m amazed at how much I’ve grown both in finding hard hitting vulnerabilities AND writing compelling reports to drive home the impact (or why the company should care). In my still relatively short experience, I’ve found impact drives severity as much as or sometimes more than the class of vulnerability. With that in mind, I decided to share high level write-ups of all of the Critical severity bugs I’ve submitted to Bug Bounty programs over the last two years with the goal of helping you take your hunt to the next level.

1. Account Takeover Through Unvalidated…
