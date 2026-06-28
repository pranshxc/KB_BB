---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-01-29_protonmail-xss-stored.md
original_filename: 2019-01-29_protonmail-xss-stored.md
title: Protonmail XSS — Stored
category: documents
detected_topics:
- xss
- idor
- command-injection
- password-reset
- rate-limit
- api-security
tags:
- imported
- documents
- xss
- idor
- command-injection
- password-reset
- rate-limit
- api-security
language: en
raw_sha256: 76cf88add8b4db57f5876179abbf7aaefadcffca6415874a82e5490ca5707b5a
text_sha256: f3a78f418af13fbe913d0bf0b87424b75d74bcfb94a1715b37d43aacbbe8d482
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Protonmail XSS — Stored

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-01-29_protonmail-xss-stored.md
- Source Type: markdown
- Detected Topics: xss, idor, command-injection, password-reset, rate-limit, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `76cf88add8b4db57f5876179abbf7aaefadcffca6415874a82e5490ca5707b5a`
- Text SHA256: `f3a78f418af13fbe913d0bf0b87424b75d74bcfb94a1715b37d43aacbbe8d482`


## Content

---
title: "Protonmail XSS — Stored"
page_title: "Protonmail XSS — Stored. Hello Everyone, | by Chand Singh | Medium"
url: "https://medium.com/@ChandSingh/protonmail-xss-stored-b733031ac3b5"
authors: ["Chand Singh (@Chand_42)"]
programs: ["Proton Mail"]
bugs: ["Stored XSS", "Bruteforce"]
publication_date: "2019-01-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5443
scraped_via: "browseros"
---

# Protonmail XSS — Stored

Chand Singh
 highlighted

Protonmail XSS — Stored
Chand Singh
Follow
2 min read
·
Jan 29, 2019

160

Hello Everyone,

It’s my first blog post related to my bug bounty work so many people are sharing there findings so I’m also try to write something.

I’m not professional in writing these type of stuff so there are many mistakes you can see in this post, so without waisting your time to read my bad english , i would like to share my finding’s.

It’s Series of Vulnerability which i found in the Protonmail Web app and also IOS app, and only publishing two now related to Protonmail.

#1 Vulnerability

Brute Force Attack on 10 Digit Code to Hijack any User Account

I searched on internet for bug bounty website’s and i found Protonmail, before that i have not heard about that email service name. So i try , what i can do with protonmail.

I just signed-up the service and checking there password reset functionality related to IDOR attacks but nothing found but i notice that they are sending the 10 Digit code to reset the password !

Proof of Concept for Brute force attack :

Protonmail (1)

#2 Vulnerability

Stored XSS in Email Inbox

Get Chand Singh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

It was interesting finding one of mine in the email service which is Stored XSS in protonmail, and it’s very easy to exploit to another user just by sending the email.

Steps to Reproduce the issue :

From Attacker Account :

Compose a email to any protonmaail user with Subject

#”><img src=x onerror=prompt(1);>

2. Send email to victim

From Victim Account :

3. open email message from victim email click on reply

4. XSS executed ! :)

Proof of Concept :

Press enter or click to view image in full size
Protonmail XSS

I found many other bugs in Protonmail and many other XSS and Recently XSS in IOS App . Soon i will write on this.

Thanks for the Protonmail Team they fix these issue quickly and they are very responsible person and awarded the bounty according to there Program :)

Thanks for Reading, Hope you liked it !
