---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-28_bug-html-injection-on-tokopedia-.md
original_filename: 2020-07-28_bug-html-injection-on-tokopedia-.md
title: Bug HTML Injection On Tokopedia !
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
raw_sha256: ab7081801fcf40b2d03cdadcdd6da732d93efe98df570bb31148b7a19e64dc72
text_sha256: edbbcaef6b046fad44d6970d02104437d249221f3a52dfb744e1bc915f414eeb
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Bug HTML Injection On Tokopedia !

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-28_bug-html-injection-on-tokopedia-.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `ab7081801fcf40b2d03cdadcdd6da732d93efe98df570bb31148b7a19e64dc72`
- Text SHA256: `edbbcaef6b046fad44d6970d02104437d249221f3a52dfb744e1bc915f414eeb`


## Content

---
title: "Bug HTML Injection On Tokopedia !"
url: "https://medium.com/@jjowi/bug-html-injection-on-tokopedia-9a9b0534ceaa"
authors: ["jowi"]
programs: ["Tokopedia"]
bugs: ["HTML injection"]
publication_date: "2020-07-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4379
scraped_via: "browseros"
---

# Bug HTML Injection On Tokopedia !

Bug HTML Injection On Tokopedia !
jowi
Follow
2 min read
·
Jul 28, 2020

14

1

TOKOPEDIA

Hello Everyone ! Here’s is my write-up BUG “HTML INJECTION” On Tokopedia

What is HTML Injection?

Hypertext Markup Language (HTML) injection is a technique used to take advantage of non-validated input to modify a web page presented by a web application to its users. Attackers take advantage of the fact that the content of a web page is often related to a previous interaction with users.

Get jowi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Sc : https://www.imperva.com/learn/application-security/html-injection/

I’m Input Payload Html Injection Via JSON Voucher Tokopedia

Proof of Concept :
Login Account in Application Tokopedia
Open Chat , And Select Victim
Click “+” And Select Voucher
Click Random Voucher, And Open Burp Suite
Voucher

5. Send Voucher And Change Request With Payload HTML Injection

Press enter or click to view image in full size
Request Voucher Input Payload HTML Injection
Press enter or click to view image in full size
HTML Injection
Remediation:
Your script should filter metacharacters from user input.
Timeline :

Report BUG : 24 May 2020

Tokopedia Respon Bug Valid (MEDIUM) : 26 May 2020

Bug Fixed : 03 June 2020

Tokopedia Send Reward ($xxx) : 12 July 2020

Thanks for reading . Happy Hunting .
