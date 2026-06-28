---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-01_escalating-ssrf-to-accessing-all-user-pii-information-by-aws-metadata.md
original_filename: 2021-06-01_escalating-ssrf-to-accessing-all-user-pii-information-by-aws-metadata.md
title: Escalating SSRF to Accessing all user PII information by aws metadata
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
raw_sha256: dc09b7893b3140de0365316d1b5edbe7cf5cff49a8960569649c8e90b085a6a5
text_sha256: 2052a7c0c754b3c842d61afbbf49e7594c1398f33290a3528d5e298c4c9e5546
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Escalating SSRF to Accessing all user PII information by aws metadata

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-01_escalating-ssrf-to-accessing-all-user-pii-information-by-aws-metadata.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, cloud-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `dc09b7893b3140de0365316d1b5edbe7cf5cff49a8960569649c8e90b085a6a5`
- Text SHA256: `2052a7c0c754b3c842d61afbbf49e7594c1398f33290a3528d5e298c4c9e5546`


## Content

---
title: "Escalating SSRF to Accessing all user PII information by aws metadata"
url: "https://notifybugme.medium.com/escalating-ssrf-to-accessing-all-user-pii-information-by-aws-metadata-aabcfd5a3e0e"
authors: ["Santosh Kumar Sha (@killmongar1996)"]
bugs: ["SSRF"]
publication_date: "2021-06-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3608
scraped_via: "browseros"
---

# Escalating SSRF to Accessing all user PII information by aws metadata

Member-only story

Escalating SSRF to Accessing all user PII information by aws metadata
Santosh Kumar Sha(@killmongar1996)
Follow
6 min read
·
May 31, 2021

376

2

Hi, everyone

My name is Santosh Kumar Sha, I’m a security researcher from India(Assam). In this article, I will be describing how I was able to leaked all user PII information by SSRF AWS metadata exploitation.

I am now offering 1:1 sessions to share my knowledge and expertise:

topmate.io/santosh_kumar_sha

SPECIAL COVID-19 Note:

Don’t go outside without any reason . Stay home be safe and also safe other. Special request to my fellow bug-bounty hunter Take care of your health .

TOOLS used for the exploitation

1. Subfinder (https://github.com/projectdiscovery/subfinder)

2. httpx (https://github.com/projectdiscovery/httpx)

3. gau(Corben) — https://github.com/lc/gau

4. waybackurls(tomnomnom) — https://github.com/tomnomnom/waybackurls.

Story Behind the bug:

This is the write of my Recent bug that i found . While I was doing recon for gathering all urls from internet archives using waybackurls and gau. So started fuzzing the for ssrf vulnerability and found one but there was some filter going on behind the server which not allow me access the internal metadata but i bypass the waf to access the internal AWS metadata.

Here it goes:
