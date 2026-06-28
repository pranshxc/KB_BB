---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-15_how-i-spammed-a-google-meet-but-for-good.md
original_filename: 2022-07-15_how-i-spammed-a-google-meet-but-for-good.md
title: How I spammed a Google meet (But for good)
category: documents
detected_topics:
- access-control
- command-injection
tags:
- imported
- documents
- access-control
- command-injection
language: en
raw_sha256: 3db1212d91d717c836c40e14aa6cf3c4a169953fcc132f78090a5d007fa0afc4
text_sha256: 7850159953550fa13963c6e8d8a9739cce17c1ab72e9b308f81860d8dd08ede3
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# How I spammed a Google meet (But for good)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-15_how-i-spammed-a-google-meet-but-for-good.md
- Source Type: markdown
- Detected Topics: access-control, command-injection
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `3db1212d91d717c836c40e14aa6cf3c4a169953fcc132f78090a5d007fa0afc4`
- Text SHA256: `7850159953550fa13963c6e8d8a9739cce17c1ab72e9b308f81860d8dd08ede3`


## Content

---
title: "How I spammed a Google meet (But for good)"
url: "https://medium.com/@shaunak007/how-i-spammed-a-google-meet-but-for-good-8bc5b328f1bb"
authors: ["Shaunak (SHA25)"]
programs: ["Google"]
bugs: ["DoS"]
publication_date: "2022-07-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2450
scraped_via: "browseros"
---

# How I spammed a Google meet (But for good)

How I spammed a Google meet (But for good)
Shaunak (SHA25)
Follow
2 min read
·
Jul 15, 2022

11

Hacking isn’t always about account takeover, authentication bypass, or authorization abuse. Sometimes it’s about functionality abuse and how it can impact the organization and the customers as well.

So foreground to my research was an illicit intention it was to bomb my class Gooogle meet and to cut the class with an excuse of some technical glitch. But later I recognized it could be a valid bug because everything was virtualized it was everyone’s biggest concern how to reduce the gaps in the virtual process. As my script was leading to DoS as well if the devices were supposedly not able to handle so much traffic. So I started to check if previously any similar bugs were reported or if issues were found to be valid or not. And the similar case was present on the Twitch where spamming was taken care of so creating much fuzz for the event manager to block/ban the attendees in such situations.

Get Shaunak (SHA25)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now, jumping to the juicy part how I exploited/took advantage of the leverage here. So, it was pretty simple all I had to is a script that could do the spamming for me and keeps it until everything I am kicked. I found a vintage script on how to send automated replies(back from 2008 probably) with just a click using VbScript. I learned a bit about VbScript and modified it to work it for me and it did the magic for me ;).

Meet - gdx-kzdw-ahk - Google Chrome 2020-11-11 17-18-58.mp4
Edit description

drive.google.com

GitHub - Shaunak-Chatterjee/SpamHell
The script is for educational purposes only. Any use of the script for the malicious or illegitimate purpose I shall not be…

github.com

The script can be found in my Git repo, I would suggest using it wisely and not with illicit intentions.

Fast forward to the submission, it was accepted initially as a bug. But later, I got to know it was a known issue(internally) and it was already being investigated to take appropriate actions. Attaching my heartbreak response from Google(while sobbing in the corner).

Press enter or click to view image in full size

The intention of sharing the experience is to spread my learning to someone trying to find bugs in similar engagement and at times it’s overwhelming but you got in you ;)
