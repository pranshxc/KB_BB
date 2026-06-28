---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-24_server-side-request-forgery-in-openid-support.md
original_filename: 2018-12-24_server-side-request-forgery-in-openid-support.md
title: Server-side Request Forgery in OpenID support
category: documents
detected_topics:
- ssrf
- command-injection
tags:
- imported
- documents
- ssrf
- command-injection
language: en
raw_sha256: d413da87236e3b378f28bb5943ac570c0bbd411af8fac712f60cbe112f489653
text_sha256: b520018e75cfc9ca95ecfff429c2fe230068f6f490a77b7bc0ddb79221733459
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Server-side Request Forgery in OpenID support

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-24_server-side-request-forgery-in-openid-support.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `d413da87236e3b378f28bb5943ac570c0bbd411af8fac712f60cbe112f489653`
- Text SHA256: `b520018e75cfc9ca95ecfff429c2fe230068f6f490a77b7bc0ddb79221733459`


## Content

---
title: "Server-side Request Forgery in OpenID support"
url: "https://medium.com/@putracraft.theworld/server-side-request-forgery-in-openid-support-defcc64d5e41"
authors: ["Putra Adhari"]
programs: ["Liberapay"]
bugs: ["SSRF"]
publication_date: "2018-12-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5507
scraped_via: "browseros"
---

# Server-side Request Forgery in OpenID support

Server-side Request Forgery in OpenID support
Putra Adhari
Follow
2 min read
·
Dec 24, 2018

81

1

Liberapay Profile at HackerOne

I just want find Bug at Liberapay but when i want to change Photo Profile the page will auto Redirect at libravatar.org .

Steps to Reproduce

I must Register in libravatar.org to become to member.
And go to Profile Page there have Add a new OpenID menu and Click it
in the Page you can add URL from everywhere and let’s time to Exploit that with SSRF
4.I try to add URL like this : http://127.0.0.1:31337

Press enter or click to view image in full size

The Page will Write <urlopen error [Errno 111] Connection refused> because the Port isn’t Open but if i add URL like this http://127.0.0.1:80 the Page will Write “No usable OpenID services found for http://127.0.0.1:80” (PORT 80 is Open)

Press enter or click to view image in full size

If i check with Nmap is like this 80/tcp open http Apache httpd

And now i’ll try to get Request from VPS .
i add URL like this : http://myvpsserver.example:31337 and trying with netcat with port 31337 .
And Working !!!

Press enter or click to view image in full size

Reference : https://www.hackerone.com/blog-How-To-Server-Side-Request-Forgery-SSRF

Impact

Server Side Request Forgery (SSRF) refers to an attack where in an attacker is able to send a crafted request from a vulnerable web application. SSRF is usually used to target internal systems behind firewalls that are normally inaccessible to an attacker from the external network. Additionally, it’s also possible for an attacker to leverage SSRF to access services from the same server that is listening on the loopback interface (127.0.0.1).

Get Putra Adhari’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Reference : https://www.acunetix.com/blog/articles/server-side-request-forgery-vulnerability/

Regards BugHunter Indonesia , BugBounty ID .

Timeline

Report (16 Des 2018)

Libravatar Appreciate Me (17 Des 2018)

Libravatar ADD me in HOF ( 24 Des 2018 )

touch me to see HOF

Bug Fix and Release

https://bugs.launchpad.net/libravatar/+bug/1808720
