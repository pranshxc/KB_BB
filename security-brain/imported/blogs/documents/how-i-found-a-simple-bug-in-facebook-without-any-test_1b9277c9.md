---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-01-31_how-i-found-a-simple-bug-in-facebook-without-any-test_2.md
original_filename: 2019-01-31_how-i-found-a-simple-bug-in-facebook-without-any-test_2.md
title: How I found a simple bug in Facebook without any Test
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
raw_sha256: 1b9277c9d118c8f152d8117f11fdfcba50edc8de537ea6019496785612e82ba7
text_sha256: d701ae3b59c0dc182993aabe230a5bf17e41f0ea11a438c6e211b6fdbf201975
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# How I found a simple bug in Facebook without any Test

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-01-31_how-i-found-a-simple-bug-in-facebook-without-any-test_2.md
- Source Type: markdown
- Detected Topics: access-control, command-injection
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `1b9277c9d118c8f152d8117f11fdfcba50edc8de537ea6019496785612e82ba7`
- Text SHA256: `d701ae3b59c0dc182993aabe230a5bf17e41f0ea11a438c6e211b6fdbf201975`


## Content

---
title: "How I found a simple bug in Facebook without any Test"
url: "https://medium.com/bugbountywriteup/how-i-found-a-simple-bug-in-facebook-without-any-test-3bc8cf5e2ca2"
authors: ["Sarmad Hassan (@JubaBaghdad)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization"]
publication_date: "2019-01-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5438
scraped_via: "browseros"
---

# How I found a simple bug in Facebook without any Test

How I found a simple bug in Facebook without any Test
Sarmad Hassan (Juba Baghdad)
Follow
2 min read
·
Jan 31, 2019

451

3

Hello Community, today I would like to talk about my easiest bug in Facebook and how I found it without any Test, so let’s jump in :)

In Aug 28, 2018, I was checking my News feed and suddenly I got this weird notification, see the below image:

It’s just a notification for an event for a closed group which was deleted

Why this notification is weird to me! o.k. let me explain to you:

The notification for the above event is related to a closed group.
I was an ex-member (Left the group) in that closed group, which means I can’t access to the group and can’t see the group contents.
So why the hell I got this notification from that group while I’m not a member in it anymore!!!
yeaaah :)

Within seconds I knew it’s a security bug see this link , at the same time some ideas came to my mind as below:

what about blocked users!!??
What if the event name changed and got deleted. is it possible to see the last update of event’s name!!?? after users got blocked or who left group!!??

After playing with my Test closed group I noticed below things:

Get Sarmad Hassan (Juba Baghdad)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

1- Blocked users and users who left the group can receive notification with last updated name of event.

2- It work in all kind of events (Accounts, pages, even workplace) not just in closed group.

I reported this directly to Facebook Security Team and they accepted it as valid bug, Thank you guys for the bounty :)

To the admin of IQDevs group, who ever you are, thank you for deleting that event because of you I found this bug ;)

Timeline:
Aug. 28, 2018 — Initial Report
Aug. 31, 2018 — Report Triaged
Dec. 19, 2018 — Bounty awarded
Jan. 31, 2019 — Bug Fixed
Jan. 31, 2019– Fixed confirmed

PoC Video:

Takeways:

1- Sometimes you don’t need Tools or F12 to find valid bugs :)

Thank you

Sarmad Hassan (JubaBaghdad)
