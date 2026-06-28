---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-20_how-i-was-able-find-mass-leaked-aws-s3-bucket-from-js-file.md
original_filename: 2021-07-20_how-i-was-able-find-mass-leaked-aws-s3-bucket-from-js-file.md
title: How I was able Find mass leaked AWS s3 bucket from js File
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
raw_sha256: c9e4973af762cf90ad487578de335d8ad884ce38496b06a9a4264da975a1a92d
text_sha256: 170c73cd1934bb48dcb3443d35873e68852b011f0623573f11ad8e8aa588b03f
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able Find mass leaked AWS s3 bucket from js File

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-20_how-i-was-able-find-mass-leaked-aws-s3-bucket-from-js-file.md
- Source Type: markdown
- Detected Topics: cloud-security, command-injection
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `c9e4973af762cf90ad487578de335d8ad884ce38496b06a9a4264da975a1a92d`
- Text SHA256: `170c73cd1934bb48dcb3443d35873e68852b011f0623573f11ad8e8aa588b03f`


## Content

---
title: "How I was able Find mass leaked AWS s3 bucket from js File"
url: "https://notifybugme.medium.com/how-i-was-able-find-mass-leaked-aws-s3-bucket-from-js-file-6064a5c247f8"
authors: ["Santosh Kumar Sha (@killmongar1996)"]
bugs: ["AWS misconfiguration"]
publication_date: "2021-07-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3493
scraped_via: "browseros"
---

# How I was able Find mass leaked AWS s3 bucket from js File

Member-only story

How I was able Find mass leaked AWS s3 bucket from js File
Santosh Kumar Sha(@killmongar1996)
Follow
4 min read
·
Jul 20, 2021

639

2

Hi, everyone

My name is Santosh Kumar Sha, I’m a security researcher from India(Assam). In this article, I will be describing How I was able Find mass leaked AWS S3 bucket from js File.

I am now offering 1:1 sessions to share my knowledge and expertise:

topmate.io/santosh_kumar_sha

SPECIAL COVID-19 Note:

Don’t go outside without any reason . Stay home be safe and also safe other. Special request to my fellow bug-bounty hunter Take care of your health and get vaccinated.

TOOLS used for the exploitation

1. Subfinder (https://github.com/projectdiscovery/subfinder)

2. httpx (https://github.com/projectdiscovery/httpx)

3. gau(Corben) — https://github.com/lc/gau

4. waybackurls(tomnomnom) — https://github.com/tomnomnom/waybackurls.

Story Behind the bug:

This is the write of my Recent bug that i found . While I was doing recon on js file. How I was able Find mass leaked AWS s3 bucket from js File.

Here it goes:

Suppose we assume the target name is example.com where every thing is in-scope like this:

In-scope : *.example.com

To gather all the subdomain from internet archives i have used subfinder …
