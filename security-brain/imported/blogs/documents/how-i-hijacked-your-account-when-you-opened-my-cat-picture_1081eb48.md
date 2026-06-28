---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-09-14_how-i-hijacked-your-account-when-you-opened-my-cat-picture.md
original_filename: 2018-09-14_how-i-hijacked-your-account-when-you-opened-my-cat-picture.md
title: How I hijacked your account when you opened my cat picture
category: documents
detected_topics:
- idor
- sqli
- command-injection
- otp
- csrf
- api-security
tags:
- imported
- documents
- idor
- sqli
- command-injection
- otp
- csrf
- api-security
language: en
raw_sha256: 1081eb4836047e44ac35b88c9d42df788c62ef43d7e49ee4a4640d8d1db58d94
text_sha256: 0882d168d477fbc1d3f1eb9c74cece77a586f69fe8148a5dffb48b6045354865
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# How I hijacked your account when you opened my cat picture

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-09-14_how-i-hijacked-your-account-when-you-opened-my-cat-picture.md
- Source Type: markdown
- Detected Topics: idor, sqli, command-injection, otp, csrf, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `1081eb4836047e44ac35b88c9d42df788c62ef43d7e49ee4a4640d8d1db58d94`
- Text SHA256: `0882d168d477fbc1d3f1eb9c74cece77a586f69fe8148a5dffb48b6045354865`


## Content

---
title: "How I hijacked your account when you opened my cat picture"
url: "https://medium.com/intigriti/how-i-hijacked-your-account-when-you-opened-my-cat-picture-9a0a0acca9e8"
authors: ["Matti Bijnens (@MattiBijnens)"]
bugs: ["Logout CSRF"]
publication_date: "2018-09-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5700
scraped_via: "browseros"
---

# How I hijacked your account when you opened my cat picture

How I hijacked your account when you opened my cat picture
Matti Bijnens
Follow
3 min read
·
Sep 14, 2018

457

2

Press enter or click to view image in full size

I set a goal for a particular program to find a way to take-over someone’s account. My goal was to be able to pick a random user (or all users) and take-over their account without any interaction.

I believe setting goals is something every bug hunter should do. I have noticed for myself that without a goal, you are just trying random things and are unlikely to accomplish anything useful. Goals can be things like “Find a SQLi in program X”, “Find an IDOR on program X” or “Find a take-over on program X”.

I had tried several things on this program trying to hijack accounts, when I looked to find an IDOR in the “Change Email” functionality. The request for changing your e-mail looked like this:

Press enter or click to view image in full size

There is nothing like an OldEmail parameter in this request, so I don’t really see much of an opportunity for IDOR here. But something else caught my eye, the value for the g-recaptcha-response is empty. I don’t see any other CSRF Token, so there is no way they are checking for CSRF on this page.

One of the most important steps is to create a proper PoC. Without a PoC your report is useless. So I created a PoC which looked as follows:

This PoC worked, but when executing it I didn’t get this “wow” feeling an account take-over should have. There were several problems:

The victim remained logged in on his account because the sessions were not invalidated.
The PoC only worked one time because after that the account “new-email2@gmail.com” already existed.

Like most programs, this one didn’t care about logout-CSRF. Good for us. We can abuse this “feature” to make the PoC a little more interesting. To solve the second issue I simply added a random number to the e-mail so you could execute it multiple times.

Get Matti Bijnens’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The final PoC looked something like this:

Press enter or click to view image in full size

I opted to use an input box to make it easier for the triage team to change it to an email they own themselves.

There are several things to be learned from this:

Out of scope / non severe bugs can be useful in a chain with other things
Make a great PoC to help developers better understand the severity of some issues.

I opted to mark the report as medium severity because there was still a lot of interaction required to exploit this.

I reported the bug on Intigriti and it got validated very quickly and I got a bounty in no time.

@MattiBijnens
