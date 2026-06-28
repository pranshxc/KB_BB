---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-02-23_how-automation-detected-default-admin-credential-worth-500.md
original_filename: 2024-02-23_how-automation-detected-default-admin-credential-worth-500.md
title: How Automation Detected Default Admin Credential Worth $500
category: documents
detected_topics:
- idor
- access-control
- command-injection
- rate-limit
- automation-abuse
tags:
- imported
- documents
- idor
- access-control
- command-injection
- rate-limit
- automation-abuse
language: en
raw_sha256: 292190942d1865bfc2923c3336ab95ce3511149b67679b0641fa81f89016b2d5
text_sha256: 37612e0b6001aab10dd015ceb2b5accedb8859aa96a1ab54f8dd72acc62f6b92
ingested_at: '2026-06-28T07:32:31Z'
sensitivity: unknown
redactions_applied: false
---

# How Automation Detected Default Admin Credential Worth $500

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-02-23_how-automation-detected-default-admin-credential-worth-500.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, rate-limit, automation-abuse
- Ingested At: 2026-06-28T07:32:31Z
- Redactions Applied: False
- Raw SHA256: `292190942d1865bfc2923c3336ab95ce3511149b67679b0641fa81f89016b2d5`
- Text SHA256: `37612e0b6001aab10dd015ceb2b5accedb8859aa96a1ab54f8dd72acc62f6b92`


## Content

---
title: "How Automation Detected Default Admin Credential Worth $500"
url: "https://vijetareigns.medium.com/how-automation-detected-default-admin-credential-worth-500-d6c09719d307"
authors: ["the_unluck_guy (@7he_unlucky_guy)"]
bugs: ["Default credentials"]
bounty: "500"
publication_date: "2024-02-23"
added_date: "2024-02-27"
source: "pentester.land/writeups.json"
original_index: 412
scraped_via: "browseros"
---

# How Automation Detected Default Admin Credential Worth $500

Member-only story

How Automation Detected Default Admin Credential Worth $500
the_unlucky_guy
Follow
3 min read
·
Feb 23, 2024

1.2K

13

FREE ARTICLE LINK👈

Hello hackers, I am back with a new bug bounty write-up. In this blog, I am going to show how my automation discovered default admin credentials in the company’s internal IT portal — Sapphire IMS. The company has a bug bounty program on Hackerone. I will be using redacted.com as the main domain.

*.redacted.com is in the scope. As usual, I started with subdomain enumeration and found approximately 70 subdomains out of which only 30 are reachable. I already spent a few days on this program and submitted a few IDOR and access control bugs on the main domain.

There are 10 subdomains that are not reachable, but their names are airflow.redacted.com, ims.redacted.com, etc. It seems that there is some internal portal running on them, and I assume that access to the portal is limited to VPN/Office IPs.

I assumed below test cases for all the internal portal:

The portal is unauthenticated
The portal is authenticated
The portal may have a default login credential

Based on that, I assume that there is a possibility in the future that, by mistake, all the portals will be made public by the developer. Relying on my prediction, I added these subdomains to my automation. My automation runs every 10 minutes. I use some community-created and some custom nuclei templates to automatically scan the subdomains for default credentials. I…
