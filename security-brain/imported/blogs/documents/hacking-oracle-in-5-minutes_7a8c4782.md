---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-03-25_hacking-oracle-in-5-minutes.md
original_filename: 2018-03-25_hacking-oracle-in-5-minutes.md
title: Hacking Oracle in 5 Minutes
category: documents
detected_topics:
- xss
- command-injection
- information-disclosure
tags:
- imported
- documents
- xss
- command-injection
- information-disclosure
language: en
raw_sha256: 7a8c47820e12c29c5b692dccb0fdda8dac6e0e9f5cfab985b07e46675dd14a98
text_sha256: 07dca944653d1d5819f3e228af60be88dae21bd16e857dd865fc51b9cc90d262
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking Oracle in 5 Minutes

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-03-25_hacking-oracle-in-5-minutes.md
- Source Type: markdown
- Detected Topics: xss, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `7a8c47820e12c29c5b692dccb0fdda8dac6e0e9f5cfab985b07e46675dd14a98`
- Text SHA256: `07dca944653d1d5819f3e228af60be88dae21bd16e857dd865fc51b9cc90d262`


## Content

---
title: "Hacking Oracle in 5 Minutes"
url: "https://medium.com/bugbountywriteup/hacking-oracle-in-5-minutes-b52107a6124c"
authors: ["Rahul R"]
programs: ["Oracle"]
bugs: ["Directory listing"]
publication_date: "2018-03-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5945
scraped_via: "browseros"
---

# Hacking Oracle in 5 Minutes

Hacking Oracle in 5 Minutes
Rahul R
Follow
2 min read
·
Mar 25, 2018

445

2

So Hey everyone I am back with another write-up this time its Oracle

This is a really short write-up and there wont be much info

So few weeks back I was sitting at home watching TV and looking at my linked in when the Postman came with my Udacity Swag and I saw a post by someone who found a XSS in Oracle so I thought lets find some..

So I didn't have my laptop ( because i was so lazy to go upstairs) but I had termux in my mobile so I ran sublister against oracle.com and landed on a sub domain which had a directory listing that contained some random stuff looking through it I found some sensitive info such as host names, ip address , passwords etc .

Press enter or click to view image in full size
Press enter or click to view image in full size
Still don’t know what this is

Timeline

Get Rahul R’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Feb 24 Reported the Issue

Mar 09 Initial Reply

Mar 14 Fix issued

Mar 23 Fixed and HOF approved for Oracle CPU April 17

Press enter or click to view image in full size

And I was like
