---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-18_how-i-found-unauthorized-bypass-rce.md
original_filename: 2022-09-18_how-i-found-unauthorized-bypass-rce.md
title: How i Found Unauthorized Bypass RCE
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 04daa9bb3731da53d68f5ae0dd646cfd6c8f6b722bb5b579c1ccd5393b4f8704
text_sha256: 62c65bb18443377ec9e67698cbb50cb14f0dd5ce536e5993bb3fc8c663753996
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# How i Found Unauthorized Bypass RCE

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-18_how-i-found-unauthorized-bypass-rce.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `04daa9bb3731da53d68f5ae0dd646cfd6c8f6b722bb5b579c1ccd5393b4f8704`
- Text SHA256: `62c65bb18443377ec9e67698cbb50cb14f0dd5ce536e5993bb3fc8c663753996`


## Content

---
title: "How i Found Unauthorized Bypass RCE"
url: "https://medium.com/@yashshirke7806/how-i-found-unauthorized-bypass-rce-3591a86425a9"
authors: ["Yashshirke"]
bugs: ["RCE", "Old components with known vulnerabilities"]
publication_date: "2022-09-18"
added_date: "2022-09-20"
source: "pentester.land/writeups.json"
original_index: 2157
scraped_via: "browseros"
---

# How i Found Unauthorized Bypass RCE

How i Found Unauthorized Bypass RCE
Yashshirke
Follow
2 min read
·
Sep 18, 2022

34

Easy Vulnerability Leads To admin Console ,P1 type

So i have Started doing hunting on one target { Target Didn’t gave me permission to Disclosed Name of Program}

Lets start

after hunting on some low hanging. And after some Recon i was hunting on Technologies which was Web logic Service and i found CVE 2020–14882 it was vulnerable to 12.1.3.0.0 version of web logic

( oracle ) Version 12.1.3.0.0

lets start with exploit,

For example lets assume the site was hosted on this IP : 192.168.1.79 and the port of web logic is 7001

As we all know we can bypass WAF sometimes with just “ / “

This was the payload :- %252e%252e%252f you Guyz can encode and check , So this payload was just bypassing Waf now i was not happy with bypassing WAF i was hunting for big impact so i found one more payload which Directing me to admin console access

Payload :- https://192.168.1.79:7001/console/images/%252e%252e%252fconsole.portal
The IP is just for example, Focus on payload which was this /console/images/%252e%252e%252fconsole.portal

SO here is the screen Shot POC

Press enter or click to view image in full size
Admin Console

Now Tip for Bug Hunters,

Get Yashshirke’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

How you can Find this, Where you can Find This,

Find on shodan.io with some dorking
Websites which used Web logic Oracle
Tip for beginners
What if we dont have IP ? what if we dont see port open of 7001 ? how we can exploit ? without this ? ……. Don’t worry Guys you can do it
SO just change the url like this :- https://taget.com//console/images/%252e%252e%252fconsole.portal
But keep one thing in mind that first you need to find login page of console so the end point of website can be anything
For references Video Poc
https://youtu.be/O0ZnLXRY5Wo

Thanks All stay connected will post more new things

Instagram : @yash.ethics
