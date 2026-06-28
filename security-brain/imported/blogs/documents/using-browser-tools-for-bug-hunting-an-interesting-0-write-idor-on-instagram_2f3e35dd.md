---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-08-04_using-browser-tools-for-bug-hunting-an-interesting-0-write-idor-on-instagram.md
original_filename: 2023-08-04_using-browser-tools-for-bug-hunting-an-interesting-0-write-idor-on-instagram.md
title: 'Using Browser Tools For Bug Hunting: An Interesting 0$ Write IDOR On Instagram'
category: documents
detected_topics:
- idor
- command-injection
- api-security
- mobile-security
tags:
- imported
- documents
- idor
- command-injection
- api-security
- mobile-security
language: en
raw_sha256: 2f3e35ddabf584244dd1bf01467133a1b7e622cad19d45e1d2c2b997fd263eb0
text_sha256: 67cd301b8514f98acf449fdb67625943badd5a0eebc50af89d4c0b6dd8179d45
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# Using Browser Tools For Bug Hunting: An Interesting 0$ Write IDOR On Instagram

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-08-04_using-browser-tools-for-bug-hunting-an-interesting-0-write-idor-on-instagram.md
- Source Type: markdown
- Detected Topics: idor, command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `2f3e35ddabf584244dd1bf01467133a1b7e622cad19d45e1d2c2b997fd263eb0`
- Text SHA256: `67cd301b8514f98acf449fdb67625943badd5a0eebc50af89d4c0b6dd8179d45`


## Content

---
title: "Using Browser Tools For Bug Hunting: An Interesting 0$ Write IDOR On Instagram"
url: "https://faizanwrites.medium.com/using-browser-tools-for-bug-hunting-an-interesting-0-write-idor-on-instagram-7d5318299c1a"
authors: ["Faizan Ahmad Wani"]
programs: ["Meta / Facebook (Instagram)"]
bugs: ["IDOR", "iOS"]
publication_date: "2023-08-04"
added_date: "2023-08-08"
source: "pentester.land/writeups.json"
original_index: 882
scraped_via: "browseros"
---

# Using Browser Tools For Bug Hunting: An Interesting 0$ Write IDOR On Instagram

Using Browser Tools For Bug Hunting: An Interesting 0$ Write IDOR On Instagram
Faizan Ahmad Wani
Follow
2 min read
·
Aug 4, 2023

79

1

I’ve been crazy for hacking Instagram, trying hard to get a valid bug and one day as I observed: Instagram app provides more account & app options to the user on mobile as compared to a user browsing on desktop. This scratched my brain, and uh oh! I smashed the fn + F12 on my browser while being signed in to my instagram. This opened the infamous browser developer tools and I toggled the device toolbar to switch my browser to simulate a mobile view. And the story begins…

An Insecure Direct Object Reference (IDOR) arises when arbitrary data entered from user is processed in an unsafe way without integrity check.In this case, while I was testing instagram application, I found that a user has the option to report bugs to instagram in profile settings. However the POST request contains a user_identifier parameter which contains Profile User ID of an instagram user which can unfortunately be tampered, to resemble any other user account and submit report on their behalf.

The reproduction steps were easy peasy:

Users: [Just an Instagram account is required]

Environment: [Tested on Mozilla firefox: with pagination changed to iOS iphone 11]

Browser: [Firefox]

Get Faizan Ahmad Wani’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

OS: [iOS]

Goto Profile Settings in Instagram ( Make sure in developer options you’ve set the resolution to Mobile Phone.
Click on circular setting options
Click Report Bug
Type anything and capture the POST request to Graph.facebook.com
Tamper the user_identifier parameter to resemble any valid user’s user_identifier (This can be fetched easily from visiting a user’s profile)

And guess what, I submitted it to Meta, and the reply was:

Press enter or click to view image in full size

RIP Integrity from the CIA triad.

Thats it for this blog guys, have a great day.
