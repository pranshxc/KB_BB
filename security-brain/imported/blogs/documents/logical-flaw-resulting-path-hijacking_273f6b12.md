---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-16_logical-flaw-resulting-path-hijacking.md
original_filename: 2021-07-16_logical-flaw-resulting-path-hijacking.md
title: Logical Flaw Resulting Path Hijacking
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 273f6b1293e2db0ba3637f3b1a8c6093a6b61e98bdd056268e970abf8ae952dc
text_sha256: f93df8ceb7e28e552bd5bd16dfa432f65f53d6540b03c3d8a1657c8cff6806d3
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Logical Flaw Resulting Path Hijacking

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-16_logical-flaw-resulting-path-hijacking.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `273f6b1293e2db0ba3637f3b1a8c6093a6b61e98bdd056268e970abf8ae952dc`
- Text SHA256: `f93df8ceb7e28e552bd5bd16dfa432f65f53d6540b03c3d8a1657c8cff6806d3`


## Content

---
title: "Logical Flaw Resulting Path Hijacking"
url: "https://infosecwriteups.com/logical-flaw-resulting-path-hijacking-dd4d1e1e832f"
authors: ["Veshraj Ghimire (@GhimireVeshraj)"]
bugs: ["Namespace attack"]
publication_date: "2021-07-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3502
scraped_via: "browseros"
---

# Logical Flaw Resulting Path Hijacking

Logical Flaw Resulting Path Hijacking
Veshraj Ghimire
Follow
2 min read
·
Jul 16, 2021

415

4

Hello, amazing people! I hope you are doing well. I am back with my new write-up. In this write-up, I will explain a logical flaw that I found on one target resulting in the hijacking of the path. So let me explain it in short.

While testing on redracted.com, I found that it was not checking and verifying the username eligibility properly. Someone could signup using any existing pathname and takeover the path result, resulting in the overwrite of the path when visited.

How Did I found it?

I signed up with the username “index.php,” then visited my profile and noticed that upon visiting retracted.com/index.php, my profile was popping up. Then I quickly notified them with my index.php username account as POC. The next day, they approved and acknowledged me.

Press enter or click to view image in full size

What is the Impact?

Get Veshraj Ghimire’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The Impact of this bug can be pretty high, can cause bad actors to simply signup using usernames such as signup.php, signin.php, and many similar usernames and can take over the path which might cause a big issue to the organization by making those signup, signing pages unavailable.

Take-Aways:

Try to signup using general path names such as index.php, signup.php, signin.php, and check if visiting those paths shows your profile. If it does, it may be vulnerable.

You can find me here if you wish to connect with me.

Good Bye Till Next Writeup, May luck favors you. Keep hacking. Stay safe!!
