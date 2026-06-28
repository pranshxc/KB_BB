---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-03-27_creating-test-conversion-using-any-app.md
original_filename: 2018-03-27_creating-test-conversion-using-any-app.md
title: Creating Test Conversion using any App
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
raw_sha256: 44ccdd49c7c918d76198a9503d332d3d97e47d26616483a6a102e97e8974d4fd
text_sha256: 0fd0731bd921256e1d72395f637421b59d53732047fbd38da300572617c897cb
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Creating Test Conversion using any App

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-03-27_creating-test-conversion-using-any-app.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `44ccdd49c7c918d76198a9503d332d3d97e47d26616483a6a102e97e8974d4fd`
- Text SHA256: `0fd0731bd921256e1d72395f637421b59d53732047fbd38da300572617c897cb`


## Content

---
title: "Creating Test Conversion using any App"
url: "https://medium.com/bugbountywriteup/creating-test-conversion-using-any-app-8b32ee0a735"
authors: ["Joshua Regio"]
programs: ["Meta / Facebook"]
bugs: ["Parameter tampering"]
bounty: "3,000"
publication_date: "2018-03-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5940
scraped_via: "browseros"
---

# Creating Test Conversion using any App

Creating Test Conversion using any App
Joshua Regio
Follow
1 min read
·
Mar 28, 2018

169

1

The Facebook ad account test can help you understand how many sales or conversions your Facebook, Instagram and Audience Network ads are causing.(source)

Press enter or click to view image in full size

Description: A malicious user can create test conversion using any app which could reveal the sales and conversions of an active campaign.

Get Joshua Regio’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Impact: Before they redesigned this feature a user could choose which type of event should the test count as a conversion. Some of these events type includes purchase, add to wishlist, initial checkout, spend credit, etc…

Reproduction Step:
1. Go to facebook.com/test-and-learn/?act=AD_ACCOUNT_ID
2. Set Up Test
3. Fill in the necessary information.
4. Intercept the request before creating a test.
5. In the /ad-studies request, change the APP ID to your victim’s app id.
6. Test Conversion is created.

Timeline:
Feb. 10, 2018 — Issue Reported
Feb. 16, 2018 — Report Triaged
Mar. 22, 2018 — Issue Fixed
Mar. 26, 2018 — Bounty Awarded $3,000
