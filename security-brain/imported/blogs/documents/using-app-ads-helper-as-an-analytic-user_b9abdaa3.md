---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-12-09_using-app-ads-helper-as-an-analytic-user.md
original_filename: 2017-12-09_using-app-ads-helper-as-an-analytic-user.md
title: Using App Ads Helper as an Analytic User
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
raw_sha256: b9abdaa33006061d0a01bef32d13d3bc233a54f088c8be9126513376b43e1b9a
text_sha256: 532a32fc862273162106b101b66149c01d96b4ed6edf78466fcecd7f0275e619
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Using App Ads Helper as an Analytic User

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-12-09_using-app-ads-helper-as-an-analytic-user.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, mobile-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `b9abdaa33006061d0a01bef32d13d3bc233a54f088c8be9126513376b43e1b9a`
- Text SHA256: `532a32fc862273162106b101b66149c01d96b4ed6edf78466fcecd7f0275e619`


## Content

---
title: "Using App Ads Helper as an Analytic User"
url: "https://medium.com/@joshuaregio/using-app-ads-helper-as-an-analytic-user-e751fcf9c594"
authors: ["Joshua Regio"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization"]
bounty: "500"
publication_date: "2017-12-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6032
scraped_via: "browseros"
---

# Using App Ads Helper as an Analytic User

Using App Ads Helper as an Analytic User
Joshua Regio
Follow
1 min read
·
Dec 9, 2017

4

Description: Analytic Users are only given access to an app’s insight. In the App Ads Helper, you can check the app platform setting, mobile app install ads bid type information and a developer tools to test if a certain function of the app is working.

Get Joshua Regio’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Proof of Concept:
Go to “https://developers.facebook.com/tools/app-ads-helper/" and select your app with an Analytic User role.

In the Ads App Helper you could:
- Check the App platform setting
- Check whether an Ad Account is eligible for bidding CPA
- Use the App Event Tester & Deep Link Tester

Impact: An analytic user can see information that shouldn’t be available to them. They could also use tools which would allow them to test certain functions of the app.

Timeline:
Sept. 1 2017 — Initial Report
Sept. 9 2017 — Report Triaged
Nov. 2 2017 — Advance Bounty of $500
Nov. 3 2017 — Bug Fixed
