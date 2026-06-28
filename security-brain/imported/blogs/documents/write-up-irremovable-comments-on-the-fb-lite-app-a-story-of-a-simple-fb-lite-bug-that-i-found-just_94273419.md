---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-02_write-up-irremovable-comments-on-the-fb-lite-app-a-story-of-a-simple-fb-lite-bug.md
original_filename: 2022-12-02_write-up-irremovable-comments-on-the-fb-lite-app-a-story-of-a-simple-fb-lite-bug.md
title: '[WRITE-UP] Irremovable comments on the FB Lite app | A story of a simple FB
  Lite bug that I found just by observation (Bounty: 500 USD)'
category: documents
detected_topics:
- mobile-security
- command-injection
- business-logic
- api-security
tags:
- imported
- documents
- mobile-security
- command-injection
- business-logic
- api-security
language: en
raw_sha256: 9427341918284830e2c69c120efa16d7846d0d134a8d5d327ae2ac36cb9aa0bf
text_sha256: 8465a155207d6410da257787362cd7dceb9608b1cbc8d8792676e15745da86f3
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# [WRITE-UP] Irremovable comments on the FB Lite app | A story of a simple FB Lite bug that I found just by observation (Bounty: 500 USD)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-02_write-up-irremovable-comments-on-the-fb-lite-app-a-story-of-a-simple-fb-lite-bug.md
- Source Type: markdown
- Detected Topics: mobile-security, command-injection, business-logic, api-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `9427341918284830e2c69c120efa16d7846d0d134a8d5d327ae2ac36cb9aa0bf`
- Text SHA256: `8465a155207d6410da257787362cd7dceb9608b1cbc8d8792676e15745da86f3`


## Content

---
title: "[WRITE-UP] Irremovable comments on the FB Lite app | A story of a simple FB Lite bug that I found just by observation (Bounty: 500 USD)"
url: "https://theshubh77.medium.com/write-up-irremovable-comments-on-fb-lite-app-a-story-of-a-simple-fb-lite-bug-that-i-found-just-125aaa826dd8"
authors: ["Shubham Bhamare (@theshubh77)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw"]
bounty: "500"
publication_date: "2022-12-02"
added_date: "2022-12-05"
source: "pentester.land/writeups.json"
original_index: 1828
scraped_via: "browseros"
---

# [WRITE-UP] Irremovable comments on the FB Lite app | A story of a simple FB Lite bug that I found just by observation (Bounty: 500 USD)

Irremovable comments on the FB Lite app | A story of a simple FB Lite bug that I found just by observation (Bounty: 500 USD)
Shubham Bhamare
Follow
4 min read
·
Dec 2, 2022

475

1

Hi guys, I’m Shubham Bhamare again. In this write-up, I’m going to tell you how I found a simple FB Lite bug that restricted FB Lite app users from deleting comments under certain circumstances. This was an easy finding because it was found just by observation. (Just like my previous finding of 5000 USD, where I was able to add any unowned phone number to my Facebook account.)

So without wasting time, let’s start! 👉

===

Description:

FYI, let me clarify that when I reported this issue, Facebook (now Meta) used to consider those bugs too where users were unable to perform certain actions through the FB Lite app but were able to perform through other platforms like Facebook Web, Facebook for Android/iOS, etc. This is because users with low bandwidth and storage were unable to use the other platforms mentioned above.

I don’t know if Facebook still accepts these types of bugs as I’m not hunting for bugs nowadays. Please confirm in the comments section if you have recently got a bounty for the same bug.

===

The story:

Chapter 1: I still remember when I reported this issue, it was the 1st day of August and a rainy afternoon. I was lying on the bed after lunch and scrolling through my old Facebook posts using the FB Lite app. Suddenly, I came across an old post of mine on which I had commented twice with the same word. So I tried to delete that comment but the app threw an error saying “We can’t process this request at the moment. Please try a bit later!”

I tried to delete my other comments but they too didn’t get deleted. After that, I tried to delete other people’s comments on my old posts but it threw the same error. I thought it was because I haven't updated the FB Lite app so I quickly updated it and tried to delete those comments again. But still, I wasn’t able to delete them.

It was a eureka moment for me as it was something unintended. I quickly recorded a video PoC demonstrating this bug and reported it to Facebook.

Chapter 2: On the same day, Facebook replied and requested additional information such as Post ID, FB Lite version, Device information, etc. as they were unable to reproduce this issue.

So I created a test post to send its ID to the team and commented on it and tried to delete that comment. But this time comment got deleted successfully. I felt sad assuming that my reported bug is nothing but a false positive. Now I tried to delete old comments and this time it threw the same error.

It was weird. I tested it further and found that only old comments that were made in the year 2013 or prior were affected by this issue. Added this additional information to the report and after some follow-ups, the team was able to reproduce this issue.

Get Shubham Bhamare’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

===

Timeline:

Aug 01, 2019: Report sent

Aug 01, 2019: Additional information requested by Facebook

Aug 02, 2019 — Aug 16, 2019: Follow-ups

Aug 23, 2019: Triaged

Oct 25, 2019: 500 USD bounty awarded

Press enter or click to view image in full size

Feb 07, 2020: Fixed completely

===

Takeaway(s):

While browsing something (even though you’re not in the mood of hunting bugs), always observe whether something’s working as intended or not.
If you are new to the Facebook bug bounty, then these types of FB Lite bugs are low-hanging fruit for you. Just observe, apply your logic and grab them.
Some bugs may be time and account specific

===

Thank you for reading! Stay tuned for my next write-up, and don’t forget to follow me on Facebook, Twitter, LinkedIn, and Instagram. 😊

===

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!
