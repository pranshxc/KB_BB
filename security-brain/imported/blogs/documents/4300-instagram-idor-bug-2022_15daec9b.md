---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-02_4300-instagram-idor-bug-2022.md
original_filename: 2022-03-02_4300-instagram-idor-bug-2022.md
title: 4300$ Instagram IDOR Bug (2022)
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
raw_sha256: 15daec9b7c102fd05e1714c05d67c908fa881ebfdeafd686444ff347cd588035
text_sha256: 3e8abbfbd8c604fab366be1bde3eac660ae8429ebdc2a9c3fa048343683cc8d6
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# 4300$ Instagram IDOR Bug (2022)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-02_4300-instagram-idor-bug-2022.md
- Source Type: markdown
- Detected Topics: idor, command-injection, api-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `15daec9b7c102fd05e1714c05d67c908fa881ebfdeafd686444ff347cd588035`
- Text SHA256: `3e8abbfbd8c604fab366be1bde3eac660ae8429ebdc2a9c3fa048343683cc8d6`


## Content

---
title: "4300$ Instagram IDOR Bug (2022)"
page_title: "$4300 Instagram IDOR Bug (2022). Hello everyone! Today im going to… | by Nawaf Alkhaldi | Medium"
url: "https://medium.com/@nvmeeet/4300-instagram-idor-bug-2022-5386cf492cad"
authors: ["Nawaf Alkhaldi (@nvmeeet)"]
programs: ["Meta / Facebook"]
bugs: ["IDOR"]
bounty: "4,300"
publication_date: "2022-03-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2854
scraped_via: "browseros"
---

# 4300$ Instagram IDOR Bug (2022)

$4300 Instagram IDOR Bug (2022)
Nawaf Alkhaldi
Follow
2 min read
·
Mar 3, 2022

849

15

Hello everyone! Today im going to explain how i found a $4300 IDOR Bug on Instagram.

Press enter or click to view image in full size
During my usual hunting routine, I have found a new feature in Instagram called “Interests” this new feature allows you to choose interests and topics you prefer to show up in your feed more often. For example (football, cars, etc..)
After digging into This feature I noticed in the post-data there was the Instagram target user id that belongs to my account, After I saw that I instantly went and changed it to my other account’s id to check for IDOR, and YES.. it worked! IDOR Bug that makes me able to add/modify and even delete any account’s favorite interests/topics.

Report timeline:

Report sent on: November 8th 2021

Get Nawaf Alkhaldi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Bounty awarded: January 28th 2022

Bounty Amount: $4000 + $300 for the delay (69 days)

Pics below:

Press enter or click to view image in full size
original bounty
Press enter or click to view image in full size
bonus for the delay

Thanks for reading!

Don’t forget to leave comment on what you think about this write-up :-)

Good luck with your hunting everyone!
