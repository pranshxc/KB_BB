---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-04-13_how-did-i-easily-find-stored-xss-at-apple-and-earn-5000-.md
original_filename: 2024-04-13_how-did-i-easily-find-stored-xss-at-apple-and-earn-5000-.md
title: How Did I Easily Find Stored XSS at Apple And Earn $5000 ?
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
raw_sha256: ba4ff1798ca9b05efc4fc607ad7aa2a12cb606c61891e549050f7f95c3bd033f
text_sha256: a6d23b85496f744c0e3991cc333418353752b5e48c32ef910c3b0422e0068348
ingested_at: '2026-06-28T07:32:32Z'
sensitivity: unknown
redactions_applied: false
---

# How Did I Easily Find Stored XSS at Apple And Earn $5000 ?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-04-13_how-did-i-easily-find-stored-xss-at-apple-and-earn-5000-.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:32Z
- Redactions Applied: False
- Raw SHA256: `ba4ff1798ca9b05efc4fc607ad7aa2a12cb606c61891e549050f7f95c3bd033f`
- Text SHA256: `a6d23b85496f744c0e3991cc333418353752b5e48c32ef910c3b0422e0068348`


## Content

---
title: "How Did I Easily Find Stored XSS at Apple And Earn $5000 ?"
url: "https://medium.com/@xrypt0/how-did-i-easily-find-stored-xss-at-apple-and-earn-5000-3aadbae054b2"
authors: ["Crypto (@xryptc)"]
programs: ["Apple"]
bugs: ["Stored XSS"]
bounty: "5,000"
publication_date: "2024-04-13"
added_date: "2024-05-11"
source: "pentester.land/writeups.json"
original_index: 341
scraped_via: "browseros"
---

# How Did I Easily Find Stored XSS at Apple And Earn $5000 ?

Top highlight

How Did I Easily Find Stored XSS at Apple And Earn $5000 ?
Crypto
Follow
3 min read
·
Apr 14, 2024

1K

17

Hello there ! Today we’ll talk about stored XSS which I found in Apple. Without further ado let’s get into it !

Press enter or click to view image in full size
Apple Sec.

First of all, our vulnerable Apple service was: https://discussions.apple.com

Get Crypto’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This service is a community where Apple users and developers discuss their problems. If you register here you can create a profile for yourself and help others or get help from them !

Press enter or click to view image in full size
It Was My Profile

Now let’s look at a simple example profile.

Press enter or click to view image in full size

This is a simple profile that I have prepared for you. As you can see you can edit the “Location” and “Bio” sections as you wish.

What If We Use A XSS Payload ?
Hmm

Payload that will be used is :

"><svg/onload=alert(1)>

We’ll place this payload in the “Location” section of our Apple profile and take a look at the result together !

Press enter or click to view image in full size
XSS

As you can see this is a Stored XSS vulnerability that is very easy to exploit ! Cookies of users and employees could be stolen, and it was very easy to achieve that with this way !

:-o

As soon as I found something like this, I immediately contacted Apple Security via e-mail. At the end of our 3-month process, I received an e-mail like the one below and I was rewarded !

Press enter or click to view image in full size
Yuppi

This is how I got the XSS vulnerability in Apple in a very easy way and completed it with great success ! I leave you with Apple’s Hall Of Fame list and my position on the list below.

https://support.apple.com/en-us/102812 (June 2022) (@xrypt0)

Thank you for reading this far and paying attention. See you in future articles !

bb

Crypto (@xrypt0)

X
