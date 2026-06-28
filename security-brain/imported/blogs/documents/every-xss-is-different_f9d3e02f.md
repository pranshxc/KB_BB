---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-20_every-xss-is-different_2.md
original_filename: 2022-06-20_every-xss-is-different_2.md
title: Every XSS is different
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
raw_sha256: f9d3e02f9aa7500333de2330fcb59f9a81c8f80bb65674ddfcda4c2c2bcfd2cc
text_sha256: c23d1f12aa58c70e63db0321ab1fe7d9f5650f28eb261a5d24aa0b9ab9f261e2
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Every XSS is different

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-20_every-xss-is-different_2.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `f9d3e02f9aa7500333de2330fcb59f9a81c8f80bb65674ddfcda4c2c2bcfd2cc`
- Text SHA256: `c23d1f12aa58c70e63db0321ab1fe7d9f5650f28eb261a5d24aa0b9ab9f261e2`


## Content

---
title: "Every XSS is different"
url: "https://medium.com/@leomsec/every-xss-is-different-c98528fee5e0"
authors: ["Leonardo"]
bugs: ["XSS"]
publication_date: "2022-06-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2534
scraped_via: "browseros"
---

# Every XSS is different

Every XSS is different
Leonardo
Follow
2 min read
·
Jun 20, 2022

21

1

Today I’m going to talk about an XSS that I found on a public bug-bounty program about a year ago, this program has multiple websites and from different countries (Brazil, France, Spain, and others), I actually reported 4 different vulnerabilities for them, but let’s just focus on this particular XSS.

First I started looking on google for a site:*.[company domain].* (if you don’t know what it does search for ‘google hacking’) so I could get all or almost all the domains/subdomains from the company, I looked at some sites but this one got my attention because it was different from all the others websites this company has.

Get Leonardo’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This particular website didn’t have a lot of things to do but it had a search bar, so obviously I saw it as a possibility for XSS, the value was reflected inside an input tag as value so I tested inserting a double quote to see if any filter was applied to it and it got encoded, so I tried sending it URL encoded and for my surprise it was enough to bypass, at this point I thought “hmm easy xss here” so I used the classic payload “><script>alert(0)</script> and….. The site returned a 403 page… Well, not so easy I guess…

After that I tried to understand at what point of the payload the site would see it as malicious and return a page with 403 code, it was at the very beginning of the code, just the “>< would be considered as malicious, I tried to bypass it by encoding in different ways but it didn’t seem to work, so it’s time to try a different payload, I decided to test the focus and autofocus HTML attributes, so I tested the payload “ onfocus=confirm(document.domain) autofocus and again got the 403 page, here I go again try to understand the filter that was applied here, after some tests I noticed that anything like <space>on<any word>=<any word> was returning the 403 page, after a while testing different encodings I noticed that when you had a character with double url encoding it would just disappear, I decided to test if it was possible to use this to evade the filter and it worked, I just added a plus sign double url encoded (%252b) between the quote and the onfocus and the site didn’t see it as a malicious payload anymore so the xss was triggered for me, but……

the saga of this xss does not end here. Basically, when I typed the xss directly in the search bar, it was getting triggered, but when I copied the url and sent it to someone and the person clicked the link, it would just not work, then I used the great power of a tool that we all hackers have that’s called ‘what if’ and I asked myself “what if I try to use some url shortener”, and yes, it finally worked \o/

I hope you enjoyed reading it and learnt something :D
