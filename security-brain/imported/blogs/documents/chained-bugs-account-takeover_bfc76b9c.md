---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-16_chained-bugs-account-takeover-.md
original_filename: 2020-05-16_chained-bugs-account-takeover-.md
title: Chained Bugs [ Account TakeOver ]
category: documents
detected_topics:
- idor
- xss
- command-injection
- otp
tags:
- imported
- documents
- idor
- xss
- command-injection
- otp
language: en
raw_sha256: bfc76b9cf471cd24f918383e68c81cefe42186d61c8f3eda426cc40ff3def503
text_sha256: e455514643646dbe11fac4fd7e1f5de860705dae8c8ac86cfb1d728aabcedd91
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Chained Bugs [ Account TakeOver ]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-16_chained-bugs-account-takeover-.md
- Source Type: markdown
- Detected Topics: idor, xss, command-injection, otp
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `bfc76b9cf471cd24f918383e68c81cefe42186d61c8f3eda426cc40ff3def503`
- Text SHA256: `e455514643646dbe11fac4fd7e1f5de860705dae8c8ac86cfb1d728aabcedd91`


## Content

---
title: "Chained Bugs [ Account TakeOver ]"
url: "https://medium.com/@bilalmerokhel/chained-bugs-account-takeover-ceff67d1d55a"
authors: ["Bilal Khan (@bilalmerokhel)"]
bugs: ["IDOR", "XSS", "Account takeover"]
bounty: "1,050"
publication_date: "2020-05-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4586
scraped_via: "browseros"
---

# Chained Bugs [ Account TakeOver ]

Chained Bugs [ Account TakeOver ]
Bilal Khan
Follow
2 min read
·
May 16, 2020

104

1

A
ssalam-O-Alaikum fellas hope you all are fine, it has been a while I've not contributed to the community so, today I will share chained bugs which led to account takeover. The program doesn't allow public disclosure so I will set the name, to chintu.com. First I will explain how I was able to get the IDOR and then how the account takeover part has taken place via XSS so, let's get started.

Story101.

The bug I reported was an IDOR with which, I was able to change the profile data but not the primary email which is used to login to an account, so I saw another field the secondary email, I thought maybe this email could be used to login to the account I didn’t try it and reported to the chintu.com, with the title [ Critical ] IDOR leads to Account TakeOver, After few days the report was Triaged and I was so happy, within few days I got a reply with $1250 bounty, but suddenly on the same day the ASE change the reward to 200$ and set the priority to P4 and created a blocker to answer their question. the argument was.

Get Bilal Khan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Press enter or click to view image in full size
Blocker
Press enter or click to view image in full size

I was so mad about the reward, so I started digging the application and while doing further recon and testing I came across an endpoint which was showing the latest profile points where the username was reflected and was not sanitized properly, I thought let's try XSS and I succeeded, what I did was change the username field via IDOR with the XSS payload and sent the Auth token to my server via XSS, after reporting this to the chintu.com their reply was.

Press enter or click to view image in full size
P2 -> 1050$

Always try harder, thanks for reading.
