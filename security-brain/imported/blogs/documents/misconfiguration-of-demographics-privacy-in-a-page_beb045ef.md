---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-03-26_misconfiguration-of-demographics-privacy-in-a-page.md
original_filename: 2018-03-26_misconfiguration-of-demographics-privacy-in-a-page.md
title: Misconfiguration of Demographics Privacy in a Page
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
raw_sha256: beb045efd0ff801bb1b4522eeeb79c4d5cff04750c29b1b7d54466fd7ffe24c4
text_sha256: f71e9dbe7de897a7339514e5d27ab4df24516feef223c48b33b9f1654758a76d
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Misconfiguration of Demographics Privacy in a Page

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-03-26_misconfiguration-of-demographics-privacy-in-a-page.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `beb045efd0ff801bb1b4522eeeb79c4d5cff04750c29b1b7d54466fd7ffe24c4`
- Text SHA256: `f71e9dbe7de897a7339514e5d27ab4df24516feef223c48b33b9f1654758a76d`


## Content

---
title: "Misconfiguration of Demographics Privacy in a Page"
url: "https://medium.com/@markchristiandeduyo/misconfiguration-of-demographics-privacy-in-a-page-682feb1179f2"
authors: ["Mark Christian Deduyo"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw"]
bounty: "750"
publication_date: "2018-03-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5943
scraped_via: "browseros"
---

# Misconfiguration of Demographics Privacy in a Page

Misconfiguration of Demographics Privacy in a Page
Mark Christian Deduyo
Follow
2 min read
·
Mar 26, 2018

116

1

Description: Demographics is Limit Visibility of This Post, Choose who can see your post on Facebook based on their demographic. For example: If you enter “Spanish” below, only people who have Spanish set as their language on Facebook or list Spanish as one of their languages on their profile will be eligible to see your post on your Page

Impact: It allows the User to view a Page post with audience limitation

Proof Of Concept:
User 1 = Page Admin
User 2 = Page Visitor (Not Friend of User 1 and Doesn’t have role in a page)

Get Mark Christian Deduyo’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

1.) User 1 (as the Page) will publish a post in the page
2.) User 1 will click “Edit Post” to edit his new post
3.) User 1 will click “Public” Privacy then change it to “Demographics”
4.) User 1 will set the Limit Visibility of This Post (ex. Gender: Women, Age: 13–14)
5.) Go to User 2 account, Take Note User 2 is a “Male” and Age “20”
6.) Notice That User 2 can still view the Post even though User 1 limit his audience

Proof Of Concept Video: Click Here

Here’s an explanation from Facebook:

Timeline:
Feb. 08, 2018 — Initial Report
Feb. 15, 2018 — Report Triaged
Mar. 03, 2018 — Temporary Fixed (Facebook Removes the Feature)
Mar. 03, 2018 — Fixed Confirmed
Mar. 14, 2018 — Bounty Awarded
