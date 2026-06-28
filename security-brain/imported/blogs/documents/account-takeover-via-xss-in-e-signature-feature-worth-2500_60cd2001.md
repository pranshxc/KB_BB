---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-08_account-takeover-via-xss-in-e-signature-feature-worth-2500.md
original_filename: 2021-09-08_account-takeover-via-xss-in-e-signature-feature-worth-2500.md
title: Account Takeover via XSS in e-signature feature worth 2500$
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
raw_sha256: 60cd2001830e1c9ed9382b1c3538a6c1c8b997640d4ba44096bbf83b0664e633
text_sha256: 4aacd2c9115b53f4e5c38bd2b4ed7a49cf15a00a78bb5b455e6636b5125add39
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Account Takeover via XSS in e-signature feature worth 2500$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-08_account-takeover-via-xss-in-e-signature-feature-worth-2500.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `60cd2001830e1c9ed9382b1c3538a6c1c8b997640d4ba44096bbf83b0664e633`
- Text SHA256: `4aacd2c9115b53f4e5c38bd2b4ed7a49cf15a00a78bb5b455e6636b5125add39`


## Content

---
title: "Account Takeover via XSS in e-signature feature worth 2500$"
url: "https://medium.com/@gguzelkokar.mdbf15/xss-via-account-takeover-in-e-signature-feature-worth-2500-435f3f8325bf"
authors: ["Gökhan Güzelkokar (@gkhck_)"]
bugs: ["XSS", "Account takeover"]
bounty: "2,500"
publication_date: "2021-09-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3333
scraped_via: "browseros"
---

# Account Takeover via XSS in e-signature feature worth 2500$

Member-only story

Account Takeover via XSS in e-signature feature worth 2500$
Gökhan Güzelkokar
Follow
2 min read
·
Sep 7, 2021

385

Hi everyone, I hope all is well. I was hacking an HR application and started testing the integrated applications that were on it. My target was HR application but I wanted to try something on this app. I didn’t even know they were bug bounty program. Just for fun. Damn I really like this. One of the integrated application which I started to test had an electronic signature feature. You prepare a pdf document and send it to someone else to sign.

Press enter or click to view image in full size

When I tried xss payload with in name field, like “><img onerror=alert(document.domain) src> everything was oky. The output was:

&quot;&gt;&lt;img onerror=alert(document.domain) src&gt;

Then I realized that this isn’t my xss payload that I always use 😇 Are you ready to this payload? That was :

“><<img onerror=alert(document.cookie) src>

Yes, just one more ‘<’. I got an alert in the admin page from an unauthenticated user. Output was:

&quot;&gt;<img onerror=alert(document.cookie) src>

I needed to research this, but I didn’t have much time in those days. I found this bug 8 months ago. I’m sorry for not being able to detail.

Sometimes filters can be skipped as simple as that. Developers can sometimes make far worse mistakes. We…
