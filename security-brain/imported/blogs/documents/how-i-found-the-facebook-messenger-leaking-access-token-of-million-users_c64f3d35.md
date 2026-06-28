---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-13_how-i-found-the-facebook-messenger-leaking-access-token-of-million-users.md
original_filename: 2020-11-13_how-i-found-the-facebook-messenger-leaking-access-token-of-million-users.md
title: How I Found The Facebook Messenger Leaking Access Token Of Million Users
category: documents
detected_topics:
- command-injection
- otp
- information-disclosure
- api-security
- mobile-security
- supply-chain
tags:
- imported
- documents
- command-injection
- otp
- information-disclosure
- api-security
- mobile-security
- supply-chain
language: en
raw_sha256: c64f3d358799daf82277bd0ef61f52a93714b36c64b5cef90083ca25a0fd162c
text_sha256: 00f5b89e322a30f47c653f777ea5077da1f63a32146cc3f0261cd4c035fcc488
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# How I Found The Facebook Messenger Leaking Access Token Of Million Users

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-13_how-i-found-the-facebook-messenger-leaking-access-token-of-million-users.md
- Source Type: markdown
- Detected Topics: command-injection, otp, information-disclosure, api-security, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `c64f3d358799daf82277bd0ef61f52a93714b36c64b5cef90083ca25a0fd162c`
- Text SHA256: `00f5b89e322a30f47c653f777ea5077da1f63a32146cc3f0261cd4c035fcc488`


## Content

---
title: "How I Found The Facebook Messenger Leaking Access Token Of Million Users"
url: "https://medium.com/@guhanraja/how-i-found-the-facebook-messenger-leaking-access-token-of-million-users-8ee4b3f1e5e3"
authors: ["Guhan Raja (@havocgwen)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
bounty: "16,125"
publication_date: "2020-11-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4138
scraped_via: "browseros"
---

# How I Found The Facebook Messenger Leaking Access Token Of Million Users

How I Found The Facebook Messenger Leaking Access Token Of Million Users
Guhan Raja
Follow
2 min read
·
Nov 12, 2020

792

4

Hi everyone,

This blog tells the story of how I discovered that the Facebook Messenger iOS app was leaking access tokens of millions of users to a third-party site, a GIF search engine

Press enter or click to view image in full size

I was checking out an iOS app and trying to see if I could find any issues with it. After a while, I didn’t find anything interesting, so I closed the app and went back to using my phone as usual

Then, I got a message from a friend on Messenger, so I opened it up to reply with a GIF. While doing this, I remembered I had this tool called Burp running, which helps me see the data that apps send. When I checked the data, I noticed that every time I searched for a GIF, my Facebook access token was being sent in the third-party GIF search engine’s domain request

What is Access Token?
An access token is some kind of a temporary token or a key which is used to perform certain actions on behalf of the user

Get Guhan Raja’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

What we can do with that?
Using token we can access the user’s account without password

Press enter or click to view image in full size

Immediately I have reported the issue to Facebook. They took a day to look into it, then sent it over to their Product Team. Surprisingly, within just 5 hours, they rolled out an update to fix the issue temporarily

Press enter or click to view image in full size

POC Video:

Timeline:
26-Sep-2020: Report Sent
28-Sep-2020: Further investigation by Facebook
28-Sep-2020: Temporary Fix
06-Oct-2020: Fixed
10-Nov-2020: Rewarded 15k$

Conclusion:
Facebook has confirmed that there is no evidence of abuse and has invalidated all relevant access tokens

Press enter or click to view image in full size

Thanks to Priya Sarvesan (my college mate who texted me) and Facebook Security Team.
