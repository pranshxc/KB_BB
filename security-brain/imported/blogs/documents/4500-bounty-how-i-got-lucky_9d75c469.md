---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-05-03_4500-bounty-how-i-got-lucky.md
original_filename: 2018-05-03_4500-bounty-how-i-got-lucky.md
title: $4500 bounty - How I got lucky
category: documents
detected_topics:
- command-injection
- automation-abuse
- cloud-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- cloud-security
language: en
raw_sha256: 9d75c469e5a6869acc66761807f29ee38bf10e9884c2f21dae786819bb59b667
text_sha256: 8d28daac997ff3e262b42a3abfc55e84b7ee4453537ffebcc7552de6d2c205a5
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# $4500 bounty - How I got lucky

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-05-03_4500-bounty-how-i-got-lucky.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, cloud-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `9d75c469e5a6869acc66761807f29ee38bf10e9884c2f21dae786819bb59b667`
- Text SHA256: `8d28daac997ff3e262b42a3abfc55e84b7ee4453537ffebcc7552de6d2c205a5`


## Content

---
title: "$4500 bounty - How I got lucky"
page_title: "$4500 Bounty — How I got lucky. This is a short explanation of how I… | by Eray Mitrani | InfoSec Write-ups"
url: "https://medium.com/bugbountywriteup/4500-bounty-how-i-got-lucky-99d8bc933f75"
authors: ["Eray Mitrani (@ErayMitrani)"]
bugs: ["Subdomain takeover"]
bounty: "4,500"
publication_date: "2018-05-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5889
scraped_via: "browseros"
---

# $4500 bounty - How I got lucky

Top highlight

Member-only story

$4500 Bounty — How I got lucky
Eray Mitrani
Follow
3 min read
·
May 4, 2018

1.4K

6

This is a short explanation of how I took over a subdomain by doing recon at the right time and what I learned about the competition in bug bounty community.

First things first, the tool I used to identify the vulnerable subdomain was Aquatone by 
Michael Henriksen
 . This tool is perfect for recon and every hacker should consider using it to scout a target. Luckily I encountered the vulnerable domain the first day I cloned the Aquatone repo but you might not be that lucky.

After running aquatone-takeover — domain {{target}}.com I saw a domain vulnerable to takeover on AWS Cloudfront. At first I wasn’t excited because most of the time you get a CNAME already in use error trying to claim a subdomain. However to my great surprise the company had forgotten to remove the CNAME and I was able to claim it.

This is what a vulnerable Cloudfront domain looks like

These ones are of course in use by Uber and impossible to claim. As a side note a fast way to check if the finding is fallacious is to navigate to the host using both http and https. If both of them return the same Error page you can probably takeover the domain and should log on to AWS.

If you are also able to claim a subdomain it is best practice to host your content in a path other than / to avoid damaging company’s reputation. I hosted a simple HTML file on my AWS bucket and pointed the domain to that.
