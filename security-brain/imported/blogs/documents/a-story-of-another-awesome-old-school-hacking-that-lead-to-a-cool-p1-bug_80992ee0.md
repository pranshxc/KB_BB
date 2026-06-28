---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-22_a-story-of-another-awesome-old-school-hacking-that-lead-to-a-cool-p1-bug.md
original_filename: 2021-10-22_a-story-of-another-awesome-old-school-hacking-that-lead-to-a-cool-p1-bug.md
title: A story of another awesome old school hacking that lead to a cool P1 bug
category: documents
detected_topics:
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 80992ee073282e6680562ffd2c0a23d222dbb9c5ffafafc74ce35260c5dc858d
text_sha256: 33773cb29862cc80c67c7246282eb9e3447f8b16a1b47adaa8ffef287a2f456d
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# A story of another awesome old school hacking that lead to a cool P1 bug

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-22_a-story-of-another-awesome-old-school-hacking-that-lead-to-a-cool-p1-bug.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `80992ee073282e6680562ffd2c0a23d222dbb9c5ffafafc74ce35260c5dc858d`
- Text SHA256: `33773cb29862cc80c67c7246282eb9e3447f8b16a1b47adaa8ffef287a2f456d`


## Content

---
title: "A story of another awesome old school hacking that lead to a cool P1 bug"
url: "https://infosecwriteups.com/a-story-of-another-awesome-old-school-hacking-that-lead-to-a-cool-p1-bug-f88da04b1ecf"
authors: ["Vuk Ivanovic"]
bugs: ["403 bypass"]
publication_date: "2021-10-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3224
scraped_via: "browseros"
---

# A story of another awesome old school hacking that lead to a cool P1 bug

Member-only story

A story of another awesome old school hacking that lead to a cool P1 bug
or how Response 200 OK w/ size 0 doesn’t always mean 0
Vuk Ivanovic
Follow
2 min read
·
Oct 22, 2021

100

There are times when things don’t align all that well. Like finding some subdomain that has 403 and running all the wordlists against it doesn’t amount to anything, and only interesting thing is some random endpoint that is size 0. Sure, you ought to try POST request against it because maybe there’s something there, or messing around with headers and so on. But when that doesn’t work, what then? Well, if the stars align a bit better, while the response size 0 still presents that there’s nothing in the body of that page, the Response headers like Server and X-Powered-By may lead to quite a lot.

On to the hack — Part 1

While it’s very nifty to use various tools to determine what the target is running, there’s nothing like manually checking out the target’s responses to your requests. The best way to go about it has always been burp. Be it free or paid version, both offer the essential — being able to see entire Response output with all the headers that the target is configured to disclose. The same can be achieved in other ways, but burp offers most readable format, imho.

And so it happened that I found a random directory which ffuf marked as 200 OK and size 0, but because I wanted to mess around with headers as per my other articles:
