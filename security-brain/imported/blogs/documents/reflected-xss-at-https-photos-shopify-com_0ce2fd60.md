---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-02-21_reflected-xss-at-httpsphotosshopifycom.md
original_filename: 2019-02-21_reflected-xss-at-httpsphotosshopifycom.md
title: Reflected XSS at https://photos.shopify.com
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 0ce2fd604fd3643d7f03479e02499aec5df771d1560341cace9cf500879e0a4b
text_sha256: 44b19d5b4640cae0babb56bcf82d4a5c01b7a9c17a1b0b2229a9118856235bc6
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Reflected XSS at https://photos.shopify.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-02-21_reflected-xss-at-httpsphotosshopifycom.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `0ce2fd604fd3643d7f03479e02499aec5df771d1560341cace9cf500879e0a4b`
- Text SHA256: `44b19d5b4640cae0babb56bcf82d4a5c01b7a9c17a1b0b2229a9118856235bc6`


## Content

---
title: "Reflected XSS at https://photos.shopify.com"
url: "https://medium.com/@modam3r5/reflected-xss-at-https-photos-shopify-com-ea696db3915c"
authors: ["Ahamed Morad (@Modam3r5)"]
programs: ["Shopify"]
bugs: ["Reflected XSS"]
publication_date: "2019-02-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5397
scraped_via: "browseros"
---

# Reflected XSS at https://photos.shopify.com

Reflected XSS at https://photos.shopify.com/
Modam3r5
Follow
2 min read
·
Feb 21, 2019

76

3

Hi again ❤,

this time i would like to share an XSS bug that i found at 
Shopify,
 the bug was relay easy to find if you read the source of the page, so i hope what i would like to share help you to find a bug ^_^.

Description :

the domain https://photos.shopify.com/ is one of 
Shopify
 gallery site to share photos and information about event etc, so the first thing that i did to understand the site shows the source of the page and by looking inside it i notice that every image has a parameter `pid` which contains information about the ID of the image and it’s included at the image TAG.

this something good if you trying to find a hidden parameter to test an XSS attack or content injected at the site.

so by adding this parameter to the end of the link and put this payload as the value for it javascript:alert("modam3r").

Press enter or click to view image in full size
the XSS was run successfully

for the first time, I was thinking that this kind of hidden parameter but after doing more search and try a random different parameter, collect that the site accepts any parameter and it returns with the value of it inside the `img` TAG, so any payload will be run successfully as I think.

Get Modam3r5’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

i send the report to 
Shopify
 and after one day i got this response

Press enter or click to view image in full size

so I moved and send the report to pixieset.com team about this, and they fixed the bug without any response to my report or give any bounty ^_^.

Results or tips:

always look for a hidden parameter, and try to use random parameters that maybe return with something good to you.

keep in mind not all report will return with bounty sometimes it’s return with Disappointment.

Time Line:

11–02–2018 report send to 
Shopify
.
12–02–2018 team response and closed as Informative.
12–02–2018 report send again to pixieset.com team with full details.
21–02–2019 the bug was fix by pixieset.com without any response from them.

@modam3r5
