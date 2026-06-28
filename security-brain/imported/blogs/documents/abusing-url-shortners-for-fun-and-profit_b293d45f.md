---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-14_abusing-url-shortners-for-fun-and-profit.md
original_filename: 2022-07-14_abusing-url-shortners-for-fun-and-profit.md
title: Abusing URL Shortners for fun and profit
category: documents
detected_topics:
- idor
- command-injection
- otp
- rate-limit
- information-disclosure
- mobile-security
tags:
- imported
- documents
- idor
- command-injection
- otp
- rate-limit
- information-disclosure
- mobile-security
language: en
raw_sha256: b293d45fb969260aa0ed867c91449f506294180f89f614c7b073f19caac24231
text_sha256: c7bc64ab17100b28885d05b748f6366ec0d4058b314b9372df3019bab34a5ede
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Abusing URL Shortners for fun and profit

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-14_abusing-url-shortners-for-fun-and-profit.md
- Source Type: markdown
- Detected Topics: idor, command-injection, otp, rate-limit, information-disclosure, mobile-security
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `b293d45fb969260aa0ed867c91449f506294180f89f614c7b073f19caac24231`
- Text SHA256: `c7bc64ab17100b28885d05b748f6366ec0d4058b314b9372df3019bab34a5ede`


## Content

---
title: "Abusing URL Shortners for fun and profit"
url: "https://infosecwriteups.com/abusing-url-shortners-for-fun-and-profit-c83c67713916"
authors: ["Sicksec (@OriginalSicksec)"]
bugs: ["Information disclosure", "Account takeover", "IDOR"]
bounty: "3,000"
publication_date: "2022-07-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2453
scraped_via: "browseros"
---

# Abusing URL Shortners for fun and profit

Member-only story

Abusing URL Shortners for fun and profit
Sicksec
Follow
4 min read
·
Jul 14, 2022

155

2

Press enter or click to view image in full size
Photo by Boitumelo Phetla on Unsplash

Hello Security Researchers

Have you ever encountered a bug where it’s hard to show impact due to the lack of enumeration of a certain value of a parameter ?
Well if yes, In this writeup I will talk about how you can find and abuse URL shortners to ATO or Information disclosure

Many companies use URL shortners to send private invite and passwordless logins and things along those lines and it’s really difficult to guess or to brute these but there’s always a way to do things by thinking outside the box 📦

Let’s talk about URL shortners and their types:

URL shortners are mostly linked to 3rd party services like https://bitly.com https://cutt.ly/ and others are made by company and they have custom built
Like : https://indd.jobs | https://inst.cr

How can we approach this:

We can use multiple scenarios first we can test functionalities that triggers email and view the source of them if they contain a URL shortner check twitter account of company and extract all the links they share

How URL Shortners Work:

Most of the case we should look for something that has this kind of behavior
URLshortner.com/{HASH} ===> Website.com/?token={YOU-CANT-GUESS-THIS}
and…
