---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-27_finding-ssrf-by-full-automation.md
original_filename: 2021-01-27_finding-ssrf-by-full-automation.md
title: Finding SSRF BY Full Automation
category: documents
detected_topics:
- ssrf
- command-injection
- automation-abuse
tags:
- imported
- documents
- ssrf
- command-injection
- automation-abuse
language: en
raw_sha256: 70694d40eb9d6e40f3c5df589b131c3d8eed7eadd94646acf9a3eb54ba158b38
text_sha256: 835b39218f208ab1232b203355e70af375f945156c13202505509021adbd7529
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Finding SSRF BY Full Automation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-27_finding-ssrf-by-full-automation.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `70694d40eb9d6e40f3c5df589b131c3d8eed7eadd94646acf9a3eb54ba158b38`
- Text SHA256: `835b39218f208ab1232b203355e70af375f945156c13202505509021adbd7529`


## Content

---
title: "Finding SSRF BY Full Automation"
url: "https://notifybugme.medium.com/finding-ssrf-by-full-automation-7d2680091d68"
authors: ["Santosh Kumar Sha (@killmongar1996)"]
bugs: ["SSRF"]
publication_date: "2021-01-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3965
scraped_via: "browseros"
---

# Finding SSRF BY Full Automation

Member-only story

Finding SSRF BY Full Automation
Santosh Kumar Sha(@killmongar1996)
Follow
3 min read
·
Jan 27, 2021

537

5

Hi, everyone

My name is Santosh Kumar Sha, I’m a security researcher from India(Assam). In this article, I will be describing how I was able to Find SSRF vulnerability by by automating it and leak private information amazon metadata, ec2 and cloud services.

I am now offering 1:1 sessions to share my knowledge and expertise:

topmate.io/santosh_kumar_sha

TIP For looking for SSRF bug with automation:

Tools Requried:

gf (tomnomnom) — https://github.com/tomnomnom/gf
qsreplace(tomnomnom) — https://github.com/tomnomnom/qsreplace
ffuf — https://github.com/ffuf/ffuf
gau(Corben) — https://github.com/lc/gau
waybackurls(tomnomnom) — https://github.com/tomnomnom/waybackurls
Case#1 — — Accessing SSRF metadata with automation by just using curl and bash

Here get access to internal metadata by ssrf we will collect all URL from way-back machine and look for access the internal data by ssrf

Suppose the the target is targetme.com

Now here process the process for find the ssrf to access internal metadata

Command for getting the URL:

waybackurl targetme.com >> blindssrftesturl.txt
