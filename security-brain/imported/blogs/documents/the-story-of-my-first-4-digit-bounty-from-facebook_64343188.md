---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-17_the-story-of-my-first-4-digit-bounty-from-facebook.md
original_filename: 2020-07-17_the-story-of-my-first-4-digit-bounty-from-facebook.md
title: The Story of My first 4 digit bounty from Facebook
category: documents
detected_topics:
- command-injection
- information-disclosure
- business-logic
tags:
- imported
- documents
- command-injection
- information-disclosure
- business-logic
language: en
raw_sha256: 643431887849c588d988395c4ee70d12d5b116f8ad6c5bc37a588b07ebf3c529
text_sha256: e3334859bbc3568760ea004f845b37cc2b2eddb28c5b2cb1ad897acc0e873663
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# The Story of My first 4 digit bounty from Facebook

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-17_the-story-of-my-first-4-digit-bounty-from-facebook.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, business-logic
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `643431887849c588d988395c4ee70d12d5b116f8ad6c5bc37a588b07ebf3c529`
- Text SHA256: `e3334859bbc3568760ea004f845b37cc2b2eddb28c5b2cb1ad897acc0e873663`


## Content

---
title: "The Story of My first 4 digit bounty from Facebook"
url: "https://medium.com/@sudipshah_66336/the-story-of-my-first-4-digit-bounty-from-facebook-3a29830e03cd"
authors: ["Sudip Shah"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw", "Information disclosure"]
publication_date: "2020-07-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4405
scraped_via: "browseros"
---

# The Story of My first 4 digit bounty from Facebook

The Story of My first 4 digit bounty from Facebook
Sudip Shah
Follow
2 min read
·
Jul 17, 2020

462

1

Luckily , I managed somehow (After a lot of frustrations of not able to find any valid bugs after the 1st one ) to find a bug in Facebook Lite app which would easily Disclose the admin_id of any page .

I was just trying to test each and every function that the FBLite app have and I found one suspicious behaviour which leads to Page Admin Disclosure. It is fixed currently so I’m disclosing it publicly .

I will write the description and steps to reproduce that I sent to facebook now :

Description : When the page messages a fan/follower of the page then the messages are sent through page’s id which is the normal behaviour . Now I found a bug that when the page admin goes to his page inbox in fblite and then send a photo to any fans/follower of the page , then the photo is sent through page’s admin’s personal profile id instead of page id . This bug is leading to Page admin disclosure.

Steps :
1. User A goes to his PageX’s inbox through fblite and sees UserB’s message thread
2. UserA messages to User B
3.User B receives the text message done by UserA through page’s id
4. UserA now sends photo to UserB through the page inbox.
5. UserB receives the photo message through UserA’s personal profile id instead of the page id which leads to page admin disclosure.

POC is here : https://drive.google.com/file/d/1F9tkf1AU33vTsrk_PE09lLmU13wB89uD/view?fbclid=IwAR2fuYeh80vFu9nfvPINdvyjh_ER9pjqO267nPW5OhgqB-KhCWhOz0H8fCQ

Timeline:

Report Submitted : June 25, 2020

Pre-triage : June 29, 2020

Get Sudip Shah’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Triaged : June 29, 2020

Confirmation of Fix : July 7, 2020

Finally Reward awarded : July 16 , 2020

The flaw in the sending photo feature through FBLite made me find this bug without using any tools . I’m very grateful to facebook for rewarding me with a nice bounty amount for this logical bug .

I don’t know how to express my happiness about my first 4 digit bounty in Facebook . I was really very happy when I received this bounty notification . I was like :

I still have a lot to learn in this journey of bug hunting and this motivated me to keep continuing the journey . :)

Thanks a lot to everyone and very special thanks to our beloved Ashok dai .

#BugBounty

Follow Infosec Writeups for more.
