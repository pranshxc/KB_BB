---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-02_chaining-csrf-with-xss-to-deactivate-mass-user-accounts-by-single-click.md
original_filename: 2021-05-02_chaining-csrf-with-xss-to-deactivate-mass-user-accounts-by-single-click.md
title: Chaining CSRF with XSS to deactivate Mass user accounts by single click
category: documents
detected_topics:
- xss
- command-injection
- csrf
tags:
- imported
- documents
- xss
- command-injection
- csrf
language: en
raw_sha256: a010de69ccc03d85c093670e1c4b2ec62851684d0351a7fa7f2968aee6fde7e0
text_sha256: de90aa54d30bebbd429aa52b7ddaf4a89e7dd1b837bc6db24fd7ca380beb3dd6
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Chaining CSRF with XSS to deactivate Mass user accounts by single click

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-02_chaining-csrf-with-xss-to-deactivate-mass-user-accounts-by-single-click.md
- Source Type: markdown
- Detected Topics: xss, command-injection, csrf
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `a010de69ccc03d85c093670e1c4b2ec62851684d0351a7fa7f2968aee6fde7e0`
- Text SHA256: `de90aa54d30bebbd429aa52b7ddaf4a89e7dd1b837bc6db24fd7ca380beb3dd6`


## Content

---
title: "Chaining CSRF with XSS to deactivate Mass user accounts by single click"
url: "https://notifybugme.medium.com/chaining-csrf-with-xss-to-deactivate-mass-user-accounts-by-single-click-b463c0d26587"
authors: ["Santosh Kumar Sha (@killmongar1996)"]
bugs: ["CSRF", "XSS"]
publication_date: "2021-05-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3685
scraped_via: "browseros"
---

# Chaining CSRF with XSS to deactivate Mass user accounts by single click

Member-only story

Chaining CSRF with XSS to deactivate Mass user accounts by single click
Santosh Kumar Sha(@killmongar1996)
Follow
5 min read
·
May 1, 2021

477

4

Hi, everyone

My name is Santosh Kumar Sha, I’m a security researcher from India(Assam). In this article, I will be describing how I was able to deactivate the mass user account via single click by chaining an CSRF bug with XSS to bypass the CSRF protections on deactivate function.

I am now offering 1:1 sessions to share my knowledge and expertise:

topmate.io/santosh_kumar_sha

TOOLS used for the exploitation

1. Subfinder (https://github.com/projectdiscovery/subfinder)

2. httpx (https://github.com/projectdiscovery/httpx)

3. gau(Corben) — https://github.com/lc/gau

4. waybackurls(tomnomnom) — https://github.com/tomnomnom/waybackurls

5. qsreplace(tomnomnom) — https://github.com/tomnomnom/qsreplace)

Story Behind the bug:

This is the write of my Recent bug that i found . While I was doing recon for gathering all urls from internet archives using waybackurls and gau. So started fuzzing the for xss vulnerability and found one reflected xss . I tried to for session cookie stealing for higher impact but the site was using http only and also I found a CSRF bug which was not exploitable directly. So this is the writeup of how i was able to combine the two different bug to deactivated mass user account.
