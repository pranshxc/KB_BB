---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-11-16_new-technique-to-find-blind-xss.md
original_filename: 2018-11-16_new-technique-to-find-blind-xss.md
title: New technique to find Blind-XSS
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
raw_sha256: 7fe13b163956f2246820ceb2d06dfb6146423476cdf985f9debceb7e87722a93
text_sha256: 30ada373aaa852ef99d98d4d37bf0760a8ab7e346900b5716efc9b81c89d55bf
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# New technique to find Blind-XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-11-16_new-technique-to-find-blind-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `7fe13b163956f2246820ceb2d06dfb6146423476cdf985f9debceb7e87722a93`
- Text SHA256: `30ada373aaa852ef99d98d4d37bf0760a8ab7e346900b5716efc9b81c89d55bf`


## Content

---
title: "New technique to find Blind-XSS"
url: "https://medium.com/@renwa/new-technique-to-find-blind-xss-c2efcd377cc2"
authors: ["Renwa (@RenwaX23)"]
bugs: ["Blind XSS"]
publication_date: "2018-11-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5579
scraped_via: "browseros"
---

# New technique to find Blind-XSS

New technique to find Blind-XSS
Renwa
Follow
2 min read
·
Nov 16, 2018

335

Blind-XSS is a powerful attack now i will talk about a technique i have used in BB programs, If you are not familiar with Blind-XSS i recommend to read Syntax Error’s post

Most of hunter test for BXSS in (Contact forms-Admin Reviews-Live Chat, …) but do you know how your request is going to be sent to the admin panel? most of them are just a simple email form that will send your info’s to support@domain then admin can review them.

Let’s see a simple contact form

Press enter or click to view image in full size

If you try to inject javascript into subject,name,message in most of cases it won’t be succeed, because it will sanitize user input before sending it to the admin portal. so how to bypass this?

Get Renwa’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Most of website use email service along with their contact form and they will be sent to the same admin portal, for instance we have support@example.com then all we need to do is sending an Email with blind-XSS payloads in (subject, body) of the Email, try to send as much emails you can to different address of the website.

Press enter or click to view image in full size

But they don’t have any emails in their website, they just use contact forms?Try (info, support, contact, sale..) or You can find their contact emails using Hunter.io

./Thanks
