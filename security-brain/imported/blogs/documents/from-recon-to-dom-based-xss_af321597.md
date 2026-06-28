---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-11-11_from-recon-to-dom-based-xss.md
original_filename: 2017-11-11_from-recon-to-dom-based-xss.md
title: From Recon to DOM-Based XSS
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: af321597210334b911ef14611062e7e92d3828807c0e4147994cec695670a7ab
text_sha256: e722c0fe88889d67df80ee31b7858a2f946405a150eaf5e7e9816e321d1d1c8d
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# From Recon to DOM-Based XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-11-11_from-recon-to-dom-based-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `af321597210334b911ef14611062e7e92d3828807c0e4147994cec695670a7ab`
- Text SHA256: `e722c0fe88889d67df80ee31b7858a2f946405a150eaf5e7e9816e321d1d1c8d`


## Content

---
title: "From Recon to DOM-Based XSS"
url: "https://medium.com/@abdelfattahibrahim/from-recon-to-dom-based-xss-f279602a14cf"
authors: ["Abdelfattah Ibrahim"]
bugs: ["DOM XSS"]
publication_date: "2017-11-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6055
scraped_via: "browseros"
---

# From Recon to DOM-Based XSS

From Recon to DOM-Based XSS
Abdelfattah Ibrahim
Follow
1 min read
·
Nov 12, 2017

155

2

I was doing some google dorking to find out if there’s any interesting files or parameters in the bug bounty program scope so i’ve tried alot of dorks and it was the turn of this one “ site:*.REDACTED.com inurl:file “ and then i found this endpoint : https://REDACTED.com/files/file.htm
and there was some listed articles in the page so i navigated to an article and the url changed to be like this:
https://REDACTED.com/files/file.htm#article1.html
after about 5 minutes i’ve figured out that any thing that you’ll put after “#” it will reflect in an IFRAME html tag
so i tried to open an external domain:
https://REDACTED.com/files/file.htm#http://evil.com
and guess what?

Press enter or click to view image in full size
Get Abdelfattah Ibrahim’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

and then tried to inject XSS payload “javascript:alert(1)” and it worked!
https://REDACTED.com/files/file.htm#javascript:alert(1)

I hope you guys like the writeup it’s pretty simple as you see
regards,
Abdelfattah.
