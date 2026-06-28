---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-03_a-short-story-of-content-spoofing-to-html-injection-in-apple-using-dangling-mark.md
original_filename: 2021-10-03_a-short-story-of-content-spoofing-to-html-injection-in-apple-using-dangling-mark.md
title: A short story of Content Spoofing to HTML Injection in Apple using Dangling
  Markup Injection
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
raw_sha256: 4f091e1a985af6d2996db43b7f3ce5cea6aff64404018f056e3e1f80466e21f7
text_sha256: ab4eeec92450e1031976c363b3b1dbe169d350f9905d19d538ee7b606647fa11
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# A short story of Content Spoofing to HTML Injection in Apple using Dangling Markup Injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-03_a-short-story-of-content-spoofing-to-html-injection-in-apple-using-dangling-mark.md
- Source Type: markdown
- Detected Topics: xss, command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `4f091e1a985af6d2996db43b7f3ce5cea6aff64404018f056e3e1f80466e21f7`
- Text SHA256: `ab4eeec92450e1031976c363b3b1dbe169d350f9905d19d538ee7b606647fa11`


## Content

---
title: "A short story of Content Spoofing to HTML Injection in Apple using Dangling Markup Injection"
page_title: "Content Spoofing to HTML Injection in Apple | InfoSec Write-ups"
url: "https://rishuranjanofficial.medium.com/html-injection-in-itunesconnect-apple-com-3f8a898f21ee"
authors: ["Rishu Ranjan (@tweetit_rrj)"]
programs: ["Apple"]
bugs: ["HTML injection", "Dangling Markup Injection"]
publication_date: "2021-10-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3266
scraped_via: "browseros"
---

# A short story of Content Spoofing to HTML Injection in Apple using Dangling Markup Injection

Member-only story

A short story of Content Spoofing to HTML Injection in Apple using Dangling Markup Injection
Rishu Ranjan
Follow
3 min read
·
Oct 3, 2021

127

1

Content Spoofing is an injection in which user input is reflected as it is in the application response which can be used in phishing attacks.

During the recon phase, I found itunesconnect.apple.com, a subdomain of apple and after digging into it, I had observed that the content of the error key parameter was reflecting back to the page as shown below

Payload - https://itunesconnect.apple.com/login?errorKey=This%20message%20can%20be%20changed%20by%20attacker.%20This%20is%20content%20spoofing%20till%20now.%20Let%20try%20to%20exploit%20it%20further.

Press enter or click to view image in full size
Content Spoofing till here

With normal inline Cross-Site Scripting(XSS) payloads, the application was giving a blank pop-up. After trying different scenarios, I have observed that dangling markup injection is possible on the vulnerable parameters (errorKey)

Let’s understand the concept of Dangling Markup Injection

Dangling markup injection is very useful where we can’t find a way to execute our JavaScript due to input filters, content security policy, or other obstacles payloads but we can inject some HTML tags. It is used to steal the contents of the page without script by using resources such as images to send the data to a remote location that an attacker controls.
