---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-26_ssrf-bug-leads-to-aws-metadata-exposure.md
original_filename: 2022-10-26_ssrf-bug-leads-to-aws-metadata-exposure.md
title: SSRF Bug Leads To AWS Metadata Exposure
category: documents
detected_topics:
- ssrf
- command-injection
- api-security
- cloud-security
tags:
- imported
- documents
- ssrf
- command-injection
- api-security
- cloud-security
language: en
raw_sha256: 17a986017fbc03cee66e43e2e1a2f1d3b2e988eecaa1ca94a01e6012821f0886
text_sha256: 8dbe8b4a4341adaf599f0bfde66dcc732da042d06955be9d266b56b740b25a18
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# SSRF Bug Leads To AWS Metadata Exposure

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-26_ssrf-bug-leads-to-aws-metadata-exposure.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `17a986017fbc03cee66e43e2e1a2f1d3b2e988eecaa1ca94a01e6012821f0886`
- Text SHA256: `8dbe8b4a4341adaf599f0bfde66dcc732da042d06955be9d266b56b740b25a18`


## Content

---
title: "SSRF Bug Leads To AWS Metadata Exposure"
url: "https://medium.com/@raymond-lind/ssrf-bug-leads-to-aws-metadata-exposure-f2ee7d43c6c3"
authors: ["Raymond Lind"]
bugs: ["SSRF"]
publication_date: "2022-10-26"
added_date: "2022-10-28"
source: "pentester.land/writeups.json"
original_index: 1989
scraped_via: "browseros"
---

# SSRF Bug Leads To AWS Metadata Exposure

Member-only story

SSRF Bug Leads To AWS Metadata Exposure
Raymond Lind
Follow
5 min read
·
Oct 26, 2022

113

1

How can you leverage an SSRF (“Server Side Request Forgery”) vulnerability to evade filters and leak internal AWS credentials on a web application? Today I will discuss how I managed to utilize a webpage screenshot feature to bypass certain filters and exfiltrate server side AWS Metadata.

Introduction

While looking through a certain BBP (“Bug Bounty Program”) I came across an interesting feature in the application. This feature allowed for a user to supply any URL and have the specified webpage captured as an image which would then be provided back to the user.

This feature appeared very interesting because if there were any errors in its configuration or input validation, its functionality could provide an attacker a wide variety of different attack methods. This includes possibly accessing endpoints on the website that I do not otherwise have access to, having the server request any domain of my choosing, and being able to request local resources on the server to screenshot and view myself.

Below I will walk through the methods I applied to attempt to discover flaws in this functionality. Many of these attempts failed but after continuously testing this functionality, it led me to one method that successfully returned any AWS metadata from the back-end server that I requested.
