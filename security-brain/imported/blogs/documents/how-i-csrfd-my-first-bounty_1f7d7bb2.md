---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-03_how-i-csrfd-my-first-bounty.md
original_filename: 2020-03-03_how-i-csrfd-my-first-bounty.md
title: How I CSRF’d My First Bounty!
category: documents
detected_topics:
- csrf
- command-injection
- otp
tags:
- imported
- documents
- csrf
- command-injection
- otp
language: en
raw_sha256: 1f7d7bb2f227693515e29825c62e6be1ef9c92e675e5d1ac2c69874288d1bdf6
text_sha256: 12e1df0703256805def382f185cae85942e33014d9908efcbb80257a821d591d
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# How I CSRF’d My First Bounty!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-03_how-i-csrfd-my-first-bounty.md
- Source Type: markdown
- Detected Topics: csrf, command-injection, otp
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `1f7d7bb2f227693515e29825c62e6be1ef9c92e675e5d1ac2c69874288d1bdf6`
- Text SHA256: `12e1df0703256805def382f185cae85942e33014d9908efcbb80257a821d591d`


## Content

---
title: "How I CSRF’d My First Bounty!"
url: "https://medium.com/@rajeshranjan457/how-i-csrfd-my-first-bounty-a62b593d3f4d"
authors: ["Rajesh Ranjan (@rajesh_ranjan4)"]
bugs: ["CSRF"]
bounty: "500"
publication_date: "2020-03-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4739
scraped_via: "browseros"
---

# How I CSRF’d My First Bounty!

How I CSRF’d My First Bounty!
Rajesh Ranjan
Follow
2 min read
·
Mar 3, 2020

275

2

Hello Everyone!

This is my first blog post, and I decided to start off by sharing about my recent finding. It was a CSRF issue, which earned me $500!

What makes this even more special for me is that it was my first bounty ever!

Introduction to CSRF:
Cross-Site Request Forgery (CSRF) is an attack that forces an end user to execute unwanted actions on a web application in which they’re currently authenticated.

Initial Reconnaissance Phase
So, I got an invitation for this private program on Bugcrowd, and it was an e-commerce website.

During my initial recon, I noticed that the users can add their address into their account. So, I quickly checked the request and there was some token named form_key that was being used to protect the users from CSRF attack.

Press enter or click to view image in full size
form_key to protect CSRF attacks

So, the next thought which came to my mind was, is there any server side validation on this token?

I quickly logged into my second test account, generated a CSRF PoC, removed the token for this particular request, and sent it to the victim.

And the final request was something like this:

Press enter or click to view image in full size
Removed the form_key value in the request

Did you notice something? I have removed the form_key value from the PoC, and not the entire input tag.

Get Rajesh Ranjan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I sent this to the victim, and when the victim clicked on “Submit”, the address was added to his account, which was the attacker’s address.

Press enter or click to view image in full size
Attacker’s address added to victim account

Boom! Like I suspected, there was no server-side validation on form_key token.

So, the next time you come across a CSRF token, be sure to perform this kind of validation.

Timeline:

Issue reported: 06 Nov 2019

Triaged as P3: 09 Nov 2019

Bounty received: 05 Jan 2020

Thanks for reading. Hope it helps

.

Connect me on twitter https://twitter.com/_rajesh_ranjan_
