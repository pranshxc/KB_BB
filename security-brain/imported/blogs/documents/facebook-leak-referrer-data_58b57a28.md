---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-08_facebook-leak-referrer-data.md
original_filename: 2020-12-08_facebook-leak-referrer-data.md
title: Facebook leak referrer data
category: documents
detected_topics:
- command-injection
- api-security
tags:
- imported
- documents
- command-injection
- api-security
language: en
raw_sha256: 58b57a2818ee9b4d43dcfac5b494e9f9f995cdfcfba18b2f82f2cc8674c76e64
text_sha256: d951a9a903ddcb3b0a7b184447939cb587246fd1a4b7fcbf3bb50a0bebd8e1a0
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook leak referrer data

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-08_facebook-leak-referrer-data.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `58b57a2818ee9b4d43dcfac5b494e9f9f995cdfcfba18b2f82f2cc8674c76e64`
- Text SHA256: `d951a9a903ddcb3b0a7b184447939cb587246fd1a4b7fcbf3bb50a0bebd8e1a0`


## Content

---
title: "Facebook leak referrer data"
page_title: "Facebook Leak Referrer Data. While finding a facebook vulnerability… | by Neil Mark Ochea / mhl_0xnmo | Medium"
url: "https://nmochea.medium.com/facebook-leak-referrer-data-in-every-sub-domain-48da5e505cf6"
authors: ["Neil Mark Ochea (@nmochea)"]
programs: ["Meta / Facebook"]
bugs: ["Open redirect"]
publication_date: "2020-12-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4081
scraped_via: "browseros"
---

# Facebook leak referrer data

Facebook Leak Referrer Data
Neil Mark Ochea / mhl_0xnmo
Follow
2 min read
·
Dec 8, 2020

56

While finding a facebook vulnerability I visited this interesting link with a back uri parameter endpoint

Press enter or click to view image in full size

So I view the source code and read it. After reading it i found out the url endpoint in the source code does not passing by linkshim, so by adding

Press enter or click to view image in full size

at the endpoint the result like this

Press enter or click to view image in full size

you can easily redirect the facebook page without linkshim the redirect works.

What is Linkshim

Every time a link is clicked on the site, the link will check that the URL against Facebook has its own internal list of malicious links, along with the lists of numerous external partners including McAfee, Google, Web of Trust, and Websense. If Facebook detects that a URL is malicious, Facebook will display an interstitial page before the browser actually requests the suspicious page.

Read the full explanation in this note: www.facebook.com

Setup

User: UserOne {Owner: UserOne }

Environment: owner UserOne

Platform: Facebook sites

Get Neil Mark Ochea / mhl_0xnmo’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Step to Reproduce

From any web browser goto www.facebook.com , login as UserOne.
Open this facebook link
Press enter or click to view image in full size
From the left top header click back button
Then facebook page redirect to without linkshim
Press enter or click to view image in full size
Press enter or click to view image in full size
Disclosure Timeline
October 13, 2020 — I reported this vulnerability issue in facebook whitehat page.
October 13, 2020 — The Facebook team reproduces & investigates regarding the vulnerability issue.
October 16, 2020 — The vulnerability has been patched by adding linkshim.
October 22, 2020 — Bounty Rewarded

Thanks for reading this article, I hope you guys learn something new today. Please share this article to spread the knowledge.

Don’t forget to follow and connect with me through LinkedIn, and Twitter.
