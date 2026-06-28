---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-22_opera-browser-vpn-bypass.md
original_filename: 2022-09-22_opera-browser-vpn-bypass.md
title: Opera Browser VPN Bypass
category: documents
detected_topics:
- command-injection
- business-logic
tags:
- imported
- documents
- command-injection
- business-logic
language: en
raw_sha256: a1173bb34593326b2409624564b7ed07a1c0809bd8e3052c4ebdb71b7a010b04
text_sha256: 8837ca6dd6c9d2d02d81868626f585892810170c41374b129a924bc6b1e64523
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Opera Browser VPN Bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-22_opera-browser-vpn-bypass.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `a1173bb34593326b2409624564b7ed07a1c0809bd8e3052c4ebdb71b7a010b04`
- Text SHA256: `8837ca6dd6c9d2d02d81868626f585892810170c41374b129a924bc6b1e64523`


## Content

---
title: "Opera Browser VPN Bypass"
url: "https://medium.com/@renwa/opera-browser-vpn-bypass-20877aaf08c0"
authors: ["Renwa (@RenwaX23)"]
programs: ["Opera"]
bugs: ["Privacy issue", "Logic flaw"]
bounty: "1,000"
publication_date: "2022-09-22"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 2131
scraped_via: "browseros"
---

# Opera Browser VPN Bypass

Opera Browser VPN Bypass
Renwa
Follow
2 min read
·
Sep 22, 2022

70

1

While looking at Opera functionalities I stumbled upon the built-in VPN inside the browser and I was able to find a technique that allow an attacker to bypass the VPN connection and get the users real IP.

You can enable the VPN in settings and starting using it

Press enter or click to view image in full size

There is another functionality called Bypass VPN for default search engines that means if you're using google then the VPN will be shutdown for every search you make and surf you do on google.com, the same thing happens for any other default search engine you have like yandex, duckduckgo..

But there is a problem, search engines these days are very powerful and can do many things not just finding pages, you can ask them questions and they will answer it for you, for example you can say what's my ip and will show your IP without going to any other site.

Press enter or click to view image in full size

And most of these search engines have an API that allows to retrieve answers from other cross site requests, for example https://api.duckduckgo.com/?q=where%20is%20paris&format=json&pretty=1 it will show the answer and the problem is you can use this API to get the real IP of the user, POC:
https://api.duckduckgo.com/?q=whats%20my%20ip&format=json&pretty=1

Get Renwa’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Steps to reproduce:
1.Go to settings and change your default search engine to DuckDuckGo
2.Enable VPN and check on the bypass for default search engines
3.Go to https://whatismyipaddress.com/ to see your new IP with VPN
4.Open https://mydomain/opera_vpn_bypass.html to see your IP that we bypassed using the bugs described above

Press enter or click to view image in full size

Code used in my domain:

Press enter or click to view image in full size

Reported 27 sep 2021 and patched after 3 months. Bounty: 1k$

Thanks ~Renwa
