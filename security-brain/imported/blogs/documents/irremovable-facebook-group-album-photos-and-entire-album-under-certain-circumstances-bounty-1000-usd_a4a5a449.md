---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-14_irremovable-facebook-group-album-photos-and-entire-album-under-certain-circumsta.md
original_filename: 2021-01-14_irremovable-facebook-group-album-photos-and-entire-album-under-certain-circumsta.md
title: 'Irremovable Facebook group album photos and entire album under certain circumstances
  (Bounty: 1000 USD)'
category: documents
detected_topics:
- mobile-security
- command-injection
- business-logic
tags:
- imported
- documents
- mobile-security
- command-injection
- business-logic
language: en
raw_sha256: a4a5a449eaeeb48377a8a0ee8d46a3e663659d65b711c50b8426eb181db3dc67
text_sha256: 7c1602ac22ac355e60c5fd2b720230fcfc45c66d3b3a5fc46ecc51850b09619d
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Irremovable Facebook group album photos and entire album under certain circumstances (Bounty: 1000 USD)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-14_irremovable-facebook-group-album-photos-and-entire-album-under-certain-circumsta.md
- Source Type: markdown
- Detected Topics: mobile-security, command-injection, business-logic
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `a4a5a449eaeeb48377a8a0ee8d46a3e663659d65b711c50b8426eb181db3dc67`
- Text SHA256: `7c1602ac22ac355e60c5fd2b720230fcfc45c66d3b3a5fc46ecc51850b09619d`


## Content

---
title: "Irremovable Facebook group album photos and entire album under certain circumstances (Bounty: 1000 USD)"
page_title: "[WRITE-UP] Irremovable Facebook group album photos and entire album under certain circumstances (Bounty: 1000 USD) | by Shubham Bhamare | InfoSec Write-ups"
url: "https://theshubh77.medium.com/irremovable-facebook-group-album-photos-and-entire-album-under-certain-circumstances-bounty-1000-b1b2a870b8e0"
authors: ["Shubham Bhamare (@theshubh77)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw"]
bounty: "1,000"
publication_date: "2021-01-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3998
scraped_via: "browseros"
---

# Irremovable Facebook group album photos and entire album under certain circumstances (Bounty: 1000 USD)

[WRITE-UP] Irremovable Facebook group album photos and entire album under certain circumstances (Bounty: 1000 USD)
Shubham Bhamare
Follow
4 min read
·
Jan 14, 2021

344

Hi guys, it's Shubham Bhamare again. In this write-up, I'm going to tell you about one of my very simple Facebook bug which was found accidentally as I wasn't in the mood of testing at that time and was just browsing our business group on Facebook.

Due to this issue, Facebook group admin was unable to delete group album photos as well as entire album under certain circumstances.

So without wasting time, let's start! 👉

===

Setup and Scenario:

1) A Facebook group where only a page (ABC) is an admin.

2) An attacker (XYZ) is a Facebook user who's the member of above group.

Platform: Facebook Web

===

Reproduction steps:

1) From ABC's perspective, create an album in a group.

Creating an album in a group
Album created by ABC

2) From XYZ's perspective, add some photos to above album.

Press enter or click to view image in full size
Adding photos to the album
Press enter or click to view image in full size
Photo uploaded by group member (XYZ)

3) Now when ABC will try to delete that photos added by XYZ, there won't have any option to delete them. Even though ABC used other platforms like Android/iOS/Lite app, mobile site to delete that photos, it won't be possible.

Press enter or click to view image in full size
There's no option to delete a photo uploaded by group member

ABC will only be able to delete his/her own photos. Being an admin of the group, he should be able to delete photos added by other group members. But there wasn't have any option at that time when I reported this issue.

===

Get Shubham Bhamare’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Fix and Bypass:

Team fixed this issue by adding edit button on photos added by other group members. But when I was verifying the fix, I found that if group admin tried to delete entire album (if it includes photos of other members), he/she won't be able to delete it as it was showing an error message.

Press enter or click to view image in full size
Delete Album button
Showing an error message while deleting entire album

Impact behind this 2nd issue was, if malicious member added thousand of inappropriate photos to album, then group admin won't be able to delete that entire album. He/she'll have to delete every photo one by one.

Also we can imagine what will happen if multiple group members added thousand of inappropriate photos to that album. 😁

===

Bounty:

1000 USD (500 USD for initial report and 500 USD for bypassing the fix or for finding 2nd issue)

Press enter or click to view image in full size
1000 USD bounty awarded by Facebook

===

Timeline:

Apr 21, 2019: Report sent
Apr 24, 2019: Pre-triaged
Apr 27, 2019: Triaged
May 15, 2019: Fixed
May 16, 2019: Fix bypassed/2nd issue found
May 17, 2019: Fixed completely
May 17, 2019: 1000 USD bounty awarded

===

Takeaway(s):

1) While browsing something (even though you're not in the mood of hunting), always observe whether something's working as intended or not.

2) Don't reveal your findings until you fully believe that there won't be any bypass for it. 😉 Check another endpoints/features too for similar issues.

3) Sometimes you just need logical thinking instead of any advanced tools or knowledge. Because Logic == Magic. 😊

4) If you're new to Facebook bug bounty, try to find logical bugs the most.

===

Thank you for reading! Stay tuned for my next write-up, and don’t forget to follow me on Facebook, Twitter, LinkedIn, and Instagram. 😊

===

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!
