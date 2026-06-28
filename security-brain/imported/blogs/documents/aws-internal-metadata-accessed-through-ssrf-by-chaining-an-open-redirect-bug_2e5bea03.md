---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-24_aws-internal-metadata-accessed-through-ssrf-by-chaining-an-open-redirect-bug.md
original_filename: 2021-04-24_aws-internal-metadata-accessed-through-ssrf-by-chaining-an-open-redirect-bug.md
title: AWS internal metadata accessed through SSRF by Chaining an Open Redirect bug
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
raw_sha256: 2e5bea039439fdaa7020cdd458311b324322680b02b2e4fff422cf5763eb71b2
text_sha256: 6fb9c6cdd84486b2724668568d06dd6a9d460082753a2f959fabe5ece3c45a65
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# AWS internal metadata accessed through SSRF by Chaining an Open Redirect bug

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-24_aws-internal-metadata-accessed-through-ssrf-by-chaining-an-open-redirect-bug.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, cloud-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `2e5bea039439fdaa7020cdd458311b324322680b02b2e4fff422cf5763eb71b2`
- Text SHA256: `6fb9c6cdd84486b2724668568d06dd6a9d460082753a2f959fabe5ece3c45a65`


## Content

---
title: "AWS internal metadata accessed through SSRF by Chaining an Open Redirect bug"
url: "https://notifybugme.medium.com/aws-internal-metadata-accessed-through-ssrf-by-chaining-an-open-redirect-bug-c4b0e4838dc"
authors: ["Santosh Kumar Sha (@killmongar1996)"]
bugs: ["SSRF", "Open redirect"]
publication_date: "2021-04-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3710
scraped_via: "browseros"
---

# AWS internal metadata accessed through SSRF by Chaining an Open Redirect bug

Member-only story

AWS internal metadata accessed through SSRF by Chaining an Open Redirect bug
Santosh Kumar Sha(@killmongar1996)
Follow
5 min read
·
Apr 24, 2021

400

2

Hi, everyone

My name is Santosh Kumar Sha, I’m a security researcher from India(Assam). In this article, I will be describing how I was able to get AWS metadata accessed through SSRF by chaining it with a open direct vulnerability.

I am now offering 1:1 sessions to share my knowledge and expertise:

topmate.io/santosh_kumar_sha

TOOLS used for the exploitation

1. Subfinder (https://github.com/projectdiscovery/subfinder)

2. httpx (https://github.com/projectdiscovery/httpx)

3. gau(Corben) — https://github.com/lc/gau

4. waybackurls(tomnomnom) — https://github.com/tomnomnom/waybackurls

Story Behind the bug:

This is the write of my Recent bug that i found . While I was doing recon for gathering all urls from internet archives using waybackurls and gau. So started fuzzing the for ssrf vulnerability and found one but there was some filter going on behind the server which not allow me access the internal metadata but i chained it with open redirect bug to bypass the waf to access the internal AWS metadata.

Here it goes:

Suppose we assume the target name is example.com where every thing is in-scope like this:
