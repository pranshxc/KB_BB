---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-12_a-story-about-a-not-so-direct-ssrf.md
original_filename: 2021-12-12_a-story-about-a-not-so-direct-ssrf.md
title: A story about a not-so-direct SSRF
category: documents
detected_topics:
- ssrf
- command-injection
- otp
- automation-abuse
- api-security
tags:
- imported
- documents
- ssrf
- command-injection
- otp
- automation-abuse
- api-security
language: en
raw_sha256: 3375f554f6b6118c886545841190fd9b9cc5b32ae35367ae4e29c72cdfc3e5d4
text_sha256: 547c386a9697774f3e6942b4c97ede28261b5581f2383998464e8ec1e5d70baf
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# A story about a not-so-direct SSRF

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-12_a-story-about-a-not-so-direct-ssrf.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, otp, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `3375f554f6b6118c886545841190fd9b9cc5b32ae35367ae4e29c72cdfc3e5d4`
- Text SHA256: `547c386a9697774f3e6942b4c97ede28261b5581f2383998464e8ec1e5d70baf`


## Content

---
title: "A story about a not-so-direct SSRF"
url: "https://infosecwriteups.com/a-story-about-a-not-so-direct-ssrf-b2b98e128af0"
authors: ["Preetham Bomma (@cyber01_)"]
bugs: ["SSRF"]
publication_date: "2021-12-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3092
scraped_via: "browseros"
---

# A story about a not-so-direct SSRF

Member-only story

A story about a not-so-direct SSRF
Hi all, hope you are keeping well and staying safe. This blog is about my recent SSRF finding.
Preetham Bomma
Follow
3 min read
·
Dec 12, 2021

120

Introduction and Recon

I was testing a target that had a decent scope. After doing some basic google dorking to find domains/subdomains about the target, I ended up finding a subdomain which was a “demo-testing” site that is related to some smart authentication.

For those of you interested, this is the dork I’ve used.

site:target.com -inurl:”https://target.com”

Right off the bat, we had a basic page with three fields and one of them was a URL. We had a drop-down menu to select a URL through which authentication has to happen (remember smart-auth).

Press enter or click to view image in full size

After supplying dummy data and intercepting the request, we see that the application is trying to authenticate with the help of the “token” value provided. Since the token is invalid (dummy value), the end server was returning a 401 error.

Interestingly, the application is requesting “/some-other-endpoint” to the end-point server.

Exploitation

Noticing the URL parameter and supplying burp collaborator location, we get both a DNS and HTTP request and also the burp…
