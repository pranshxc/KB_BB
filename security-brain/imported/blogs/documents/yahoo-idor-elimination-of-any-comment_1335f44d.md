---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-08-17_yahoo-idor-elimination-of-any-comment.md
original_filename: 2018-08-17_yahoo-idor-elimination-of-any-comment.md
title: YAHOO IDOR -elimination of any comment
category: documents
detected_topics:
- idor
- command-injection
tags:
- imported
- documents
- idor
- command-injection
language: en
raw_sha256: 1335f44d14cdaad48dd381ca1521e4d5bd9d33f6555494bb981ba760a000dd1d
text_sha256: f715c3ec6dab443f36d487421f477f3dec814fba5fbdfde53639c04f556da152
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# YAHOO IDOR -elimination of any comment

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-08-17_yahoo-idor-elimination-of-any-comment.md
- Source Type: markdown
- Detected Topics: idor, command-injection
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `1335f44d14cdaad48dd381ca1521e4d5bd9d33f6555494bb981ba760a000dd1d`
- Text SHA256: `f715c3ec6dab443f36d487421f477f3dec814fba5fbdfde53639c04f556da152`


## Content

---
title: "YAHOO IDOR -elimination of any comment"
url: "https://medium.com/@black_b/yahoo-idor-elimination-of-any-comment-e898f4f955f1"
authors: ["Bada Diaz (@bada77)"]
programs: ["Yahoo! / Verizon Media"]
bugs: ["IDOR"]
publication_date: "2018-08-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5746
scraped_via: "browseros"
---

# YAHOO IDOR -elimination of any comment

YAHOO IDOR -elimination of any comment
black_b
Follow
2 min read
·
Aug 17, 2018

33

Hello everyone, my name is Bernardo and I’m from Chile, this time I bring you a bug (IDOR) that I found in Yahoo that allows you to remove any comments on the website.

I found this vulnerability on a page https: //*.yahoo.com, which users commented and evaluated a product from that website, so I started to see the comments and evaluations of users on the website and I found with the next surprise.

POC

Get black_b’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Id = my own

id = user

Press enter or click to view image in full size

and the surprise appeared the comment of that user was deleted.

my face when this happened

thanks for reading this post

thanks 
HackerOne

bug bounty yahoo reward
and swag yahoo :D

My data: https://twitter.com/bada_77
