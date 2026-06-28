---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-27_how-i-scored-2k-bounty-via-an-idor.md
original_filename: 2021-08-27_how-i-scored-2k-bounty-via-an-idor.md
title: How I Scored 2K Bounty via an IDOR
category: documents
detected_topics:
- idor
- command-injection
- mfa
tags:
- imported
- documents
- idor
- command-injection
- mfa
language: en
raw_sha256: 7687c425d5ca8fbb005619052294ce655ca2493b6a094f73169dd9c93374902a
text_sha256: 4ab84c557aabba0465cfe69f886ded02e5961eca5288bb080e6b59c651545268
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# How I Scored 2K Bounty via an IDOR

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-27_how-i-scored-2k-bounty-via-an-idor.md
- Source Type: markdown
- Detected Topics: idor, command-injection, mfa
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `7687c425d5ca8fbb005619052294ce655ca2493b6a094f73169dd9c93374902a`
- Text SHA256: `4ab84c557aabba0465cfe69f886ded02e5961eca5288bb080e6b59c651545268`


## Content

---
title: "How I Scored 2K Bounty via an IDOR"
url: "https://infosecwriteups.com/how-i-scored-2k-bounty-via-an-idor-32eb2fa8aa1e"
authors: ["Sicksec (@OriginalSicksec)"]
programs: ["Mail.ru"]
bugs: ["IDOR"]
bounty: "2,000"
publication_date: "2021-08-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3381
scraped_via: "browseros"
---

# How I Scored 2K Bounty via an IDOR

Top highlight

Member-only story

How I Scored 2K Bounty via an IDOR
Easiest IDOR ever ?!
Sicksec
Follow
2 min read
·
Aug 27, 2021

178

Press enter or click to view image in full size
Photo by Benjamin Dada on Unsplash

Hello Security Researchers

In this writeup I will talk how I was able to find an IDOR in one of the largest Russian Company nothing other than Mail.ru
So approaching targets with huge scope can be frustrating sometimes since you don’t know where to start
For me I started looking in the main scope of Mail.ru Games

I fired up Burp
Created an account
Adding things in my cart
Viewing the blog
Creating a support ticket

Before testing anything the ticket link looked kind of suspicious since it had /ticket/INTEGER
and the full URL looked like something like this

Let’s breakdown what can go wrong here
We have few parameters project_id user_id sign and the ticket number
First thing I did is to remove the sign which is the signature and see if I can access it from an unauthenticated browser
This looks easy no way that works right ?!!
