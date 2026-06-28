---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-06_irremovable-guest-in-facebook-event-facebook-bug-bounty.md
original_filename: 2022-08-06_irremovable-guest-in-facebook-event-facebook-bug-bounty.md
title: Irremovable guest in facebook event — Facebook bug bounty
category: documents
detected_topics:
- command-injection
- business-logic
tags:
- imported
- documents
- command-injection
- business-logic
language: en
raw_sha256: f1e56442a8f8de26ecbd81d21158f0df23f07ab223d771d003d156de4e4d0866
text_sha256: 3d0bbbc869224a2d1a66d2ce52aa4599163bbd66f5d85bf6808e411fa2bbb9a7
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Irremovable guest in facebook event — Facebook bug bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-06_irremovable-guest-in-facebook-event-facebook-bug-bounty.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `f1e56442a8f8de26ecbd81d21158f0df23f07ab223d771d003d156de4e4d0866`
- Text SHA256: `3d0bbbc869224a2d1a66d2ce52aa4599163bbd66f5d85bf6808e411fa2bbb9a7`


## Content

---
title: "Irremovable guest in facebook event — Facebook bug bounty"
url: "https://medium.com/@rajeevgyawali92/irremovable-guest-in-facebook-event-facebook-bug-bounty-e10e03c98cd5"
authors: ["Rajiv Gyawali (@rajiv_gyawali)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw"]
publication_date: "2022-08-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2359
scraped_via: "browseros"
---

# Irremovable guest in facebook event — Facebook bug bounty

Rajiv Gyawali
 highlighted

Irremovable guest in facebook event — Facebook(Meta) bug bounty
Rajiv Gyawali
Follow
2 min read
·
Aug 5, 2022

57

1

Hello Everyone, This is Rajiv Gyawali from Butwal, Nepal. This is a story of one of my finding on facebook.

Story : I was reading writeups of facebook bug bounty and came to a writeup which was about being unable to remove member from facebook event, The circumstances were “Invited user blocks owner of event”, I tested the same scenario at first but couldn’t reproduce it, Later i went to one of my test group and created an event in normal scenario(I thought it to be a normal scenario at first), and tried to remove a member from that event, i was unable to remove that member from group, I became happy with the thought like…ohhhhh buggy…thing :)

I tested that issue in several groups, There comes some disappointment, I was unable to reproduce it in some groups, i was very unsure whether to report that issue or not as there was a risk of fb team not reproducing it, i reported it anyway.

As expected, facebook team could not reproduce the issue, i myself was confused about the reproduction scenario of bug(So that was fair reply from facebook security :D), I again started testing for that issue from zero level, And…finally figured out the scenario required for the reproduction of issue…. Big relief :P :P

Actually, To reproduce that issue following Scenario was required :

When the owner of an event is a member of a group along with his facebook page, he can’t remove guest from an event.

So, I sent them with the additional information required to reproduce the issue, and they were able to reproduce the issue (PoC : https://youtu.be/MhC97tJxk0Q )

Get Rajiv Gyawali’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Timeline :

Report sent — 17th Sep 2021

Initial response from facebook — 22 September 2021 (Unable to reproduce)

Sent with additional info and scenario — 23rd September 2021

Reproduced — 24th September 2021

Triaged — 29th September 2021

Bounty Rewarded — 7th October 2021

Fixed and Confirmed — 21th November

This issue however was still reproducible in FB4A, may exist even now, but facebook team said they don’t accept this sort of issues in FB4A.

Thank you for reading to the end, Let’s get connected here Rajiv Gyawali

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 Github Repos and tools, and 1 job alert for FREE!
