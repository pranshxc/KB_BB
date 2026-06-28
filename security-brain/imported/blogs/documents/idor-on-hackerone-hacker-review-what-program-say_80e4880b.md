---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-09-02_idor-on-hackerone-hacker-review-what-program-say.md
original_filename: 2017-09-02_idor-on-hackerone-hacker-review-what-program-say.md
title: IDOR on HackerOne Hacker Review “What Program Say”
category: documents
detected_topics:
- idor
- command-injection
- api-security
tags:
- imported
- documents
- idor
- command-injection
- api-security
language: en
raw_sha256: 80e4880b746ddd028955a9c41c68689a6125a662c56587d7208bd1975c54292c
text_sha256: 4ac0576597ed12d4cad8a98d45df490b09e41a3b39a0e976e4a9bde043127a3a
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# IDOR on HackerOne Hacker Review “What Program Say”

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-09-02_idor-on-hackerone-hacker-review-what-program-say.md
- Source Type: markdown
- Detected Topics: idor, command-injection, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `80e4880b746ddd028955a9c41c68689a6125a662c56587d7208bd1975c54292c`
- Text SHA256: `4ac0576597ed12d4cad8a98d45df490b09e41a3b39a0e976e4a9bde043127a3a`


## Content

---
title: "IDOR on HackerOne Hacker Review “What Program Say”"
url: "https://medium.com/japzdivino/idor-on-hackerone-hacker-review-what-program-say-885ce3989a6f"
authors: ["Japz Divino (@japzdivino)"]
programs: ["HackerOne"]
bugs: ["IDOR"]
publication_date: "2017-09-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6110
scraped_via: "browseros"
---

# IDOR on HackerOne Hacker Review “What Program Say”

Member-only story

IDOR on HackerOne Hacker Review “What Program Say”
Japz Divino
Follow
4 min read
·
Sep 2, 2017

96

Severity: Low

Weakness: Insecure Direct Object Reference

Hello everyone, welcome to my first blog, I’m going to share my recent finding on HackerOne’s own bug bounty program.

NOTE: There are two precondition to successfully exploit the bug.

Attacker must be a team member that can review a hacker (hacker program participants)
Victims must be a participant of the program (submitted a report — despite of any status of report, even the report was not yet touched by the sec team, as long as you submitted a report, you are already a participant)

When i am checking on disclosed report in h1 hacktivity, i always visit some of the profile that have a recently disclosed report to see if i can get some idea on their report, but recently i have observed that some of the researchers have a “What Program Say” on their profile, so i think this is a new feature on hackerone, I’ve found it cool and a bit interesting so i try to check if i can find some good fruit on this new feature :) , First thing is how that review posted on hacker profile ?

According to this https://support.hackerone.com/hc/en-us/articles/115003573643-Hacker-Reviews , With Hacker Reviews, HackerOne customers have the option to send comments on hacker…
