---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-17_ffuf-ing-recon-or-how-to-get-to-p1p3-from-a-slightly-different-recon.md
original_filename: 2022-07-17_ffuf-ing-recon-or-how-to-get-to-p1p3-from-a-slightly-different-recon.md
title: FFUF-ing RECON, or how to get to P1–P3 from a slightly different recon
category: documents
detected_topics:
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: 3a1d78ee3d77b784a578a50d4f63292d4954579b3f0b32b8f3b44c2423a7eac1
text_sha256: 667e263622e99d12398d8f96f265e83fbd4aa56cd79adc6fb8111642cabddcbe
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# FFUF-ing RECON, or how to get to P1–P3 from a slightly different recon

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-17_ffuf-ing-recon-or-how-to-get-to-p1p3-from-a-slightly-different-recon.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `3a1d78ee3d77b784a578a50d4f63292d4954579b3f0b32b8f3b44c2423a7eac1`
- Text SHA256: `667e263622e99d12398d8f96f265e83fbd4aa56cd79adc6fb8111642cabddcbe`


## Content

---
title: "FFUF-ing RECON, or how to get to P1–P3 from a slightly different recon"
page_title: "FFUF-ing RECON. , or how to get to P1–P3 from a… | by Vuk Ivanovic | InfoSec Write-ups"
url: "https://infosecwriteups.com/ffuf-ing-recon-1ee4e79b3256"
authors: ["Vuk Ivanovic"]
bugs: ["vHost misconfiguration", "403 bypass", "Information disclosure"]
publication_date: "2022-07-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2438
scraped_via: "browseros"
---

# FFUF-ing RECON, or how to get to P1–P3 from a slightly different recon

Member-only story

FFUF-ing RECON
, or how to get to P1–P3 from a slightly different recon
Vuk Ivanovic
Follow
3 min read
·
Jul 17, 2022

166

2

When it comes to recon, especially looking for subdomains, there have been a ton of tools and writeups since the beginning of hacking. But, somehow the least discussed approach is the one that can yield the most amazing results (not always though), and I had only found one tool dealing with it before ffuf existed, but I gave up on it (could be I was doing it wrong, but whatever (: ). I’m talking about vhost discovery using ffuf, which can also be used for regular subdomain discovery with easier to configure against false positives.

FFUF for more than dir bruteforce

There is a nice piece of seemingly simple way to achieve vhosts scanning using ffuf:

Press enter or click to view image in full size
Screenshot from GitHub https://github.com/ffuf/ffuf#virtual-host-discovery-without-dns-records

I mean, it’s logically sound… up to a point. The thing that it doesn’t account for is that sometimes there are subdomains/vhosts with 403, 404, 400 that are still interesting to dig deeper into. Using ffuf for file/folder bruteforcing and gau/wayback machine to maybe find some obscure yet interesting endpoints.

Another thing is figuring out whether the size of response means false positive or a redirect to the same destination, etc. That is why you also have to keep an eye on the output and if you notice that the size is the same for multiple subdomains, and also what subdomains…
