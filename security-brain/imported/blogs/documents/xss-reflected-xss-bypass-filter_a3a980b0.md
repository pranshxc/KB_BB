---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-23_xss-reflected-xss-bypass-filter.md
original_filename: 2019-04-23_xss-reflected-xss-bypass-filter.md
title: '[XSS] Reflected XSS Bypass Filter'
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
raw_sha256: a3a980b082cdb13666ade58485d7c64d22539ecce831cb2c2bf7363cc79e9359
text_sha256: 3f7d7dc4fe4e65af05891502ef3479c798ded2cc34c8cd6fe94a9e423aef9ac8
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# [XSS] Reflected XSS Bypass Filter

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-23_xss-reflected-xss-bypass-filter.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `a3a980b082cdb13666ade58485d7c64d22539ecce831cb2c2bf7363cc79e9359`
- Text SHA256: `3f7d7dc4fe4e65af05891502ef3479c798ded2cc34c8cd6fe94a9e423aef9ac8`


## Content

---
title: "[XSS] Reflected XSS Bypass Filter"
url: "https://medium.com/bugbountywriteup/xss-reflected-xss-bypass-filter-de41d35239a3"
authors: ["Mohamed Sayed (@FlEx0Geek)"]
bugs: ["Reflected XSS"]
publication_date: "2019-04-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5296
scraped_via: "browseros"
---

# [XSS] Reflected XSS Bypass Filter

[XSS] Reflected XSS Bypass Filter
Mohamed Sayed
Follow
2 min read
·
Apr 23, 2019

229

6

Press enter or click to view image in full size

I would like to write about this but it takes some time to bypass the filter and some time to find the right HTML tag to write a payload.

Get Mohamed Sayed’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I was testing on a program which is private let’s call it example.com I found a search field so I start to test it with my lovely value ‘“>< to know what will be blocked I found that the value added to a lot of places on the source code but almost all of them encoded with HTML-Encode but I found my value added on a tag called dfn without encoding so there is a hope to find an XSS so I added an XSS payload but It redirects me to block page because of these < > values not accepted after a few minutes I understand how the function works the function block the request if this < connected to anything like the word <svg or special char <! and if I write a complete HTML tag the filter will delete all of the tag I tried to bypass it using URL-Encoding but it doesn’t work so I tried double encode and it works to bypass it and I wrote a payload like that %253Csvg onload=alert0)%253E this payload added to the source code but there was a problem that the filter delete this = I tried a lot to bypass this but I couldn’t :( I told to my self what? after all of this time I couldn’t execute XSS payload

I asked my friends about payloads without this = and I asked Google but I didn’t found anything, the problem not here the problem is my mind was sleep and when he wakes up I got it

I forgot the king of XSS payloads <script>alert(0)</script> WOW I don’t know how I forgot it but this is our guy so I decoded it and try to execute but there is another problem is these two ( ) so I replaced it with `` and the payload executed I was WooooooooooW

I like this bug and I like you who completed the topic I hope it is helpful to you guys, thanks for reading this, goodbye.
