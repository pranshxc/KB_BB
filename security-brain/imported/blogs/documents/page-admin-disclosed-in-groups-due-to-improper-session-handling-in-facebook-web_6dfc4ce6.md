---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-04_page-admin-disclosed-in-groups-due-to-improper-session-handling-in-facebook-web.md
original_filename: 2021-02-04_page-admin-disclosed-in-groups-due-to-improper-session-handling-in-facebook-web.md
title: Page Admin Disclosed In Groups Due To Improper Session Handling In Facebook
  Web
category: documents
detected_topics:
- command-injection
- automation-abuse
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- information-disclosure
- api-security
language: en
raw_sha256: 6dfc4ce684beb65303cd8966e3f97ada9214d7fecd9f3fe87835f3d535a66a78
text_sha256: e4c57288c296d666062e6a3031f608e4383145225e6e0252f441f8d298380f67
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Page Admin Disclosed In Groups Due To Improper Session Handling In Facebook Web

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-04_page-admin-disclosed-in-groups-due-to-improper-session-handling-in-facebook-web.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `6dfc4ce684beb65303cd8966e3f97ada9214d7fecd9f3fe87835f3d535a66a78`
- Text SHA256: `e4c57288c296d666062e6a3031f608e4383145225e6e0252f441f8d298380f67`


## Content

---
title: "Page Admin Disclosed In Groups Due To Improper Session Handling In Facebook Web"
url: "https://medium.com/bugbountywriteup/page-admin-disclosed-in-groups-due-to-bad-session-handling-in-facebook-web-184514fafff9"
authors: ["Samip Aryal (@samiparyal_)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
publication_date: "2021-02-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3935
scraped_via: "browseros"
---

# Page Admin Disclosed In Groups Due To Improper Session Handling In Facebook Web

Page Admin Disclosed In Groups Due To Improper Session Handling In Facebook Web + FB4A [$xxx+$xxxx]
Samip Aryal
Follow
4 min read
·
Feb 4, 2021

162

2

…

This quick writeup is about a vulnerability in Facebook that could have revealed Admins of ex-page_members of a Facebook group when adding a poll option.

…

A group can be joined by profiles as well as pages independently. Now, after a page gets removed from a group; it can no longer interact fully with the group posts from others. However, it can seemingly interact lightly with its previous interactions like deleting comments, undoing like, etc.

Here, while I was testing this idea initially on FB4A, Interestingly; I found that it can also add poll options to the poll post that it made during membership even after being a non-member at the present. After adding poll options, the polls were added to the post with the page’s name. It was intended. But, when I moved to the Facebook web, I found that when adding poll options as the non-member, the poll options were being added from the admin’s personal profile which was never a part of the group (was never a member).

Why is this an issue?
-> Because; due to this behavior he is being revealed as the admin of the page who made the poll post.

How group members can be sure that the profile which added the poll option is surely an admin of the page?
-> Because no other non-members are allowed to add a poll option to poll_post in a group. If a poll option gets added to a poll_post by a non-member profile; that clearly means that he is the admin of the page that made the poll_post.

…

REPRODUCTION STEPS IN A NUTSHELL

FBDL Code

Or, you can see the POC Video HERE.

…

Timeline for the report thread

Reported — Tuesday, 29 December 2020

Pre-Triaged — Monday, 4 January 2021

Triaged — Tuesday, 5 January 2021

Fixed & Fixed confirmed — Wednesday, 13 January 2021

Bounty Rewarded — Monday, 1 February 2021

FBDL bonus provided — Monday, 1 February 2021

[EDIT] Bypass Achieved — June 2021 (See at the bottom for bypass info)

…

Bounty Reward ($XXX) Message From Facebook

Facebook fixed this issue by removing the option to add polls in the poll_post after being a non-member.

Get Samip Aryal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

…

(EDIT 2021–05)

So, here something funny happened;

Earlier I had also posted something like this at the end of this report initially.

You missed it lol

→ So, this had remained up to several months with this report. But, it seems like no one actually tried this one out. As a result, I myself returned to this report some days ago and was able to achieve this exact thing I was describing as an opportunity.

So, I noticed that; if a page is one of the admins of the group, then the page was able to make the poll post in any event of the group unlike it being as a normal member.

This was the point I was missing out earlier as I was only trying to make a poll post using a normal page member. But yeah, this time I tried to perform it using a page member with admin rights of the group and it got successful. I was able to achieve the same admin disclosure vulnerability as above but this time additionally combined with a voice indication failure vulnerability as mentioned here at the last point. As a result, Facebook rewarded me once again with an even better bounty : )

Second One

You can see the POC video of this one ((here)).

…

So, yeah one takeaway from this is; don’t hesitate to grab the opportunity that is given to you : ))

…

Thank you for reading this writeup about a simple vulnerability. If you have any suggestions/queries, I’m available on Facebook/ Instagram.

….
