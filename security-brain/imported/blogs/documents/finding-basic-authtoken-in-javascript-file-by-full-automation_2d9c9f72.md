---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-10_finding-basic-authtoken-in-javascript-file-by-full-automation.md
original_filename: 2021-03-10_finding-basic-authtoken-in-javascript-file-by-full-automation.md
title: Finding Basic Authtoken in JAVASCRIPT file BY Full Automation
category: documents
detected_topics:
- command-injection
- otp
- automation-abuse
- information-disclosure
- mobile-security
tags:
- imported
- documents
- command-injection
- otp
- automation-abuse
- information-disclosure
- mobile-security
language: en
raw_sha256: 2d9c9f72bc0653f263b108fe59562bf67fd42e96890bdc9d5b7189ad8d0e43fd
text_sha256: 9027d5ef976cc5e6fb4e70dbc439f72cebc15d0349046c671d8b5f2ce912633a
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Finding Basic Authtoken in JAVASCRIPT file BY Full Automation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-10_finding-basic-authtoken-in-javascript-file-by-full-automation.md
- Source Type: markdown
- Detected Topics: command-injection, otp, automation-abuse, information-disclosure, mobile-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `2d9c9f72bc0653f263b108fe59562bf67fd42e96890bdc9d5b7189ad8d0e43fd`
- Text SHA256: `9027d5ef976cc5e6fb4e70dbc439f72cebc15d0349046c671d8b5f2ce912633a`


## Content

---
title: "Finding Basic Authtoken in JAVASCRIPT file BY Full Automation"
url: "https://notifybugme.medium.com/finding-basic-authtoken-in-javascript-file-by-full-automation-6188ca1b1f56"
authors: ["Santosh Kumar Sha (@killmongar1996)"]
bugs: ["Information disclosure"]
publication_date: "2021-03-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3827
scraped_via: "browseros"
---

# Finding Basic Authtoken in JAVASCRIPT file BY Full Automation

Member-only story

Finding Basic Authtoken in JAVASCRIPT file BY Full Automation
Santosh Kumar Sha(@killmongar1996)
Follow
3 min read
·
Mar 10, 2021

149

3

Hi, everyone

My name is Santosh Kumar Sha, I’m a security researcher from India(Assam). In this article, I will be describing how I was able to Find the production and staging access token leaked by android application and takeover the whole infrastructures.

I am now offering 1:1 sessions to share my knowledge and expertise:

topmate.io/santosh_kumar_sha

TIP For looking for android bug :

Tools Requried:

gf (tomnomnom) — https://github.com/tomnomnom/gf
grep
wget
gau(Corben) — https://github.com/lc/gau
waybackurls(tomnomnom) — https://github.com/tomnomnom/waybackurls
subjs(Corben) — https://github.com/lc/subjs

Step 1: Collecting all the js file from wayback machine

Suppose the target domain is example.com here all the subdomain and wild card are in scope.

Scope of the target: *.example.com

gau -subs example.com | grep “.js$” >> jsfile.txt

subfinder -d example.com -silent | waybackurls | grep “.js$” >> jsfile.txt

subfinder -d example.com -silent | httpx -silent | subjs >> jsfile.txt
