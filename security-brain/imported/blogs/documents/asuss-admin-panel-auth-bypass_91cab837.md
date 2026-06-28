---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-18_asuss-admin-panel-auth-bypass.md
original_filename: 2018-12-18_asuss-admin-panel-auth-bypass.md
title: Asus’S Admin Panel Auth Bypass
category: documents
detected_topics:
- ssrf
- command-injection
- rate-limit
tags:
- imported
- documents
- ssrf
- command-injection
- rate-limit
language: en
raw_sha256: 91cab8375aa72faec93e6d83c2114d2137306fe944d33017a120b958f147b858
text_sha256: 1141af1e4a134129c51437a5830bcb316a018c157690c534fe7f1b83ca9b9d2f
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Asus’S Admin Panel Auth Bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-18_asuss-admin-panel-auth-bypass.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, rate-limit
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `91cab8375aa72faec93e6d83c2114d2137306fe944d33017a120b958f147b858`
- Text SHA256: `1141af1e4a134129c51437a5830bcb316a018c157690c534fe7f1b83ca9b9d2f`


## Content

---
title: "Asus’S Admin Panel Auth Bypass"
page_title: "ASUS’S ADMIN PANEL AUTH BYPASS. So this is the write up for my Asus’s… | by Zeeshan Mustafa | Medium"
url: "https://medium.com/@mustafakhan_89646/asuss-admin-panel-auth-bypass-af5062584ddf"
authors: ["Mustafa Khan (@by6153)"]
programs: ["Asus"]
bugs: ["Authentication bypass"]
publication_date: "2018-12-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5515
scraped_via: "browseros"
---

# Asus’S Admin Panel Auth Bypass

Zeeshan Mustafa
Follow
2 min read
·
Dec 18, 2018

144

2

Press enter or click to view image in full size

ASUS’S ADMIN PANEL AUTH BYPASS

So this is the write up for my Asus’s admin panel bypass report that most of my friends were asking me. If you have private programs to test feel free to contact me on https://twitter.com/by6153

The vulnerability was within their (.in) domain (asus.in) it was a PHP based admin panel and the vulnerability were:

1: forced browsing. (Want to know more? click here)

2: HTTP response tampering. (want to know more? Click here)

To exploit this I had three ways.

1: NoRedirect (Firefox Add-on)

2: Turning off JavaScript of browser.

3: HTTP response tampering via Burp suite.

Get Zeeshan Mustafa’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

========================================

Asus’s Admin panel Login page

========================================

URL: http://asus.in/where-to-buy/webadmin/index.php

As you can see index.php is the login page. So here I brute forced the current directory with Dirbuster and got dashboard.php is present there but directly we can’t access it so here I turned off JavaScript and browsed it again and got access to the panel and tried with no redirect add-on and it was working too. Then I tried HTTP response tampering via Burp Suite and got success. Below is video POC.

Reported Asus’s Security team on

Nov 22, 2018 at 10:12 PM — But they didn’t respond me.

Dec 4, 2018 at 8:38 PM — I had Resend the report to them and they answered this time on.

Dec 5, 2018 at 8:21 AM and fixed it.

I must say they are too slow to answer to your reports.

Check out my SSRF write up Here.
