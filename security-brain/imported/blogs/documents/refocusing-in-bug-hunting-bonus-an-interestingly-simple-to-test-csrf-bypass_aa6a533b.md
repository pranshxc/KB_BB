---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-01_refocusing-in-bug-hunting-bonus-an-interestingly-simple-to-test-csrf-bypass.md
original_filename: 2020-08-01_refocusing-in-bug-hunting-bonus-an-interestingly-simple-to-test-csrf-bypass.md
title: 'Refocusing in bug hunting, Bonus: An interestingly simple to test CSRF bypass'
category: documents
detected_topics:
- idor
- xss
- command-injection
- csrf
- api-security
tags:
- imported
- documents
- idor
- xss
- command-injection
- csrf
- api-security
language: en
raw_sha256: aa6a533b1cd559d24cc228c72941ba729881ac1db71c7e7ec4c9006dac14b327
text_sha256: eaedde3d1818d8d1b53e177bc44ea19c59f6914fac4ee4986e38a3fa6c769bfa
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Refocusing in bug hunting, Bonus: An interestingly simple to test CSRF bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-01_refocusing-in-bug-hunting-bonus-an-interestingly-simple-to-test-csrf-bypass.md
- Source Type: markdown
- Detected Topics: idor, xss, command-injection, csrf, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `aa6a533b1cd559d24cc228c72941ba729881ac1db71c7e7ec4c9006dac14b327`
- Text SHA256: `eaedde3d1818d8d1b53e177bc44ea19c59f6914fac4ee4986e38a3fa6c769bfa`


## Content

---
title: "Refocusing in bug hunting, Bonus: An interestingly simple to test CSRF bypass"
url: "https://medium.com/bugbountywriteup/refocusing-in-bug-hunting-bonus-an-interestingly-simple-to-test-csrf-bypass-8595b3312147"
authors: ["Vuk Ivanovic"]
bugs: ["CSRF"]
publication_date: "2020-08-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4361
scraped_via: "browseros"
---

# Refocusing in bug hunting, Bonus: An interestingly simple to test CSRF bypass

Member-only story

Refocusing in bug hunting, Bonus: An interestingly simple to test CSRF bypass
Vuk Ivanovic
Follow
3 min read
·
Aug 1, 2020

186

Use the source… of a html page

It happens that from time to time you get stuck during bug hunting. You visit the website that is in scope, and you look around it, you check what burp proxy history logs, and there’s nothing there. That is, nothing obvious. And, at times, you may stop there. Especially if you’re early on your journey like I was some time ago.

I went to this website that had the usual suspects like search form, ability to add products to a cart, to your wishlist, and to place the order.

The obvious attack, for a “green” bug hunter, is to throw xss payloads into all the parameters and see what happens. And, in this case, nothing. There was nothing interesting, the html tags were being properly encoded. It looked like a dead end.

Therefore, I left it be for a few months. And, when I came back, instead of using the tool to extract links to js files that the website was using, I actually decided to read through the source code of the main page. It wasn’t like the real deal, just html source code. But, it turned out that a lot of interesting javascript code was right in the midst of all the html stuff.

The interesting part was a section where javascript was being used for POST and GET requests to very interestingly named endpoints. Knowing the basic javascript was more than enough to understand what the code was doing, and how to test for IDOR using those endpoints.
