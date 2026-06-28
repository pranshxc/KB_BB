---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-01-06_reflected-xss-on-asus.md
original_filename: 2019-01-06_reflected-xss-on-asus.md
title: Reflected XSS ON ASUS.
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
raw_sha256: 87eaa7220665cae3c41cef53937350308c956034a9b21820b07badbb8946a866
text_sha256: 9aa4dc8698a16894f9c1555f8d7300181b1a5d1e4ff26030c9e8016556e3260b
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Reflected XSS ON ASUS.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-01-06_reflected-xss-on-asus.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `87eaa7220665cae3c41cef53937350308c956034a9b21820b07badbb8946a866`
- Text SHA256: `9aa4dc8698a16894f9c1555f8d7300181b1a5d1e4ff26030c9e8016556e3260b`


## Content

---
title: "Reflected XSS ON ASUS."
url: "https://medium.com/@thejuskrishnan911/reflected-xss-on-asus-568ce0541171"
authors: ["Thejus Krishnan"]
programs: ["Asus"]
bugs: ["Reflected XSS"]
publication_date: "2019-01-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5484
scraped_via: "browseros"
---

# Reflected XSS ON ASUS.

Top highlight

Reflected XSS ON ASUS.
Thejus Krishnan
Follow
1 min read
·
Jan 6, 2019

128

Hy this is Thejus Krishnan, This article on my recent finding of ASUS Web Application Vulnerability which was affected by cross Site Scripting.

Press enter or click to view image in full size

When i was searching for an Asus product, i accidentally found out a sub domain https://press.asus.com.

Url : https://press.asus.com/search?search=, Here i tried XSS.

When i submitted the payload “dvs9c”><script>alert(‘hello’)</script>jnyf0" in the search parameter. BOOM..! i got XSS.

Get Thejus Krishnan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Vulnerable url : https://press.asus.com/search.php?search=Triodvs9c"><script>alert(“hello”)</script>jnyf0

Press enter or click to view image in full size

Few Weeks after reporting this issue to Asus Security Team. I got a replay from Asus Team that the issue has been resolved.

Thanks for reading.

Timeline :
DEC 15 Reported the issue.
DEC 17 Responded
DEC 22 Fixed and HOF approved
DEC 28 Listed in HOF
