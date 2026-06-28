---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-25_xss-through-image-proxy-using-svg-image.md
original_filename: 2021-12-25_xss-through-image-proxy-using-svg-image.md
title: XSS through image proxy using SVG image
category: documents
detected_topics:
- cloud-security
- ssrf
- xss
- command-injection
tags:
- imported
- documents
- cloud-security
- ssrf
- xss
- command-injection
language: en
raw_sha256: 1e1f6fd79bc8803aef719e2177cdc70dae27716fda5663f07f4d6e3817e8a1d1
text_sha256: b48db0c8ab6bb55350cb55f3cec3a8806e7b1bee8c51e7026a92cc1b72dcefc1
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# XSS through image proxy using SVG image

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-25_xss-through-image-proxy-using-svg-image.md
- Source Type: markdown
- Detected Topics: cloud-security, ssrf, xss, command-injection
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `1e1f6fd79bc8803aef719e2177cdc70dae27716fda5663f07f4d6e3817e8a1d1`
- Text SHA256: `b48db0c8ab6bb55350cb55f3cec3a8806e7b1bee8c51e7026a92cc1b72dcefc1`


## Content

---
title: "XSS through image proxy using SVG image"
url: "https://3bodymo.medium.com/xss-through-image-proxy-using-svg-image-49cdf955cf4f"
authors: ["Abdullah Mohamed (@3bodymo_)"]
bugs: ["XSS"]
publication_date: "2021-12-25"
added_date: "2023-06-25"
source: "pentester.land/writeups.json"
original_index: 3061
scraped_via: "browseros"
---

# XSS through image proxy using SVG image

XSS through image proxy using SVG image
Abdullah Abdelrazek
Follow
2 min read
·
Dec 25, 2021

161

Press enter or click to view image in full size

Hi
everyone, today’s story will be short because there are not many details in it.

I got a private invitation to hunt in the program, once I opened the website, I used to check the place of images and JS files, because if they are uploaded on service like Amazon S3 bucket, I will scan this bucket.

When I clicked on a random image I saw the link of image like this:

https://company.com/1/2010/1920/https://example.s3.amazonaws.com/images/a1.jpg

From here I have two thing to do, the first thing is to scan S3 bucket to know if there is a misconfiguration or not .. here is my writeup to know how to scan this type of misconfiguration.

Get Abdullah Abdelrazek’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The second thing I did (which it is the reason to write this writeup) is check if the endpoint accepts an images from my host or not, I tried and it works.

Press enter or click to view image in full size

I tried a files with different extensions to know if I can exploit SSRF, but unfortunately the endpoint only accept images extension.

The last thing I tried, I made an SVG file contain my XSS payload. After I made it I put my SVG file URL in the endpoint and the vulnerable link was like that:

https://company.com/1/2010/1920/https://attacker.com/payloads/poc.svg

Contrary to what I expected, the alert got from the company’s host and not from my host.

Press enter or click to view image in full size
How to fix?

The team fixed the bug through make the proxy only accept images from their S3 bucket that belong to them.

Press enter or click to view image in full size

Thanks for your reading, I hope my story was useful.
