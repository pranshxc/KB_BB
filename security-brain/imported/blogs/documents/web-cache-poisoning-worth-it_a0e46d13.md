---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-02_web-cache-poisoning-worth-it.md
original_filename: 2023-01-02_web-cache-poisoning-worth-it.md
title: Web-Cache Poisoning $$$? Worth it?
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
raw_sha256: a0e46d13cf8c3d655c3d65f4381547322d68755c940044de5b4711220d704233
text_sha256: 7d4c52d7d57b4b7d223dd4386afb0a88a6e5095b9a90fee8907cf01172b1b8bd
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Web-Cache Poisoning $$$? Worth it?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-02_web-cache-poisoning-worth-it.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `a0e46d13cf8c3d655c3d65f4381547322d68755c940044de5b4711220d704233`
- Text SHA256: `7d4c52d7d57b4b7d223dd4386afb0a88a6e5095b9a90fee8907cf01172b1b8bd`


## Content

---
title: "Web-Cache Poisoning $$$? Worth it?"
url: "https://yaseenzubair.medium.com/web-cache-poisoning-worth-it-e7c6d88797b1"
authors: ["Yaseen Zubair"]
bugs: ["Web cache poisoning", "XSS"]
bounty: "200"
publication_date: "2023-01-02"
added_date: "2023-01-06"
source: "pentester.land/writeups.json"
original_index: 1711
scraped_via: "browseros"
---

# Web-Cache Poisoning $$$? Worth it?

Web-Cache Poisoning $$$? Worth it?
Yaseen Zubair
Follow
2 min read
·
Jan 2, 2023

157

2

In this article, I will try to guide the readers about a bug that is easy to miss and doesn’t get a lot of attention, but surely it’s worth it. I was testing a website that has a private bug bounty program, the website was secure and I failed in getting any of the bugs I knew, and suddenly a response header took my attention.

Identifying the Vulnerability:

I was navigating through the website with burp suite turned on and proxying the URLs. The website was pretty secure and had very limited functionality, it was behind a WAF as well. There weren’t any interesting subdomains either. So I switched to burp suite and started to analyze different sorts of pages. I came across several pages that look almost identical as far as headers are concerned.

GET /redacted-page1 HTTP/1.1
Host: www.redacted.com
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close
Referer: https://www.redacted.com/
Cookie: _TO_AB_Testing=14

The response returned as:

HTTP/1.1 200 OK
<Snip....
...Snip>>
X-Cache: Miss from cloudfront

While a similar request to /redacted-page2 yielded almost the same response:

HTTP/1.1 200 OK
<snip ...
.... snip>
X-Cache: Hit from cloudfront

The cache hit means that the page was cached at CloudFront. So when any other user requests the /redacted-page2, he will be served via CloudFront’s cached data providing that the user hit the same cache server, which he will, if the user is from a similar geographical location, he is most likely to hit the same cache. Also, since it was a production website I couldn’t damage the availability of the website, so I had to be careful while testing, therefore I cached different parameters by sending requests like: /redacted-page2?dontpoisoneverycache=1, etc.

Get Yaseen Zubair’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I started sending out different headers, by changing the Host header, to see If I was able to redirect the mass users but it returned a server error. Then I tried adding:

X-Forwarded-Host: evil.com
X-Host: evil.com

To my surprise, it was appended as a link on the web-page as:

<a href=”http://evil.com/redacted-page2" >

Upon clicking, I was redirected to evil.com, I quickly changed the network and navigated to the URL via a different browser and the cached page worked :-) I was redirected to evil.com

I tried escalating it to XSS setting header as:

javascript:alert(1)”> and evil.com”onmouseover=alert(1)>
But it was filtered :-(

I reported it to the appropriate team and it was triaged in 2 days. It was classified as medium and was awarded a bounty of 200$.

https://gfycat.com/actualillassassinbug-money-cash-dollars
