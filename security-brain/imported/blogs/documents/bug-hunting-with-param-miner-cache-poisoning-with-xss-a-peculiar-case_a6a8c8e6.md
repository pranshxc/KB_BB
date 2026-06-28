---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-08_bug-hunting-with-param-miner-cache-poisoning-with-xss-a-peculiar-case.md
original_filename: 2020-08-08_bug-hunting-with-param-miner-cache-poisoning-with-xss-a-peculiar-case.md
title: 'Bug Hunting with Param Miner: Cache poisoning with XSS, a peculiar case'
category: documents
detected_topics:
- sso
- xss
- command-injection
tags:
- imported
- documents
- sso
- xss
- command-injection
language: en
raw_sha256: a6a8c8e616804e36ab41366087e1edfb528328f38e0a6e7e1f755e5f26dae147
text_sha256: 2296658d4cf44cc6515a1419f03340e6e77b16f8452aa53ea5080014e9646208
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Bug Hunting with Param Miner: Cache poisoning with XSS, a peculiar case

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-08_bug-hunting-with-param-miner-cache-poisoning-with-xss-a-peculiar-case.md
- Source Type: markdown
- Detected Topics: sso, xss, command-injection
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `a6a8c8e616804e36ab41366087e1edfb528328f38e0a6e7e1f755e5f26dae147`
- Text SHA256: `2296658d4cf44cc6515a1419f03340e6e77b16f8452aa53ea5080014e9646208`


## Content

---
title: "Bug Hunting with Param Miner: Cache poisoning with XSS, a peculiar case"
url: "https://medium.com/bugbountywriteup/cache-poisoning-with-xss-a-peculiar-case-eb5973850814"
authors: ["Vuk Ivanovic"]
bugs: ["XSS", "Web cache poisoning"]
publication_date: "2020-08-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4341
scraped_via: "browseros"
---

# Bug Hunting with Param Miner: Cache poisoning with XSS, a peculiar case

Member-only story

Bug Hunting with Param Miner: Cache poisoning with XSS, a peculiar case
Vuk Ivanovic
Follow
4 min read
·
Aug 8, 2020

345

2

Press enter or click to view image in full size

You have heard of the cache poisoning, a bug that had existed for far longer than most of people have been aware, as in many other cases of this nature, in my opinion. But, this article isn’t about a history lesson; however, there are a couple of lessons, maybe more, that you might find useful.

Param Miner with an Edge:

See what I did there? Never mind, it will make itself known soon enough.

Here’s the real world example. Of course I can’t disclose the bbp in question, but the details of the attack won’t make it necessary to do so.

I use Param Miner, an extension for burp pro (technically, it also works in burp community edition, but with a lot of limitations). And, aside from testing for hidden parameters, it also tests for cache poisoning, and then there’s burp pro with its scanner which tests for xss. Add them together and you can get yourself some nice bounties. But, it still requires some legwork.

Doesn’t your heart simply swell up by an increase in adrenaline production upon seeing this, or maybe it flutters, or it starts beating stronger. Either way, it means a good news. It did for me. Upon the initial (with hands shaking) review, it turned out that it wasn’t a false positive. Param miner had discovered a hidden…
