---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-21_how-i-got-access-to-essilor-international-company-customer-pii-info-by-aws-metad.md
original_filename: 2023-03-21_how-i-got-access-to-essilor-international-company-customer-pii-info-by-aws-metad.md
title: How I got access to Essilor International company customer PII INFO by AWS
  metadata access through SSRF
category: documents
detected_topics:
- ssrf
- command-injection
- cloud-security
tags:
- imported
- documents
- ssrf
- command-injection
- cloud-security
language: en
raw_sha256: a127a98ecc65bc5a6ae2ed0906d17047c3995889f3415909cd9a9d814b2337e6
text_sha256: 85c1cad67e664acf28e363ccc75538fdb3101dd9f519cf0afdd0665790d8e4a5
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# How I got access to Essilor International company customer PII INFO by AWS metadata access through SSRF

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-21_how-i-got-access-to-essilor-international-company-customer-pii-info-by-aws-metad.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, cloud-security
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `a127a98ecc65bc5a6ae2ed0906d17047c3995889f3415909cd9a9d814b2337e6`
- Text SHA256: `85c1cad67e664acf28e363ccc75538fdb3101dd9f519cf0afdd0665790d8e4a5`


## Content

---
title: "How I got access to Essilor International company customer PII INFO by AWS metadata access through SSRF"
url: "https://notifybugme.medium.com/how-i-got-access-to-essilor-international-company-customer-pii-info-by-aws-metadata-access-through-3da02f4c79f0"
authors: ["Santosh Kumar Sha (@killmongar1996)"]
bugs: ["SSRF"]
publication_date: "2023-03-21"
added_date: "2023-03-23"
source: "pentester.land/writeups.json"
original_index: 1351
scraped_via: "browseros"
---

# How I got access to Essilor International company customer PII INFO by AWS metadata access through SSRF

Member-only story

How I got access to Essilor International company customer PII INFO by AWS metadata access through SSRF
Santosh Kumar Sha(@killmongar1996)
Follow
4 min read
·
Mar 21, 2023

143

1

Hi, everyone

My name is Santosh Kumar Sha, I’m a security researcher from India(Assam). In this article, I will be Describing How I was able Find multiple SSRF with aws metadata access ON a Essilor International company System and Get access to there production server.

I am now offering 1:1 sessions to share my knowledge and expertise:

topmate.io/santosh_kumar_sha

SPECIAL Note:

Don’t go outside test scope without any permission. Stay safe and also hack safe . Special request to my fellow bug-bounty hunter Take care of your health and always abide the rule of engagement.

TOOLS used for the exploitation

1. Subfinder (https://github.com/projectdiscovery/subfinder)

2. httpx (https://github.com/projectdiscovery/httpx)

3. gau(Corben) — https://github.com/lc/gau

4. waybackurls(tomnomnom) — https://github.com/tomnomnom/waybackurls.

Story Behind the bug:

This is the write of my compromising the insurance company production and get access to 100GB customer High profile data by SSRF and escalating it get their aws production server customer stored data.
