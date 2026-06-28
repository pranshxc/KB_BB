---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-31_my-first-bug-report-at-facebook-2021.md
original_filename: 2021-03-31_my-first-bug-report-at-facebook-2021.md
title: My first Bug report at Facebook 2021
category: documents
detected_topics:
- access-control
- command-injection
- automation-abuse
- business-logic
tags:
- imported
- documents
- access-control
- command-injection
- automation-abuse
- business-logic
language: en
raw_sha256: 9c70b461bbd59163a6c73d952ef8320a0c8aa6c0b72c5279b7a71755dea777d5
text_sha256: 81a419132cc355391e860d245fb4dbf2042212da3dd6e8bdcc5a8dd5909db385
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# My first Bug report at Facebook 2021

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-31_my-first-bug-report-at-facebook-2021.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, automation-abuse, business-logic
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `9c70b461bbd59163a6c73d952ef8320a0c8aa6c0b72c5279b7a71755dea777d5`
- Text SHA256: `81a419132cc355391e860d245fb4dbf2042212da3dd6e8bdcc5a8dd5909db385`


## Content

---
title: "My first Bug report at Facebook 2021"
url: "https://medium.com/@Kntjrld/my-first-bug-report-at-facebook-2021-bab2c2373ee3"
authors: ["Kent Jarold Abulag (@wkemenhehehegsg)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw", "Broken authorization"]
publication_date: "2021-03-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3779
scraped_via: "browseros"
---

# My first Bug report at Facebook 2021

My first Bug report at Facebook 2021
Kent Jarold Abulag
Follow
2 min read
·
Mar 31, 2021

61

1

Press enter or click to view image in full size
Meta BBP

Sharing my story how I was rewarded $xxx from Facebook. I started hunting a bug this February 2021 when I see it to one member of group that he will be awarded by doing that things. But in actual hunting, I realized that It’s not easy like I think. I submit a reports in Bugcrowd and HackerOne but my reports is Informative and the one is duplicate. It’s not easy for beginners so I always reading write-ups and watching in Youtube. Until I read a write-ups of bug in Facebook and that’s it. For those who didn’t already know, Facebook can award you if you found a bug that may affects to Privacy of it’s user and award can be high if you will find a High risk bug.

Since I always deactivate my Facebook account and I always used only is the Messenger app, It brings me to my first bug bounty in Facebook. Through Facebook Messenger a deactivated Facebook account can able to send message to any Facebook user and Instagram user. In searching bugs in both application I found that if the Facebook is deactivated, Instagram user can't block it.

Title: Instagram User was Unable to Block deactivated Facebook account on cross-app communication
Steps to reproduce:

1. Deactivate your Facebook account and use Messenger application
2. Through Messenger send a message to any Instagram user except to Instagram account that connected to your Facebook account.
3. From Instagram app, you can send and receive a message from Deactivated Facebook account but you can’t block that Facebook account.

Get Kent Jarold Abulag’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

PoC link: https://youtu.be/et7yC6ENqRs

I have some tips for beginners or new to Facebook bug bounty program. This is based on my experienced.

1. Always update your application before you starts hunting.
2. If you know that you find a bug. Test it multiple times before doing a write-ups.
3. Always provide PoC even your bug is easy to reproduce.
4. Be nice to security team.

And last don't give up, I failed multiple times before I get my first bug bounty but I considered myself as lucky because 2 months in hunting bug and almost 1 month in Facebook bug bounty program is too soon for me to be awarded.

Edited:

Special thanks to Admin Rien/Rena of PHU IV and Pinoy Info Sec.

Timeline:

March 6, 2021 - Initial report
March 10, 2021 - Needs a PoC
March 11, 2021 - I sent PoC
March 17, 2021 - I conduct a test to different account and I sent again the 2nd PoC.
March 18, 2021 - Triaged
March 25, 2021 - Fixed
March 31, 2021 - Bounty awarded
