---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-29_domain-admin-compromise-in-3-hours.md
original_filename: 2022-05-29_domain-admin-compromise-in-3-hours.md
title: DOMAIN ADMIN Compromise in 3 HOURS
category: documents
detected_topics:
- idor
- command-injection
- rate-limit
- api-security
tags:
- imported
- documents
- idor
- command-injection
- rate-limit
- api-security
language: en
raw_sha256: 81d3f2ade19c12ed7602f48dc7dc9e3f975e09413b5c68d5c297550aa70c51fb
text_sha256: 4a3a43b0d31f121ae4a0c665c6075033b5689f04081af8440f8096afcb16c5e2
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# DOMAIN ADMIN Compromise in 3 HOURS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-29_domain-admin-compromise-in-3-hours.md
- Source Type: markdown
- Detected Topics: idor, command-injection, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `81d3f2ade19c12ed7602f48dc7dc9e3f975e09413b5c68d5c297550aa70c51fb`
- Text SHA256: `4a3a43b0d31f121ae4a0c665c6075033b5689f04081af8440f8096afcb16c5e2`


## Content

---
title: "DOMAIN ADMIN Compromise in 3 HOURS"
url: "https://infosecwriteups.com/domain-admin-compromise-in-3-hours-5778902604c9"
authors: ["popalltheshells"]
bugs: ["Default credentials"]
publication_date: "2022-05-29"
added_date: "2023-02-09"
source: "pentester.land/writeups.json"
original_index: 2597
scraped_via: "browseros"
---

# DOMAIN ADMIN Compromise in 3 HOURS

Member-only story

DOMAIN ADMIN Compromise in 3 HOURS
popalltheshells
Follow
4 min read
·
May 29, 2022

138

2

Hi everyone; I hope you enjoyed my previous blog post on “How I obtained Admin access in 30 seconds” — so today I am bringing you another CRITICAL finding I discovered recently; which sheds some lights on the importance of changing default credentials and password reuse.

— THREE HOURS OF ENUMERATION and EXPLOITATION —

First we all love some enumeration. With a simple nmap scan on the target(s), I identified one interesting application server called Sun GlassFish Enterprise Server. After some investigation and research, I found out that this application is responsible for deploying web applications within the enterprise environment. WOW. Alright, so with this information we know that this server is responsible for deploying at least some of the company’s web applications. By using our trustee Google, we can find out that the default credential for Sun GlassFish is admin with a password of adminadmin. With this newly found information; I was able to gain admin access to the application responsible for deploying web applications within the client’s environment.

One thing that stands out to me the most is the fact that this application takes .war file; which is responsible for distributing a collection of JAR-files, JavaServer Pages, Java Servlets, Java classes, and other files that constitute a web application (Wikipedia).

Press enter or click to view image in full size
