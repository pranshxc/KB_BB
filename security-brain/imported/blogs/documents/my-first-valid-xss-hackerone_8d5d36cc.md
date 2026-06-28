---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-08-25_my-first-valid-xsshackerone.md
original_filename: 2018-08-25_my-first-valid-xsshackerone.md
title: My first valid xss(@Hackerone)
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: 8d5d36cc277061792d9992c64d07426643204cf01542fd21b6905c0721bd458e
text_sha256: d197ddea2d29abd65d26643d9cc8e58dfd08b58104dea830b506ca6c5a2bfa54
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# My first valid xss(@Hackerone)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-08-25_my-first-valid-xsshackerone.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `8d5d36cc277061792d9992c64d07426643204cf01542fd21b6905c0721bd458e`
- Text SHA256: `d197ddea2d29abd65d26643d9cc8e58dfd08b58104dea830b506ca6c5a2bfa54`


## Content

---
title: "My first valid xss(@Hackerone)"
url: "https://medium.com/@nandwanajatin25/my-first-valid-xss-hackerone-f8ba0a7c647"
authors: ["Jatin Aesthetic (@techyfreakk)"]
bugs: ["XSS"]
bounty: "100"
publication_date: "2018-08-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5738
scraped_via: "browseros"
---

# My first valid xss(@Hackerone)

My first valid xss(@Hackerone)
Jatin Nandwana
Follow
2 min read
·
Aug 25, 2018

138

1

Hey today I will share my first ever valid xss bug which was a reflected xss on a public program on hackerone.

So lets start, I was very new to hackerone and I took a random program to start and I started to do some recon by finding the subdomains and different endpoints.When I was looking at different pages inside the website and then I found an endpoint like this:

https://example.com/abc/]

I thought there is something fishy here and I opened that page but the page loaded normally.Then I looked at the source of the page and at last of the source I founded a commented out string containing the path after the domain.

So I tried entering something else in the url path and it displayed as it is in that comment.So I tried closing that comment with a closing comment tag

Get Jatin Nandwana’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

— —><test> and I was successful in closing that comment tag and was successful in inserting other tags so I insert a script tag after that so the final payload become

https://example.com/abc/]--><script>alert(1)</script>

and boom! xss executed!

So in this way I was able to execute xss on that page.Later I realised that this was on every page of that domain and every path of that particular domain had a commented out string containing whatever in the url path was, so xss was executing on every page of that domain.

Reported : 26/05/2018

Bounty : $100

Thanks for reading! I will post my more interesting findings here.
