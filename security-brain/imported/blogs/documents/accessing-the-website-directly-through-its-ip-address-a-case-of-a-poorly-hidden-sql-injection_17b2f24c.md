---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-27_accessing-the-website-directly-through-its-ip-address-a-case-of-a-poorly-hidden-.md
original_filename: 2020-08-27_accessing-the-website-directly-through-its-ip-address-a-case-of-a-poorly-hidden-.md
title: Accessing the website directly through its IP address, a case of a poorly hidden
  sql injection
category: documents
detected_topics:
- sqli
- command-injection
- api-security
tags:
- imported
- documents
- sqli
- command-injection
- api-security
language: en
raw_sha256: 17b2f24caddaa2aebbcc017498c1a860078e530b2d16edcb19d80f4454c08cbb
text_sha256: 45c84174e588ca635efd19cd7eb89236d32c72e587149b025057cb628db9a5e5
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Accessing the website directly through its IP address, a case of a poorly hidden sql injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-27_accessing-the-website-directly-through-its-ip-address-a-case-of-a-poorly-hidden-.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, api-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `17b2f24caddaa2aebbcc017498c1a860078e530b2d16edcb19d80f4454c08cbb`
- Text SHA256: `45c84174e588ca635efd19cd7eb89236d32c72e587149b025057cb628db9a5e5`


## Content

---
title: "Accessing the website directly through its IP address, a case of a poorly hidden sql injection"
url: "https://medium.com/bugbountywriteup/accessing-the-website-directly-through-its-ip-address-a-case-of-a-poorly-hidden-sql-injection-82833defbbc3"
authors: ["Vuk Ivanovic"]
bugs: ["SQL injection"]
publication_date: "2020-08-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4291
scraped_via: "browseros"
---

# Accessing the website directly through its IP address, a case of a poorly hidden sql injection

Member-only story

Accessing the website directly through its IP address, a case of a poorly hidden sql injection
Vuk Ivanovic
Follow
3 min read
·
Aug 27, 2020

30

an example: where website.com resolves to ip address 10.2.3.2

You may have heard the expression: hiding in plain sight. And specifically in IT security there is another expression: security through obscurity. This article will be my experience with a bug where one could argue that it was the case of security through obscurity, but it could have been a coincidence. This will be a story of me stumbling onto sql injection (a simple login bypass which logged me into admin panel), but not in a usual way. Either way, it should give you an idea or two for what to look for in the future. Unless if you are already on to it.

First impression, wrong impression:

The bbp in question had a wide scope, the trusty *.website.com. Love those :) Which, of course, meant time to do a lot of recon action. Using tools like massdns, amass, a bit of crt.sh, etc.

When all the subdomains were collected, I started going through those that sounded interesting. And, there was this subdomain which just showed a simple Help/About me type of page. At first glance — nothing there. No forms, no additional links, nothing to give a clue about it being anything, but a static page. Time to move on?
