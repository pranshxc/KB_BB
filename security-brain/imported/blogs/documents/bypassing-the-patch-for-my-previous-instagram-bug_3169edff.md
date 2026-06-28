---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-18_bypassing-the-patch-for-my-previous-instagram-bug.md
original_filename: 2019-11-18_bypassing-the-patch-for-my-previous-instagram-bug.md
title: Bypassing the patch for my previous Instagram bug.
category: documents
detected_topics:
- sso
- access-control
- command-injection
- business-logic
- api-security
tags:
- imported
- documents
- sso
- access-control
- command-injection
- business-logic
- api-security
language: en
raw_sha256: 3169edff3c60fbb7bd7b704221cac24c03c551fad952cfadd226b5b3e7b95f75
text_sha256: b9909bcdc8655a3bf9cb46ab585e4f3581d5e4ae065095285cb914301ec6131c
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing the patch for my previous Instagram bug.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-18_bypassing-the-patch-for-my-previous-instagram-bug.md
- Source Type: markdown
- Detected Topics: sso, access-control, command-injection, business-logic, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `3169edff3c60fbb7bd7b704221cac24c03c551fad952cfadd226b5b3e7b95f75`
- Text SHA256: `b9909bcdc8655a3bf9cb46ab585e4f3581d5e4ae065095285cb914301ec6131c`


## Content

---
title: "Bypassing the patch for my previous Instagram bug."
url: "https://medium.com/bugbountywriteup/bypassing-the-fix-of-my-previous-instagram-bug-49ece4ea7e1d"
authors: ["Baibhav Anand (@SpongeBhav)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization", "Logic flaw"]
publication_date: "2019-11-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4937
scraped_via: "browseros"
---

# Bypassing the patch for my previous Instagram bug.

Bypassing the patch for my previous Instagram bug.
Baibhav Anand
Follow
3 min read
·
Nov 18, 2019

318

Press enter or click to view image in full size

Hello readers! In this article I will be sharing with you how I was able to get bounty twice with a single simple logic flaw breaking Instagram story with a single simple logic flaw breaking Instagram story restriction.

Get Baibhav Anand’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The bug was in Instagram stories, what exactly I could do was I could reply to Instagram stories even when the account owner had set the privacy of Allow message replies to "off".

Here are the details steps of reproduction for my first bug:
Firstly what I would do was open the Instagram story of which replies were disabled.
Now while I am in the story, from a different phone I would send myself a WhatsApp message to get my keyboard popup during the story. (This step could be done by various other ways too)
Now as soon as the keyboard pops up during the story, what I noticed was there was a reply box in the particular story.
Now that there is a reply box, I could reply to the story with ease.

The way Facebook fixed this bug was that they no longer allowed the reply button to show up when the keyboard popped up during a story with replies disabled and they awarded me with a 3digit bounty.

Now how actually did I manage to bypass this fix?

Since this was a just a UI based fix, a part of me knew this was still vulnerable and all I had to do was to find a way to pop up the keyboard again and get the reply button to show up again. I tried various ways but none of them seemed to work until I did this:

Opening the previous story on which replies were enabled so that the next story that will automatically show up would be the one with replies disabled.
Now I would pop up the keyboard in that previous story and let the keyboard be on until the story would pass and the next story with replies disabled would show up.
Now that my keyboard was already on and the story lead to the one with replies disabled, my keyboard would still be on and there was a reply button.
Now that there was a reply option I could reply to the story again.

Now this time they implemented a server side fix that even if someone managed to reply to an Instagram story with replies disabled he/she will get an error that the message wasn’t sent. This time they awarded me with a 4digit bounty.

Lesson to learn:
When your bug gets fixed try to bypass the fix and check if the fix was a complete fix, sometimes the security guys can be lazy to implement a complete fix from every aspect that the bug could be reproduced.

Thank you for making it to the end of this article.

Leave me a follow: https://www.twitter.com/spongebhav

Follow Infosec Write-ups for more such awesome write-ups.

InfoSec Write-ups
A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub…

medium.com
