---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-28_stored-xss-in-microsoft-outlook.md
original_filename: 2020-05-28_stored-xss-in-microsoft-outlook.md
title: Stored XSS in Microsoft outlook
category: documents
detected_topics:
- xss
- command-injection
- mobile-security
tags:
- imported
- documents
- xss
- command-injection
- mobile-security
language: en
raw_sha256: 50028f5941561ccad33b89b266baf6494a16f314138c465e188e603dc0a19c24
text_sha256: fefd1a397b6fdf106ad23f9106b090c123328653b5c17c53dde7a8f0dc7ba9c8
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Stored XSS in Microsoft outlook

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-28_stored-xss-in-microsoft-outlook.md
- Source Type: markdown
- Detected Topics: xss, command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `50028f5941561ccad33b89b266baf6494a16f314138c465e188e603dc0a19c24`
- Text SHA256: `fefd1a397b6fdf106ad23f9106b090c123328653b5c17c53dde7a8f0dc7ba9c8`


## Content

---
title: "Stored XSS in Microsoft outlook"
url: "https://medium.com/@kminthein/stored-xss-in-microsoft-outlook-ebce9ff9e45b"
authors: ["kminthein / weev3 (@kyawminthein99)"]
programs: ["Microsoft"]
bugs: ["Stored XSS"]
publication_date: "2020-05-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4558
scraped_via: "browseros"
---

# Stored XSS in Microsoft outlook

Stored XSS in Microsoft outlook
kminthein
Follow
1 min read
·
May 28, 2020

10

Copy from one of my 2018 blog post.

I want share about my finding in Microsoft outlook IOS application that could affect 2.62.0 and below. I’m not bounty hunter and i really don’t want to become. When I have free time, i choose random websites or apps. Two months ago, i upload a file via Microsoft out using web based application with extension name….

'"><img src=x onerror="alert(window.clientInformation.appVersion);">.jpg

Nothing happened in their core website and i think “Wait what if vulnerable to XSS in ios app?” and then i opened this message via ios app and the result is

Press enter or click to view image in full size

I speak myself “OMG!!”. The problem is that they missed to standardize in IOS side. Yes, they do properly in outlook.live.com. So this vulnerability becomes Stored(blind) XSS.

Get kminthein’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I reported to Microsoft MSRC and they placed my name in their security researcher list, lol i don’t think myself as security researcher.

https://technet.microsoft.com/en-us/security/cc308589.aspx

Thanks everyone who read this write-up.
