---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-28_facebook-page-admin-disclosure-by-create-doc-button-bounty-5000-usd.md
original_filename: 2020-12-28_facebook-page-admin-disclosure-by-create-doc-button-bounty-5000-usd.md
title: 'Facebook page admin disclosure by ''Create doc'' button (Bounty: 5000 USD)'
category: documents
detected_topics:
- command-injection
- information-disclosure
tags:
- imported
- documents
- command-injection
- information-disclosure
language: en
raw_sha256: 3a4066b3629454f55216d23ebaffbeca1f8d64ce27b65ef0c53bec8357bb3ebf
text_sha256: 3a09bc5b7198139bac609cb8c0739e2ffcc263c02f9bcfc71ba9fcd38a4ecf10
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook page admin disclosure by 'Create doc' button (Bounty: 5000 USD)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-28_facebook-page-admin-disclosure-by-create-doc-button-bounty-5000-usd.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `3a4066b3629454f55216d23ebaffbeca1f8d64ce27b65ef0c53bec8357bb3ebf`
- Text SHA256: `3a09bc5b7198139bac609cb8c0739e2ffcc263c02f9bcfc71ba9fcd38a4ecf10`


## Content

---
title: "Facebook page admin disclosure by 'Create doc' button (Bounty: 5000 USD)"
url: "https://theshubh77.medium.com/facebook-page-admin-disclosure-by-create-doc-button-bounty-5000-usd-2fd1ff615bf8"
authors: ["Shubham Bhamare (@theshubh77)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
bounty: "5,000"
publication_date: "2020-12-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4043
scraped_via: "browseros"
---

# Facebook page admin disclosure by "Create doc" button (Bounty: 5000 USD)

Facebook page admin disclosure by "Create doc" button (Bounty: 5000 USD)
This issue could have accidentally revealed the identity of the Facebook page admin by the “Create doc” button
Shubham Bhamare
Follow
4 min read
·
Dec 29, 2020

673

5

Press enter or click to view image in full size

Hi guys, it's Shubham Bhamare again. In this write-up, I'm going to tell you about my 2nd valid bug that I found on Facebook. This issue could have accidentally revealed the identity of the Facebook page admin by the "Create doc" button. This is one of the very special findings for me because the bounty I received for this report was beyond my expectations. 😃

So without wasting time, let's start! 👉

===

Setup and Scenario:

1) A Facebook user Sarah is the admin of Sarah's Page.

2) Sarah's Page is linked to Sarah's Group.

3) Sarah hasn't made herself an admin of the group because she doesn't want to disclose her identity.

4) So now it's clear that Sarah's Group has only one admin i.e. Sarah's Page. Sarah is just a member of that group and always acts as a page.

Press enter or click to view image in full size

===

Reproduction steps:

1) Using the Facebook web, acting as Sarah's Page, create a document in Sarah's Group with the "Create doc" button.

Press enter or click to view image in full size

2) Before publishing that document, uncheck the option "Allow group members to edit this document". So that only the document owners or admins will be able to edit that document.

Press enter or click to view image in full size

3) Now acting as Sarah's Page, edit and save that document.

4) Now if we see the version history of this document, there will be the name of Sarah.

Press enter or click to view image in full size

===

Get Shubham Bhamare’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The logic behind it:

It was easy for other group members to determine who was the admin of the page as only the document owner or admins were able to edit that document. Though there was the name of Sarah in edit history which was unintended.

===

Fix and Bypass:

When the team fixed this issue for the "Create doc" button which was present in the post editor, I found that there was another similar button on the "Files" page which was also vulnerable.

When the team was verifying the second fix, they internally identified 3rd vector that also could be abused.

===

Bounty:

5000 USD (This reward covers all three of those vulnerabilities. That's why I like Facebook bug bounty the most. 💙)

Press enter or click to view image in full size

===

Timeline:

Oct 13, 2018: Report sent
Oct 17, 2018: Pre-triaged
Oct 17, 2018: Triaged
Oct 17, 2018: Sent additional information about another vulnerable "Create doc" button
Feb 09, 2019: Fixed completely
Feb 09, 2019: 5000 USD bounty awarded

===

Takeaway(s):

1) Don't reveal your findings until you fully believe that there won't be any bypass for it. 😉 Check other endpoints/features too for similar issues.

2) Sometimes you just need logical thinking instead of any advanced tools or knowledge. Because Logic == Magic. 😊

3) Again, if you're new to Facebook bug bounty, try to find logical bugs the most.

===

Thank you for reading! Stay tuned for my next write-up and don't forget to follow me on Facebook, Twitter, Instagram, and Medium. 😊

===

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!
