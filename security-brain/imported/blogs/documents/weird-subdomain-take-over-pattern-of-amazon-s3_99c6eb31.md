---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-31_weird-subdomain-take-over-pattern-of-amazon-s3.md
original_filename: 2020-05-31_weird-subdomain-take-over-pattern-of-amazon-s3.md
title: Weird “Subdomain Take Over” pattern of Amazon S3
category: documents
detected_topics:
- cloud-security
- command-injection
tags:
- imported
- documents
- cloud-security
- command-injection
language: en
raw_sha256: 99c6eb3169df9a8480697ed072280a0a8a6e839562d7180b935e8d3962c2910a
text_sha256: a0d57621e82a09a40f3126fba617810c5c12108df6af56e557811b4520c6c1be
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Weird “Subdomain Take Over” pattern of Amazon S3

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-31_weird-subdomain-take-over-pattern-of-amazon-s3.md
- Source Type: markdown
- Detected Topics: cloud-security, command-injection
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `99c6eb3169df9a8480697ed072280a0a8a6e839562d7180b935e8d3962c2910a`
- Text SHA256: `a0d57621e82a09a40f3126fba617810c5c12108df6af56e557811b4520c6c1be`


## Content

---
title: "Weird “Subdomain Take Over” pattern of Amazon S3"
url: "https://medium.com/@secureITmania/weird-subdomain-take-over-pattern-of-amazon-s3-75165ab2e883"
authors: ["Simgamsetti Manikanta (@zaheckmania)"]
bugs: ["Subdomain takeover"]
publication_date: "2020-05-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4542
scraped_via: "browseros"
---

# Weird “Subdomain Take Over” pattern of Amazon S3

Member-only story

Weird “Subdomain Take Over” pattern of Amazon S3
secureITmania
Follow
5 min read
·
May 31, 2020

28

Thanks for huge response to my previous write-ups. Recently I participated in a Bug Bounty program and I have found “Sub-domain takeover” issue by leveraging the Amazon S3 hosting service.

Even though you have an idea on the subdomain takeover via AWS S3. In this write-up, I will show the non-typical way of S3 subdomain takeover and also show the OSINT process to find the s3 regions and finally how I found the correct region of the target.

Introduction — Sub-Domain & S3

Subdomain: A Subdomain is a domain that the part of a larger domain. For example blog.example.com, www.example.com are subdomains of example.com

AWS S3: S3 is Simple Storage Service provided by the AWS cloud platform. In which they provide the cloud object storage and that offers industry-leading scalability, data availability, security, and performance.

Subdomain Takeover:

Subdomain takeover is a process of registering a non-existing domain name to gain control over another domain.

Actually before going to understand the subdomain takeover we have to discuss “DNS & CNAME” record. The main logic behind subdomain takeover is tangled with the actual subdomain CNAME record. CNAME records can be used to alias one…
