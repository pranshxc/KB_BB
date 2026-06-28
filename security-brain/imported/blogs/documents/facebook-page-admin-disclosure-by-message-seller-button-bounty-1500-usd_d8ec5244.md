---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-26_facebook-page-admin-disclosure-by-message-seller-button-bounty-1500-usd.md
original_filename: 2020-12-26_facebook-page-admin-disclosure-by-message-seller-button-bounty-1500-usd.md
title: 'Facebook page admin disclosure by ''Message Seller'' button (Bounty: 1500
  USD)'
category: documents
detected_topics:
- command-injection
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- command-injection
- automation-abuse
- information-disclosure
language: en
raw_sha256: d8ec52446bd4521a39a4bad11edd0bc43d95a4ff0aae3120ed75c251500d9b12
text_sha256: e3ffd199aa5a55b310ba2a3df83aff59898d713af680b0c002e097116b98064a
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook page admin disclosure by 'Message Seller' button (Bounty: 1500 USD)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-26_facebook-page-admin-disclosure-by-message-seller-button-bounty-1500-usd.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `d8ec52446bd4521a39a4bad11edd0bc43d95a4ff0aae3120ed75c251500d9b12`
- Text SHA256: `e3ffd199aa5a55b310ba2a3df83aff59898d713af680b0c002e097116b98064a`


## Content

---
title: "Facebook page admin disclosure by 'Message Seller' button (Bounty: 1500 USD)"
url: "https://theshubh77.medium.com/facebook-page-admin-disclosure-by-message-seller-button-bounty-1500-usd-caaa2eac4121"
authors: ["Shubham Bhamare (@theshubh77)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
bounty: "1,500"
publication_date: "2020-12-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4048
scraped_via: "browseros"
---

# Facebook page admin disclosure by "Message Seller" button (Bounty: 1500 USD)

Facebook page admin disclosure by "Message Seller" button (Bounty: 1500 USD)
This issue could have accidentally revealed the identity of the Facebook page admin under certain circumstances
Shubham Bhamare
Follow
3 min read
·
Dec 25, 2020

536

2

Hi guys, I’m Shubham Bhamare from Maharashtra, India. As I promised in my previous write-up, here’s my first Facebook bug bounty write-up. Finally! 😂

I know it’s too late to publish this write-up as this bug was found and rewarded in 2018. I’m extremely sorry for that. Anyways, I’m going to publish all my other findings too in the coming days.

So without wasting time, let's start! 👉

===

Description:

This issue could have accidentally revealed the identity of the Facebook page admin under certain circumstances.

On Facebook, page admin’s roles are secret. Disclosing the identity of the page admin may cause a significant privacy issue. In this case, it was possible to disclose the identity of the page admin under certain circumstances.

===

Setup:

2 Facebook users i.e. Shubham and John

1 Facebook page i.e. Shubham's Page

1 Facebook group i.e Shubham's Page Group

Platform: Facebook Web

===

Scenario:

As mentioned above, there are 2 Facebook users i.e. Shubham and John.

Shubham is the admin of Shubham's Page.

Shubham's Page is linked to Shubham's Page group which is a group for Shopping. Post approval for this group is turned on.

John is a member of said group.

Shubham hasn't made himself an admin of a group because he doesn't want to disclose his identity.

So now that group has only one admin i.e. Shubham's Page.

Shubham is just a member of that group and always acts as a page.

===

Reproduction steps:

1) From John's account, create a selling post in the group.

Press enter or click to view image in full size

2) Post will be sent to admin for approval.

Get Shubham Bhamare’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

3) Now from Shubham’s account (acting as a page), click on the "Message Seller" button at the bottom of the above unapproved post and send a message.

Press enter or click to view image in full size

4) Message will be sent from Shubham's personal profile instead of the page, which is unintended.

===

The logic behind it:

It’s easy for John to determine who’s the admin of the page as there’s only one group admin (Shubham’s Page) who can see that unapproved post.

===

Fix:

The team fixed this issue by removing the "Message Seller" button when acting as a page.

===

Bypass:

I found that fix was incomplete as this issue was still working on old unapproved posts.

===

Bounty:

1500 USD

Press enter or click to view image in full size

===

Timeline:

Sep 09, 2018: Report sent
Sep 11, 2018: Pre-triaged
Sep 12, 2018: Triaged
Oct 13, 2018: Fixed
Oct 13, 2018: Fix bypassed
Oct 23, 2018: Fixed completely
Nov 03, 2018: 1500 USD bounty awarded

===

Takeaway(s):

1) If you're new to Facebook bug bounty, try to find logical bugs the most.

2) Always try to find a bypass.

===

Thank you for reading! My next write-up will be about my second bug in Facebook (Bounty: 5000 USD). So stay tuned and don’t forget to follow me on Medium. 😊

===

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!
