---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-14_tale-of-2-tootb-bugs-google-and-whatsapp.md
original_filename: 2021-01-14_tale-of-2-tootb-bugs-google-and-whatsapp.md
title: 'Tale of 2 TOOTB Bugs: Google and WhatsApp'
category: documents
detected_topics:
- command-injection
- automation-abuse
- information-disclosure
- business-logic
- api-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- information-disclosure
- business-logic
- api-security
language: en
raw_sha256: 266fc992c8ff5c8c884bda61ad783529aba005afeba1597c9c51e073d9437c18
text_sha256: 21b8f18bc30f207edbf7bef84f505e0433b7a73d7a92f6d057bb17b21aeedb9f
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Tale of 2 TOOTB Bugs: Google and WhatsApp

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-14_tale-of-2-tootb-bugs-google-and-whatsapp.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, information-disclosure, business-logic, api-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `266fc992c8ff5c8c884bda61ad783529aba005afeba1597c9c51e073d9437c18`
- Text SHA256: `21b8f18bc30f207edbf7bef84f505e0433b7a73d7a92f6d057bb17b21aeedb9f`


## Content

---
title: "Tale of 2 TOOTB Bugs: Google and WhatsApp"
url: "https://medium.com/bug-bounty-hunting/tale-of-2-tootb-bugs-google-and-whatsapp-3c0ad40d604c"
authors: ["Circle Ninja (@circleninja)"]
programs: ["Google", "Meta / Facebook"]
bugs: ["Information disclosure", "Logic flaw"]
publication_date: "2021-01-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3999
scraped_via: "browseros"
---

# Tale of 2 TOOTB Bugs: Google and WhatsApp

Tale of 2 TOOTB Bugs: Google and WhatsApp
Ronnie Joseph
2 min read
·
Jan 14, 2021

--

Press enter or click to view image in full size

First of all, with TOOTB , I meant “think out of the box”. Don’t get confused haha.

Also lets keep all writeups from now on simple and short shall we? Or you like the stories also which I made long back!!

WHATSAPP:

Recently it had some privacy policy changes, so just thought i should just post about this then anyways.

Bug: Shadow viewing another users’ status updates while having set your read receipt ”disabled”. (In some cases.)

According to the app’s usage, switching off the Read Receipts for messages does not let you know if the person has read your message or not, you will also not be able to see who all have checked your status.

Bypass:

There is a section for already viewed updates in whatsapp.
Just on top of that you can see the section for new status.
Click on the top of already viewed status and keep pressing with you finger . (don’t tap, hold it.)
While keeping fingers touched, swipe over to left side and don’t lift your fingers.
In that way we are able to see the status of section in “Unseen status updates. “ but only of the bottom person of that section. (I mean unseen status just above the section of already viewed updates. )
Also you can’t view a video status of a user as in that cases you have to lift finger for that video to play .
So the glitch works perfect in every case of all status updates just above the already seen section, but with either text or images.

I know its a bit hard to get without a poc but I don’t carry much time for that. Sorry :(

Get Ronnie Joseph’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Reported around 6 months back.

Still unfixed as the bug doesn’t match the minimum monetary standards which I do agree. But a bug is a bug. ;)

YouTube:

Bug: ABILITY TO VIEW AGE RESTRICTED VIDEOS ON YT WITHOUT SIGNING IN .

I had reported it around a year back, and got reply that it is know internally blah blah. This was not fixed for many months until recently when i check it has been fixed.

Suppose https://www.youtube.com/watch?v=xzy is a age restricted video on youtube.
Simply create this url https://www.youtube.com/embed/xzy and you will be able to view the video without doing all the usual sign in or changing your age in google account lol.

So that was tale of two quick finds.

Tale of 2 TOOTB Bugs: Google and WhatsApp by @CircleNinja https://link.medium.com/X3H4yOQz2cb

If you appreciate it and would like to encourage me to write more , pls do share on twitter and tag me, it gives me motivation otherwise, I will become a lazy ass haha.
