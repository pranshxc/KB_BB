---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-18_how-could-i-tag-photo-to-any-users-scrapbook-on-facebook.md
original_filename: 2020-08-18_how-could-i-tag-photo-to-any-users-scrapbook-on-facebook.md
title: How could I Tag Photo to any user’s Scrapbook on Facebook
category: documents
detected_topics:
- idor
- access-control
- command-injection
tags:
- imported
- documents
- idor
- access-control
- command-injection
language: en
raw_sha256: dc13d89e29421e29df182002e15ede59861fa8e5beaaa53f89bbd5a4ef8c5b52
text_sha256: d4417252f2961652d88e1ce7431987b21c6c4480463024bb57813e1ec6fa5fc0
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# How could I Tag Photo to any user’s Scrapbook on Facebook

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-18_how-could-i-tag-photo-to-any-users-scrapbook-on-facebook.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `dc13d89e29421e29df182002e15ede59861fa8e5beaaa53f89bbd5a4ef8c5b52`
- Text SHA256: `d4417252f2961652d88e1ce7431987b21c6c4480463024bb57813e1ec6fa5fc0`


## Content

---
title: "How could I Tag Photo to any user’s Scrapbook on Facebook"
url: "https://medium.com/bugbountywriteup/how-could-i-tag-photo-to-any-users-scrapbook-on-facebook-23ab15e6e4b4"
authors: ["Raja Sudhakar (@Rajasudhakar)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization"]
publication_date: "2020-08-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4309
scraped_via: "browseros"
---

# How could I Tag Photo to any user’s Scrapbook on Facebook

How could I Tag Photo to any user’s Scrapbook on Facebook
Raja Sudhakar
Follow
2 min read
·
Aug 18, 2020

107

2

Press enter or click to view image in full size

Summary:

This blog post is about an Insecure direct object reference vulnerability in Facebook Scrapbook. In Facebook Scrapbook only Owner and their Partner will be able to tag scrapbook in photos. vulnerability is any users can tag other user’s scrapbook in photos.

Vulnerability Type :

IDOR (Insecure Direct Object References)

Reference: https://www.owasp.org/index.php/Top_10_2010-A4-Insecure_Direct_Object_References

Get Raja Sudhakar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Steps to reproduce:

Open Facebook Profile and Create any Post with photo.
Now visit any User’s Scrapbook Album.
Right Click in User’s Scrapbook album and copy Scrapbook ID.
Now Visit your Post you created and open photo.
Now Click photo and Click Tag photo option choose any user to tag.
Now before tagging make sure Burp Suite’s Interceptor is turned on to capture the request.
Click on “Choose user” now, you will see below kind of request in Burp suite:
POST /ajax/photo_tagging_ajax.php?av=100022637353520HTTP/1.1
Host: www.facebook.comConnection: closeContent-Length: 668Origin: https://www.facebook.comUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0)fbid=XXX&id=USERID&subject=XXXX&name=XXXX&action=add&etc

8. Now change the subject parameter value to victim’s scrapbook ID and Forward the request.

9.Done.

Timeline:

February 25, 2020 — Initial Report

March 03, 2020 — Report Triaged

May 01, 2020 — Vulnerability Fixed By Facebook

May 01, 2020 — Fixed Confirmed

May 01, 2020 — Bounty awarded by Facebook
