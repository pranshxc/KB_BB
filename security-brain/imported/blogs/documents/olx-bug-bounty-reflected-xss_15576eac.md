---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-03-13_olx-bug-bounty-reflected-xss.md
original_filename: 2019-03-13_olx-bug-bounty-reflected-xss.md
title: 'OLX Bug Bounty: Reflected XSS'
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
raw_sha256: 15576eac2a4ff63f12ea789c076d5b4aed685be4d6eddcc2158b3476fc20e192
text_sha256: a1981128948d1702b4c4677995e89d3afb82ca88f3e3dc87b8837351b2e329aa
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# OLX Bug Bounty: Reflected XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-03-13_olx-bug-bounty-reflected-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `15576eac2a4ff63f12ea789c076d5b4aed685be4d6eddcc2158b3476fc20e192`
- Text SHA256: `a1981128948d1702b4c4677995e89d3afb82ca88f3e3dc87b8837351b2e329aa`


## Content

---
title: "OLX Bug Bounty: Reflected XSS"
url: "https://medium.com/@abaykandotcom/olx-bug-bounty-reflected-xss-adb3095cd525"
authors: ["Mukhammad Akbar (@abaykandotcom)"]
programs: ["OLX"]
bugs: ["Reflected XSS"]
publication_date: "2019-03-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5362
scraped_via: "browseros"
---

# OLX Bug Bounty: Reflected XSS

OLX Bug Bounty: Reflected XSS
abay - Akbar Kustirama
Follow
1 min read
·
Mar 13, 2019

85

1

Who would have thought that there was even a bug that we could find on page 404 Not Found right?

Get abay - Akbar Kustirama’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This time I wrote up when I found Reflected XSS on one of the domains in-scope by OLX, sharjah.dubizzle.com.

Step to Reproduce
Visit https://sharjah.dubizzle.com/property-for-sale/land" accesskey="X" onclick=alert(1337) codelatte="/2018/10/10/commercial-land-for-sale-in-al-sajja-12/ (you can copy and paste).
XSS is reflected inside HTML Link tag
Press enter or click to view image in full size
Press ALT + SHIFT + X in keyboard to trigger XSS payload.
Alert will showing up.
Press enter or click to view image in full size

After the bug was fixed, my name entered on the Security Hall of Fame 😎

Reference

https://hackerone.com/reports/504984 (Original Report).
https://portswigger.net/blog/xss-in-hidden-input-fields (XSS in hidden input fields).

PS: Sorry, maybe there are some irreverent words. It’s semi-google-translate. Hopefully you understand that xD
