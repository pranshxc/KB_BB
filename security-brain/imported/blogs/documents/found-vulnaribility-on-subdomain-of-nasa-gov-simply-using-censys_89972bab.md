---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-19_found-vulnaribility-on-subdomain-of-nasagov-simply-using-censys.md
original_filename: 2022-10-19_found-vulnaribility-on-subdomain-of-nasagov-simply-using-censys.md
title: Found vulnaribility on subdomain of nasa.gov simply using censys
category: documents
detected_topics:
- idor
- command-injection
- rate-limit
- api-security
tags:
- imported
- documents
- idor
- command-injection
- rate-limit
- api-security
language: en
raw_sha256: 89972bab66d2a8035df2550e43eff1f0aa41e423451bb2ff282a918fad684f78
text_sha256: 626e799188b7b0f829abba9f1d9a8aab48947843f37c86bf63c253f4b6d6db15
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Found vulnaribility on subdomain of nasa.gov simply using censys

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-19_found-vulnaribility-on-subdomain-of-nasagov-simply-using-censys.md
- Source Type: markdown
- Detected Topics: idor, command-injection, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `89972bab66d2a8035df2550e43eff1f0aa41e423451bb2ff282a918fad684f78`
- Text SHA256: `626e799188b7b0f829abba9f1d9a8aab48947843f37c86bf63c253f4b6d6db15`


## Content

---
title: "Found vulnaribility on subdomain of nasa.gov simply using censys"
url: "https://medium.com/@kandar.souvik6/found-vulnaribility-on-subdomain-of-nasa-gov-simply-using-censys-d93f253ff560"
authors: ["hacker_might"]
programs: ["NASA"]
bugs: ["Exposed registration page"]
publication_date: "2022-10-19"
added_date: "2022-10-21"
source: "pentester.land/writeups.json"
original_index: 2023
scraped_via: "browseros"
---

# Found vulnaribility on subdomain of nasa.gov simply using censys

Found vulnaribility on subdomain of nasa.gov simply using censys
hacker_might
Follow
Oct 20, 2022

9

1

Hi, i have found low level vulnaribility on subdomain of nasa.gov simply using censys.At first i have used the process mentioned at my blog(https://medium.com/@kandar.souvik6/live-subdomain-enumeration-using-censys-43a8b6e9e775) to find live subdomain of nasa.gov . Then i have found a very interesting internal subdomain redacted.nasa.gov which has signup feature enbled.So an attacker can simply signup into the subdomain and use the whole internal feature.

Get hacker_might’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I have simply reported this VDP of nasa , within a day i got a response -

Press enter or click to view image in full size

They fixed the vulnaribility(after a month whenever i was trying to open the subdomain it was showing ERR_CONNECTION_TIMED_OUT).
