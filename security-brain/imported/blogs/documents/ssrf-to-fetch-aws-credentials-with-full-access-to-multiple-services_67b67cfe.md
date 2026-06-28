---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-28_ssrf-to-fetch-aws-credentials-with-full-access-to-multiple-services.md
original_filename: 2021-02-28_ssrf-to-fetch-aws-credentials-with-full-access-to-multiple-services.md
title: SSRF to fetch AWS credentials with full access to multiple services
category: documents
detected_topics:
- ssrf
- xss
- command-injection
- cloud-security
tags:
- imported
- documents
- ssrf
- xss
- command-injection
- cloud-security
language: en
raw_sha256: 67b67cfe862c6dd8922e32431eefee8645d23c2a485f089e9e471e8979a13855
text_sha256: a68e3fbd74596700cff38c82aa647a5374c142d2d2d38e8ef70013886f0688a9
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# SSRF to fetch AWS credentials with full access to multiple services

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-28_ssrf-to-fetch-aws-credentials-with-full-access-to-multiple-services.md
- Source Type: markdown
- Detected Topics: ssrf, xss, command-injection, cloud-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `67b67cfe862c6dd8922e32431eefee8645d23c2a485f089e9e471e8979a13855`
- Text SHA256: `a68e3fbd74596700cff38c82aa647a5374c142d2d2d38e8ef70013886f0688a9`


## Content

---
title: "SSRF to fetch AWS credentials with full access to multiple services"
url: "https://zonduu.medium.com/ssrf-to-fetch-aws-credentials-with-full-access-to-various-services-18cd08194e91"
authors: ["Zonduhackerone (@zonduu1)"]
bugs: ["SSRF"]
publication_date: "2021-02-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3852
scraped_via: "browseros"
---

# SSRF to fetch AWS credentials with full access to multiple services

SSRF to fetch AWS credentials with full access to multiple services
Zonduhackerone
Follow
2 min read
·
Feb 28, 2021

151

Press enter or click to view image in full size

This is a post about how I found a simple yet really critical vulnerability in a bug bounty program. It was the most critical bug I have ever found.

All started after I found a path in a subdomain that was almost a blank page with no functionality at all.

It had a few parameters that were all vulnerable to XSS so I reported the issue, it was triaged by Hackerone but at the end (yeah I have bad luck) it was closed as “internal dupe”.

Get Zonduhackerone’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The path was in https://host/payment/? so it was looking really promising that I was able to access this endpoint while being unauthenticated although the page was almost blank.

I didn’t give up and started fuzzing this endpoint as well as trying to find new ones to see if more unauthenticated stuff would show up. After some time I finally got something, a callback to our server.

After identifying the vulnerable parameter urlLogo (I changed the parameter name a bit because I have to redact everything), I started to think it would be a blind SSRF because the response of the url I was providing was not in the response.

Moving this to my blog:

https://zonduu.me/posts/critical-ssrf/
