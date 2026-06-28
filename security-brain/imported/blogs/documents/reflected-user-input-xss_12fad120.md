---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-15_reflected-user-input-xss.md
original_filename: 2020-06-15_reflected-user-input-xss.md
title: Reflected User Input == XSS!
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
raw_sha256: 12fad120b609b893248e32970f645d825b54f586c8835ab39998591bf4400a13
text_sha256: 56987c7da11186c486573476e2927cbec35b0fe3d0edd227f4b26b2eb2b39b51
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Reflected User Input == XSS!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-15_reflected-user-input-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `12fad120b609b893248e32970f645d825b54f586c8835ab39998591bf4400a13`
- Text SHA256: `56987c7da11186c486573476e2927cbec35b0fe3d0edd227f4b26b2eb2b39b51`


## Content

---
title: "Reflected User Input == XSS!"
url: "https://medium.com/bugbountywriteup/reflected-user-input-xss-c3e681710e74"
authors: ["Silent Bronco (@silentbronco)"]
bugs: ["Reflected XSS"]
bounty: "50"
publication_date: "2020-06-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4495
scraped_via: "browseros"
---

# Reflected User Input == XSS!

Tushar Bhardwaj
 highlighted

Reflected User Input == XSS!
Tushar Bhardwaj
Follow
2 min read
·
Jun 16, 2020

214

Hey guys! I hope everyone is doing great, this a small writeup of one of my findings, hope this can help you. Let's start!

Popped an alert box through the email field.

In
December, REDACTED decided to go public with their Bug Bounty program,so I thought why not hunt their as they had a huge scope.

Get Tushar Bhardwaj’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Here’s some really basic info before we dig in:

Email addresses are widely used in forms and displayed several times in different parts of a web application.Any input different from a classic email format gets rejected by application returning an “INVALID” response

While testing the support ,I found this:

Support Page

As we can see above, that the email: test@test.com is being reflected, tried the basic XSS payload: <script>alert()</script> but no luck as it required “@” in the email field.

Press enter or click to view image in full size

I remembered reading Brutelogic’s XSS in limited input formats.I strongly suggest reading his post, he has explained many other situations which will be of great help and might come in handy.

So,the payload I used in the email field was “<svg/onload=alert(1)>”@x.y .Submit and I have a pop-up on my screen!

I was awarded a $50 bounty for this reflected “email” XSS.

Thank you for reading!

Also, don’t forget to follow me on Twitter
