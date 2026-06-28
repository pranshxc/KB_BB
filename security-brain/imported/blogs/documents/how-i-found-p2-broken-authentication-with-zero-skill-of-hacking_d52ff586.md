---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-21_how-i-found-p2-broken-authentication-with-zero-skill-of-hacking.md
original_filename: 2021-12-21_how-i-found-p2-broken-authentication-with-zero-skill-of-hacking.md
title: How I found (P2) Broken Authentication with Zero Skill of Hacking
category: documents
detected_topics:
- command-injection
- password-reset
- automation-abuse
- mobile-security
tags:
- imported
- documents
- command-injection
- password-reset
- automation-abuse
- mobile-security
language: en
raw_sha256: d52ff586e814ae3543c292c326d718eb20a6c8ed81a762085fb37a81524d61eb
text_sha256: 7365dbd14f54be6a756cc8771608385c3e4ddf40a87ee9f5a40739c60771207e
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# How I found (P2) Broken Authentication with Zero Skill of Hacking

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-21_how-i-found-p2-broken-authentication-with-zero-skill-of-hacking.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, automation-abuse, mobile-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `d52ff586e814ae3543c292c326d718eb20a6c8ed81a762085fb37a81524d61eb`
- Text SHA256: `7365dbd14f54be6a756cc8771608385c3e4ddf40a87ee9f5a40739c60771207e`


## Content

---
title: "How I found (P2) Broken Authentication with Zero Skill of Hacking"
url: "https://medium.com/@yoshimlutfi/how-i-found-p2-broken-authentication-with-zero-skill-of-hacking-c40b5643fe4a"
authors: ["yoshi m lutfi (@yoshiahmadlutfi)"]
bugs: ["Authentication bypass", "Account takeover"]
publication_date: "2021-12-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3071
scraped_via: "browseros"
---

# How I found (P2) Broken Authentication with Zero Skill of Hacking

How I found (P2) Broken Authentication with Zero Skill of Hacking
yoshi m lutfi
Follow
2 min read
·
Dec 21, 2021

26

1

This is a local bounty program in my country that I recently joined,
I choose one of the programs and try to analyze it, this program runs on 2 platforms, as usual, web and mobile applications.

Either on the web/mobile application there is a mechanism, if we use a new browser/device to access the app then the system will send email verification to be able to use the application. Apart from being in the form of an email, the application also displays another mechanism by using a phone call verification.

I am testing the mobile application first and doing normal flow, everything went smoothly, verification using email or phone calls went well. then I thought, what if the verification using a phone call is done in a web application, how will the server validate the call? because our laptop cannot receive a call right?

Get yoshi m lutfi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now I access the application using the web, and when a message appears that I must verify using the email sent to my email, then I choose another alternative, which is a phone call, and strangely, the application immediately verifies the user and manages to enter the dashboard without any mechanism, whatever be it a phone call or whatever.

I finally reported the bugs and my report was accepted and got a severity risk of P2 (High).

Now they only use email verification only

Tips:
If the application can run on different platforms, explore each function of the application. then try to use each of these functions on both platforms, maybe there are some functions that have not been validated or anything that could be a security hole.
