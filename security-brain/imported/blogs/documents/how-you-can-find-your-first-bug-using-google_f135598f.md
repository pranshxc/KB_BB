---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-07_how-you-can-find-your-first-bug-using-google.md
original_filename: 2022-12-07_how-you-can-find-your-first-bug-using-google.md
title: How you can find your first bug using google
category: documents
detected_topics:
- ssrf
- xss
- command-injection
- csrf
- information-disclosure
tags:
- imported
- documents
- ssrf
- xss
- command-injection
- csrf
- information-disclosure
language: en
raw_sha256: f135598ffd1f88466a64ce95b41d6b508dfb371afa76f36199086bb0ebe7628c
text_sha256: a268601c439b635123e81bee924fdbd6ef4c8275b1008fe9ef7d93a9c5484615
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# How you can find your first bug using google

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-07_how-you-can-find-your-first-bug-using-google.md
- Source Type: markdown
- Detected Topics: ssrf, xss, command-injection, csrf, information-disclosure
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `f135598ffd1f88466a64ce95b41d6b508dfb371afa76f36199086bb0ebe7628c`
- Text SHA256: `a268601c439b635123e81bee924fdbd6ef4c8275b1008fe9ef7d93a9c5484615`


## Content

---
title: "How you can find your first bug using google"
url: "https://medium.com/@shellyshubh/how-you-can-find-your-first-bug-using-google-c9327f82632e"
authors: ["shbugger1"]
bugs: ["Information disclosure"]
publication_date: "2022-12-07"
added_date: "2022-12-09"
source: "pentester.land/writeups.json"
original_index: 1807
scraped_via: "browseros"
---

# How you can find your first bug using google

Top highlight

How you can find your first bug using google
shbugger1
Follow
2 min read
·
Dec 7, 2022

110

3

If you are a bug bounty hunter, you are already familiar with bugs like XSS, CSRF, SSRF etc, but as a beginner, they are usually hard to find and you get easily demotivated when you are unable to find these. In my opinion Information Disclosure is one of the most underrated bugs which is pretty easy to find even for beginners.

As a beginner myself, I started hunting for Information Disclosure through google dorks and so far I have found a ton of juicy information about targets.

Get shbugger1’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The dork I have used the most is

site:target.com ext:pdf intext:confidential

I have found nearly 6 bugs in programs including 3 fortune 500 companies. The severity of the bug itself is low but if you manage to find a really private information you can even go to p2 or p1

The best I was able to find was a bank confirmation letter of a really big company which disclosed

Account Name:
Account Number: 
Account Currency: 
Account Type:
Beneficiary Bank Swift Code: 
Beneficiary Bank Address:

One thing you shold always keep in mind is that before submitting your report, make sure it does make an impact. Sometimes you will find documents with “Confidential Information” but it doesnt really have an impact on disclosure.

Thanks for reading.
