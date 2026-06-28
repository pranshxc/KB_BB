---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-09_broke-limited-scope-with-a-chain-of-bugs-tips-for-every-rider-cors.md
original_filename: 2020-03-09_broke-limited-scope-with-a-chain-of-bugs-tips-for-every-rider-cors.md
title: Broke limited scope with a chain of bugs (tips for every rider CORS)
category: documents
detected_topics:
- command-injection
- automation-abuse
- cors
tags:
- imported
- documents
- command-injection
- automation-abuse
- cors
language: en
raw_sha256: 9d32571511fba6d39b05a392120b3e2e4af143be10288ce5ce747fd2ccf996d5
text_sha256: 4d1ca2394be68f688f03d7c5a4fd11981a5de0c50a845f6f78aaaddefd93527b
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Broke limited scope with a chain of bugs (tips for every rider CORS)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-09_broke-limited-scope-with-a-chain-of-bugs-tips-for-every-rider-cors.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, cors
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `9d32571511fba6d39b05a392120b3e2e4af143be10288ce5ce747fd2ccf996d5`
- Text SHA256: `4d1ca2394be68f688f03d7c5a4fd11981a5de0c50a845f6f78aaaddefd93527b`


## Content

---
title: "Broke limited scope with a chain of bugs (tips for every rider CORS)"
url: "https://medium.com/bugbountywriteup/broke-limited-scope-with-a-chain-of-bugs-ef734ac430f5"
authors: ["Valeriy Shevchenko (@Krevetk0Valeriy)"]
bugs: ["CORS misconfiguration", "RCE"]
publication_date: "2020-03-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4726
scraped_via: "browseros"
---

# Broke limited scope with a chain of bugs (tips for every rider CORS)

Member-only story

Broke limited scope with a chain of bugs (tips for every rider CORS)
Valeriy Shevchenko
Follow
7 min read
·
Mar 9, 2020

89

One morning, I was asked to participate in a private bug bounty program. In general, my experience in security is based on such private projects. This is good on the one hand, as there is almost no rush to find the most dangerous bug before the others. On the other hand, it’s a bad growth point. The growth point is definitely there, but the growth rate in this situation is quite slow. The person who wrote to me asked for a link to my HackerOne account. I shared the link to my profile. But I was a little embarrassed. My profile at that moment was with zero reputation (5 month ago). Well, it wasn’t. It was a bit negative, as I once tried to contact the company to inform them about the “broken functionality”, but at that time I couldn’t find a better connection than the HackerOne. I reported a problem. But I got a negative reputation score just because the problem was not related to the security area. And I haven’t used this account since that time. At that point, I decided to fix the situation by all means.

It decided to try to rehabilitate myself on several programs. Both programs are private. But it didn’t simplify the situation because people with a famous name in the field of information security had already found a lot of vulnerabilities there before me.
