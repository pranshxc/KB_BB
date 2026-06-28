---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-21_how-i-made-my-first-from-finding-a-bug-in-facebook.md
original_filename: 2019-08-21_how-i-made-my-first-from-finding-a-bug-in-facebook.md
title: How I made my first $$$ from finding a bug in Facebook
category: documents
detected_topics:
- access-control
- command-injection
- mobile-security
tags:
- imported
- documents
- access-control
- command-injection
- mobile-security
language: en
raw_sha256: f004f5dc19c2a91e5a7a783842adb4ed134027c4807b024210103a442693f0d0
text_sha256: 8896e477f6e6fe790b40ce4bfd11547a6923eb65da3dc53c54ec576970eebb88
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# How I made my first $$$ from finding a bug in Facebook

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-21_how-i-made-my-first-from-finding-a-bug-in-facebook.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `f004f5dc19c2a91e5a7a783842adb4ed134027c4807b024210103a442693f0d0`
- Text SHA256: `8896e477f6e6fe790b40ce4bfd11547a6923eb65da3dc53c54ec576970eebb88`


## Content

---
title: "How I made my first $$$ from finding a bug in Facebook"
page_title: "How I Made My First $$$ by Finding a Bug in Facebook | by Aayush Pokhrel | Medium"
url: "https://medium.com/@aayushpokhrel/how-i-made-my-first-from-finding-a-bug-in-facebook-da3b11e550f0"
authors: ["Aayush Pokhrel (@aayushpok)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization"]
publication_date: "2019-08-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5071
scraped_via: "browseros"
---

# How I made my first $$$ from finding a bug in Facebook

How I Made My First $$$ by Finding a Bug in Facebook
Aayush Pokhrel
Follow
2 min read
·
Aug 21, 2019

304

5

One day, I decided to hunt for bugs in Facebook and chose the Facebook Lite application for testing. After a few hours, I discovered a small issue: admins couldn’t delete conversations with users who had messaged their page.

At first, I thought this wasn’t a security bug. But then I realized it was a privacy issue — since admins and users could discuss private matters on a page, the inability to delete these conversations posed a potential risk.

Get Aayush Pokhrel’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Understanding the impact, I reported the issue to Facebook, and fortunately, I was rewarded for my findings! 🎉”

Vulnerability Type: Privacy / Authorization
Product Area: Android (Facebook Lite)
Title: “Admins Can’t Delete User Conversations on Facebook Lite Pages”
Vulnerability Description:

In Facebook Lite, page admins are unable to delete conversations with users who message their page. This prevents admins from removing potentially sensitive discussions, leading to a privacy risk.

Impact of the Vulnerability:

Privacy is a crucial aspect of any communication platform. Since admins and users may exchange private or sensitive information, the inability to delete conversations could pose a privacy risk for page administrators.

Steps to Reproduce:
Login as User A (a normal user) on one device.
Login as User B (a page admin) on another device using Facebook Lite.
User A sends a message to User B (page admin).
User B receives a notification in Facebook Lite.
User B opens the chat and attempts to delete the conversation, but an error appears, preventing deletion.
Status: Reported & Rewarded 🎉

#Happy_Hacking 🚀

Timeline:
Initial Report: July 12, 2019
Reproduced: July 16, 2019
Triaged: July 17, 2019
Fixed: July 29, 2019
Fix Confirmed: July 29, 2019
Awarded ($$$): August 15, 2019 🎉

#Happy_Hacking 🚀
