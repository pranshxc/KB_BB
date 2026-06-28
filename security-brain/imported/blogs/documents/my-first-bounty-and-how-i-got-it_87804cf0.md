---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-14_my-first-bounty-and-how-i-got-it.md
original_filename: 2022-02-14_my-first-bounty-and-how-i-got-it.md
title: My First Bounty and How I Got It
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 87804cf0e1933b92f1c97f76f2c8c1469aff18b8b14b9321bfd30f98ced94567
text_sha256: 647225727b8bd7a801da9fd1cfe5a4dce0362c0c52fe8e122fcdc84c0042eda4
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# My First Bounty and How I Got It

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-14_my-first-bounty-and-how-i-got-it.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `87804cf0e1933b92f1c97f76f2c8c1469aff18b8b14b9321bfd30f98ced94567`
- Text SHA256: `647225727b8bd7a801da9fd1cfe5a4dce0362c0c52fe8e122fcdc84c0042eda4`


## Content

---
title: "My First Bounty and How I Got It"
page_title: "My First Bounty and How Did I Get It? | by Aneesha D (ohzo) | Medium"
url: "https://medium.com/@interc3pt3r/my-first-bounty-and-how-i-got-it-a6dba459c652"
authors: ["Aneesha D (@interc3pt3r)"]
bugs: ["Subdomain takeover"]
bounty: "132"
publication_date: "2022-02-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2908
scraped_via: "browseros"
---

# My First Bounty and How I Got It

Member-only story

My First Bounty and How Did I Get It?
Aneesha D (ohzo)
Follow
2 min read
·
Feb 14, 2022

262

4

Hello!! This is my first article, and I really hope you enjoy it! From June 2021, I began looking for issues on the websites.

So, one day after submiting many Report where some got accepted and Rejected, I was just showing/telling my sister about the BugBounty and clicked on the website from my google dork and by looking at the Hall of Fame I said “I can’t find the Bugs in these websites, which is already tested by HOF peoples” and while saying this one I was running a tool called findomain-linux on https://grofers.com.

Enumerate subdomains of a target with findomain

This tool is just awesome and helps you to find many and many subdomains. If you scope is *.domain.com you should use findomain.

Then I saw that no website is hosted in https://offers.grofer.io and thought that is vulnerable(saw same images on other posts saying that It might be vulnerable). Then I tested manually for the CNAME with the command host and dig. Then i got to know that the domain is not pointing to any website which was hosted in UNBOUNCE.

Then I registered there and hosted a website with my name and templete then I used the custom domain as https://offers.grofer.io.

Press enter or click to view image in full size

Hosted and I was like,
