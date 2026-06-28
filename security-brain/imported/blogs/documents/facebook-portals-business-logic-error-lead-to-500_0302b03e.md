---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-30_facebook-portals-business-logic-error-lead-to-500.md
original_filename: 2022-06-30_facebook-portals-business-logic-error-lead-to-500.md
title: Facebook Portal’s business logic error lead to 500$
category: documents
detected_topics:
- business-logic
- mobile-security
- access-control
- command-injection
tags:
- imported
- documents
- business-logic
- mobile-security
- access-control
- command-injection
language: en
raw_sha256: 0302b03eeb6b915a39579adf5d82446799527b99d5421657d6aa4fde930bb1a7
text_sha256: b65c90e2634e8dae1d54df48920468411fe80d9a8f171302c2a3dc3a9aef9220
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook Portal’s business logic error lead to 500$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-30_facebook-portals-business-logic-error-lead-to-500.md
- Source Type: markdown
- Detected Topics: business-logic, mobile-security, access-control, command-injection
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `0302b03eeb6b915a39579adf5d82446799527b99d5421657d6aa4fde930bb1a7`
- Text SHA256: `b65c90e2634e8dae1d54df48920468411fe80d9a8f171302c2a3dc3a9aef9220`


## Content

---
title: "Facebook Portal’s business logic error lead to 500$"
url: "https://medium.com/@unurbayar1998/facebook-portals-business-logic-error-lead-to-500-708e91b4055f"
authors: ["unurbayar amarsaikhan (@0xunuruu)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw", "Broken authorization"]
bounty: "500"
publication_date: "2022-06-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2495
scraped_via: "browseros"
---

# Facebook Portal’s business logic error lead to 500$

Facebook Portal’s business logic error lead to 500$
unurbayar amarsaikhan
Follow
3 min read
·
Jun 30, 2022

83

1

Introduction

Hello everybody, I’m Unurbayar. This bug is my first valid bug in Facebook.

I had sent +50 reports to the Facebook across 3 accounts. Sadly :( all of my reports closed as informative, not-applicable, duplicate. So it made me crazy and I was much disappointed myself. But finally after almost 1 year I’ve found a valid bug Facebook Portal.

Press enter or click to view image in full size

First of all I want to thank to 
Abhishek Pathak
 sharing his findings. He shared https://medium.com/@pathleax/this-is-how-i-was-able-to-see-and-delete-your-private-facebook-portal-photos-a93ed22f875b write-up and it certainly helped me to get a bounty. Because by reading his write-up I’ve discovered Facebook Portal Android application that lead to me find a bug.

About Facebook Portal

Facebook Portal is a multi functional app mainly designed for Portal devices which helps to make calls, create/share albums and photos to connected Portal devices, although it works without a Portal device too.

Story

When 
Abhishek Pathak
 write-up was released in 2021-December, I’ve checked Facebook Portal Android application and it seemed to have less functionality and features than other Facebook products. So I thought it was not exploitable anymore.

But in 2022-April, I was hunting Facebook and checked Facebook Portal Android application again. So no bug were found and I went for a bed.

While lying on bed, I thought that how Facebook account block feature would work between accounts in Facebook Portal. It was late night so checked block account feature tomorrow.

Amazingly, Facebook Portal had not implemented account block feature properly.

Here is what I did

2 accounts were created, they are friends. In Facebook Portal first account will create album and upload some photos. After doing that first account will share his album to second account in Facebook Portal. Consequently second account will block first account in Facebook.

By blocking, first account would not able to remove and see second account from his album. Moreover second account was able to see new uploaded photos and upload new photos in album.

PoC
Description

In Portal mobile app users create album and become admin of album, add their friends to album.
When their friends block admin of album in facebook, admin of album can not see and remove their friends.
Furthermore, their friends can access new uploaded pictures and upload new pictures.

Repro Steps

Users: [UserA, UserB; UserA is friends with UserB]

Get unurbayar amarsaikhan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Environment: [AlbumOne with owner UserA in Portal]

Browser: [n/a]

OS: [Android]

UserA create AlbumOne.
2.UserA upload picture to AlbumOne
3.UserA add UserB to AlbumOne
4.UserB block UserA
5.UserA can not see and remove UserB
6.UserA upload new picture to AlbumOne
7.UserB access AlbumOne
8.UserB see new picture
9.UserB upload picture to AlbumOne

Impact

Admin can not remove and see their friends.
Their friends can access album & upload new pictures.

Timeline

2022/04/18 — Report Submitted

2022/04/21 —Acknowledged by Facebook

2022/04/25 — Asked for update

2022/05/01 — Asked for update

2022/05/04 — Needs more info

2022/05/04 — Provided another PoC

2022/05/06 — More investigation

2022/05/11 — Asked for update

2022/05/12 — Asked for update

2022/05/16 — Asked for update

2022/05/17 — Bounty Rewarded 500$

2022/06/09 — Fixed

2022/06/09 — Fix confirmed by me
