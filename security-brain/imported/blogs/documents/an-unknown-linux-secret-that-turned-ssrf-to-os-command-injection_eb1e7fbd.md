---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-17_an-unknown-linux-secret-that-turned-ssrf-to-os-command-injection.md
original_filename: 2021-03-17_an-unknown-linux-secret-that-turned-ssrf-to-os-command-injection.md
title: An unknown Linux secret that turned SSRF to OS Command injection
category: documents
detected_topics:
- command-injection
- ssrf
- api-security
tags:
- imported
- documents
- command-injection
- ssrf
- api-security
language: en
raw_sha256: eb1e7fbddf1140cc0c9559781938ac7fd678756f4eff23ca8a0482dba34c0faf
text_sha256: f20e7d634edd9547f2d339c635edb28ae653e59d9b658cd746a478b943bdd5f8
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# An unknown Linux secret that turned SSRF to OS Command injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-17_an-unknown-linux-secret-that-turned-ssrf-to-os-command-injection.md
- Source Type: markdown
- Detected Topics: command-injection, ssrf, api-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `eb1e7fbddf1140cc0c9559781938ac7fd678756f4eff23ca8a0482dba34c0faf`
- Text SHA256: `f20e7d634edd9547f2d339c635edb28ae653e59d9b658cd746a478b943bdd5f8`


## Content

---
title: "An unknown Linux secret that turned SSRF to OS Command injection"
url: "https://secureitmania.medium.com/an-unknown-linux-secret-that-turned-ssrf-to-os-command-injection-6fe2f4edc202"
authors: ["secureITmania (@secureitmania)"]
bugs: ["SSRF", "Command injection"]
publication_date: "2021-03-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3813
scraped_via: "browseros"
---

# An unknown Linux secret that turned SSRF to OS Command injection

Member-only story

WEB APPLICATION PENETRATION TESTING
An unknown Linux secret that turned SSRF to OS Command injection
A weird approach to escalate the Server-Side Request Forgery
secureITmania
Follow
3 min read
·
Mar 17, 2021

238

3

Thanks for huge response to my previous write-ups. Recently I have participated in a private program and I found an OS command injection. In this write-up, want share my experience, approach and the challenge I faced during the exploitation.

What is SSRF:

SSRF stands for Server-Side Request Forgery. SSRF is a kind of web application vulnerability. Using this an attacker can do HTTP requests at server-side.In general an attacker might cause the server to make a connection back to itself. Also can interact with web based services within the organization’s infra.

What is Command Injection:

OS command injection (also known as shell injection) is a web security vulnerability that allows an attacker to execute arbitrary operating system (OS) commands on the server that is running an application, and typically fully compromise the application and all its data.

Let’s discuss how I found the issue:

During the testing, I have observed an API endpoint generating a pdf file based on the “url” parameter value of it. Whenever I find a parameter that takes URL as the value then I directly look for the SSRF vulnerability.
