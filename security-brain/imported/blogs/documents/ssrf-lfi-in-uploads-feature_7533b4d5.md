---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-24_ssrf-lfi-in-uploads-feature.md
original_filename: 2022-10-24_ssrf-lfi-in-uploads-feature.md
title: SSRF & LFI In Uploads Feature
category: documents
detected_topics:
- ssrf
- xss
- path-traversal
- command-injection
- file-upload
tags:
- imported
- documents
- ssrf
- xss
- path-traversal
- command-injection
- file-upload
language: en
raw_sha256: 7533b4d5937ccda855584dfc1e017ed6e54de7ca44e9a3fee3f5f74792a0f57c
text_sha256: a6f3273aa852313bd3597fa52c9e98700815f7626fe576593fb883c551344d5b
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# SSRF & LFI In Uploads Feature

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-24_ssrf-lfi-in-uploads-feature.md
- Source Type: markdown
- Detected Topics: ssrf, xss, path-traversal, command-injection, file-upload
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `7533b4d5937ccda855584dfc1e017ed6e54de7ca44e9a3fee3f5f74792a0f57c`
- Text SHA256: `a6f3273aa852313bd3597fa52c9e98700815f7626fe576593fb883c551344d5b`


## Content

---
title: "SSRF & LFI In Uploads Feature"
url: "https://medium.com/@raymond-lind/ssrf-lfi-in-uploads-feature-a134aa467abf"
authors: ["Raymond Lind"]
bugs: ["SSRF", "LFI"]
publication_date: "2022-10-24"
added_date: "2022-10-25"
source: "pentester.land/writeups.json"
original_index: 2000
scraped_via: "browseros"
---

# SSRF & LFI In Uploads Feature

Member-only story

SSRF & LFI In Uploads Feature
Raymond Lind
Follow
6 min read
·
Oct 24, 2022

95

Hello fellow hackers, today I will discuss how I found a Server-Side Request Forgery (SSRF) which lead to a Local File Inclusion (LFI) that exposed backend resources in a bug bounty program.

Introduction

Server-Side Request Forgery (SSRF) is a web application vulnerability often characterized by the ability for an attacker to induce the server-side application to make HTTP requests to specific domains provided by that user.

Although without the correct validation, it is possible for the attacker to make connections to backend resources that shouldn’t otherwise be available to them. This is often due to the request originating from the backend server rather than the attackers machine, therefore granting them unauthorized access.

Now that we know the basics, let’s jump into how I ended up finding a SSRF/LFI vulnerability in a bug bounty program’s upload feature.

Initial Finding

I tend to heavily test file upload functionality in bug bounty programs when I see them. This is because file upload vulnerabilities can lead to a bunch of different issues such as Server-Side Request Forgery (SSRF), Cross-Site Scripting (XSS), and sometimes even Remote Command Execution (RCE).

While testing this and uploading a word document, I noticed that the document gets converted into a PDF on the backend, which is later displayed to the user after conversion. This means that the data within the provided file…
