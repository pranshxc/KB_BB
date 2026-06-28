---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-24_how-i-hacked-the-dutch-government-with-sqli-and-won-the-famous-t-shirt.md
original_filename: 2022-02-24_how-i-hacked-the-dutch-government-with-sqli-and-won-the-famous-t-shirt.md
title: How I Hacked the Dutch Government with SQLi and Won the Famous T-Shirt?
category: documents
detected_topics:
- sqli
- command-injection
tags:
- imported
- documents
- sqli
- command-injection
language: en
raw_sha256: 202c10529ce1f8d6963b3ba9be65b31f83d0691af4eb6d6e322b6d01715e7b4d
text_sha256: c8fcc50bbd21f70c911577d3ba234ff85ef2e030326f8a690115f6d23b69004c
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# How I Hacked the Dutch Government with SQLi and Won the Famous T-Shirt?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-24_how-i-hacked-the-dutch-government-with-sqli-and-won-the-famous-t-shirt.md
- Source Type: markdown
- Detected Topics: sqli, command-injection
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `202c10529ce1f8d6963b3ba9be65b31f83d0691af4eb6d6e322b6d01715e7b4d`
- Text SHA256: `c8fcc50bbd21f70c911577d3ba234ff85ef2e030326f8a690115f6d23b69004c`


## Content

---
title: "How I Hacked the Dutch Government with SQLi and Won the Famous T-Shirt?"
url: "https://goktugkaya.medium.com/how-i-hacked-the-dutch-government-and-won-the-famous-t-shirt-b45cdf5dfaa1"
authors: ["Göktuğ Kaya (@g0ktugkaya)"]
programs: ["Dutch Government"]
bugs: ["SQL injection"]
publication_date: "2022-02-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2873
scraped_via: "browseros"
---

# How I Hacked the Dutch Government with SQLi and Won the Famous T-Shirt?

How I Hacked the Dutch Government with SQLi and Won the Famous T-Shirt?
Göktuğ Kaya
Follow
Feb 25, 2022

45

5

Hello, those who are at the computer day and night. While reading hacking posts on Medium, I saw someone win this t-shirt. And so I started researching to win this t-shirt. From here, I set myself a target site. And I started testing the site. I came across a search function with filters.

Press enter or click to view image in full size
Example Request

Then I started checking the filters for SQLi. I changed the GET request to POST. And the “query” parameter not in the photo was vulnerable to SQLi attack.

For ethical reasons, I didn’t want to see the all database.
Get Göktuğ Kaya’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Payload;

‘%2b(select*from(select(sleep(20)))a)%2b’

I then reported this vulnerability to the NCSC-NL side and won this famous t-shirt. xD

Thanks for reading. And good luck. (:
