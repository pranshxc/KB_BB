---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-11-22_how-i-found-information-disclosure-on-scribdcom.md
original_filename: 2018-11-22_how-i-found-information-disclosure-on-scribdcom.md
title: How i Found Information Disclosure on Scribd.com
category: documents
detected_topics:
- command-injection
- csrf
- information-disclosure
tags:
- imported
- documents
- command-injection
- csrf
- information-disclosure
language: en
raw_sha256: 38765446fc9b413078529f2c60a34b1734f815518bfa7376f695bc48237d249e
text_sha256: 801da68783e700ac71e0f9e17caf248dc8fb9666d6129e0285a166bbdf9423db
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# How i Found Information Disclosure on Scribd.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-11-22_how-i-found-information-disclosure-on-scribdcom.md
- Source Type: markdown
- Detected Topics: command-injection, csrf, information-disclosure
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `38765446fc9b413078529f2c60a34b1734f815518bfa7376f695bc48237d249e`
- Text SHA256: `801da68783e700ac71e0f9e17caf248dc8fb9666d6129e0285a166bbdf9423db`


## Content

---
title: "How i Found Information Disclosure on Scribd.com"
url: "https://medium.com/@androgaming1912/how-i-found-password-bypass-vulnerability-on-private-document-at-scribd-com-c0905e8dcc9a"
authors: ["Zerb0a"]
programs: ["Scribd.com"]
bugs: ["CSRF"]
publication_date: "2018-11-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5571
scraped_via: "browseros"
---

# How i Found Information Disclosure on Scribd.com

How i Found Information Disclosure on Scribd.com
zer
Follow
2 min read
·
Nov 22, 2018

25

1

hi, this is my first write up on medium.com.
11 days ago i found a vulnerability on scribd.com when i finding an answer of my homework ( I was lazy at that time).

then I made a document and made the document private

In my heart I thought that the download button made me curious, so I decided to intercept before pressing the download button. and I found a Request with the POST method in the url: https://www.scribd.com/document_downloads/request_document_for_download

Then I will make a document and give a password (make private) the document and try to get access from another account. After that I created a new account and made a CSRF whose contents were more or less like this:

<html>

<title> Scribd VUlnerability </ title>

<body>

<form action = “https://www.scribd.com/document_downloads/request_document_for_download" method = “POST”>

<input type = “hidden” name = “id” value = “(ID FILE)” />

Get zer’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

<input type = “submit” value = “Submit request” />

</ form>

</ body>

</ html>.

and try to do pentesting.

Bingo! after that I managed to get the password to see the private document. After that I asked whether there was a bug bounty program or not to the IT security scribd. after 11 days (When I wrote this) I immediately reported this bug to the Scribd team so that it could be fixed.

Full Video PoC on my Blog :
https://raflipasya19.blogspot.co.id
My Youtube Channel :
T-GOX Channel

Status:

19 November 2018 16:59 PM = Reported To Scribd Security Team
20 November 2018 01:58 AM = Their team Review my report
No response after 4 Days, so i decided to Write Up this issue
