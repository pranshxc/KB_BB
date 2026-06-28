---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-22_fun-with-header-and-forget-password.md
original_filename: 2020-09-22_fun-with-header-and-forget-password.md
title: Fun with Header and Forget Password
category: documents
detected_topics:
- sqli
- xss
- command-injection
tags:
- imported
- documents
- sqli
- xss
- command-injection
language: en
raw_sha256: 32887419c9e0696c259108b02876b9ce19d466fe55c7ad5c53d7eb186d10fe97
text_sha256: c7f13cc83726056719dc7e7423235dfb505d16d6f5de6b2e69ae4d3ba7e5d1f1
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Fun with Header and Forget Password

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-22_fun-with-header-and-forget-password.md
- Source Type: markdown
- Detected Topics: sqli, xss, command-injection
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `32887419c9e0696c259108b02876b9ce19d466fe55c7ad5c53d7eb186d10fe97`
- Text SHA256: `c7f13cc83726056719dc7e7423235dfb505d16d6f5de6b2e69ae4d3ba7e5d1f1`


## Content

---
title: "Fun with Header and Forget Password"
url: "https://medium.com/bugbountywriteup/fun-with-header-and-forget-password-without-that-nasty-twist-cbf45e5cc8db"
authors: ["Vuk Ivanovic"]
bugs: ["HTTP header injection"]
publication_date: "2020-09-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4244
scraped_via: "browseros"
---

# Fun with Header and Forget Password

Member-only story

Fun with Header and Forget Password
— Without that nasty twist
Vuk Ivanovic
Follow
2 min read
·
Sep 22, 2020

56

Press enter or click to view image in full size

This one doesn’t have that awful caveat compared to my other article :)
Playing around with headers is important during bug hunting. But, it’s easy to limit yourself to just sending GET requests with blind xss/blind sqli/blind rce/etc. inside Referer, User-Agent, Cookies, custom headers, etc. But, that’s an easy way to miss things. Had I not used Match and Replace rule in burp suite I wouldn’t have detected this bug.

The initial phase:

In order to determine if there were any delayed pingbacks as per portswigger article[link], I had Referer header set to pingb.in payload. And, after browsing the target website, using various functions, I checked for any pingbacks. Got nothing, not even dns. I figured, maybe there is a delay of a few hours if not longer than that, so I left it be. Spoiler: never got any delayed pingbacks in this case, but this article isn’t about that :)

The discovery:

The target website in question also had Sign up functionality, and with it Forget password. And during the previous step, I also triggered forget password to look into it later. To my surprise when I checked my email, the password recovery link used my pingb.in link.
