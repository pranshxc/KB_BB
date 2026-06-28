---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-02-22_modifying-any-ad-space-and-placement.md
original_filename: 2018-02-22_modifying-any-ad-space-and-placement.md
title: Modifying any Ad Space and Placement
category: documents
detected_topics:
- idor
- command-injection
- otp
tags:
- imported
- documents
- idor
- command-injection
- otp
language: en
raw_sha256: 7cc5d4d68c9de11beb9e04b762014fdda9771bf7e2ab0714a9e7b67b56a9a543
text_sha256: 1852ca07c14bc1ce3a019f128ee21bbebf4f136bef8802fa7300c06e858826d5
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: true
---

# Modifying any Ad Space and Placement

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-02-22_modifying-any-ad-space-and-placement.md
- Source Type: markdown
- Detected Topics: idor, command-injection, otp
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: True
- Raw SHA256: `7cc5d4d68c9de11beb9e04b762014fdda9771bf7e2ab0714a9e7b67b56a9a543`
- Text SHA256: `1852ca07c14bc1ce3a019f128ee21bbebf4f136bef8802fa7300c06e858826d5`


## Content

---
title: "Modifying any Ad Space and Placement"
url: "https://medium.com/@joshuaregio/modifying-any-ad-space-and-placement-e22c7cec050f"
authors: ["Joshua Regio"]
programs: ["Meta / Facebook"]
bugs: ["IDOR"]
publication_date: "2018-02-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5967
scraped_via: "browseros"
---

# Modifying any Ad Space and Placement

Modifying any Ad Space and Placement
Joshua Regio
Follow
2 min read
·
Feb 23, 2018

105

1

Press enter or click to view image in full size

In early November, Facebook introduced a new feature in the Audience Network called Ad Spaces.

Description: It is possible to modify any Ad Space and Placement given the victim’s Ad Space and Placement IDs

Impact: A malicious user can modify any info of an Ad Space. A malicious user can also add and modify Placement.

Get Joshua Regio’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Proof of Concept:
Editing Ad Space:
1. Go to “https://developers.facebook.com/apps/APP_ID/audience-network/adspaces/".
2. Create an Ad Space.
3. Edit that Ad Space.
4. Using a Debugging Tool, capture the POST request in editing the Ad Space.
5. In the POST request change the param “ad_space_id” to any Ad space ID

Adding Placement:
1. Go to “https://developers.facebook.com/apps/APP_ID/audience-network/adspaces/".
2. In your Ad Space, create a Placement.
3. Make sure to capture the POST request using a Debugging Tool.
4. In the POST request change the “ad_space_id” to any Ad Space ID

Editing Placement:
1. Go to “https://developers.facebook.com/apps/APP_ID/audience-network/adspaces/".
2. Select and Edit your Placement.
3. Make sure to capture the POST request using a proxy tool.
4. In the POST request URL change the Placement ID to your Victim’s Placement ID.

Their initial fix was to disallow any user to modify any Ad Spaces, but you could still modify Ad Spaces if you have a Tester or Analytic User role in the App.

Video POC: https://drive.google.com/drive/folders/***REDACTED-SUSPECT-TOKEN***Timeline:
Nov. 09, 2017 — Initial Report
Nov. 14, 2017 — Report Triaged
Dec. 5, 2017 — Fixed by Facebook
Dec. 5, 2017 —Fix is insufficient
Dec. 15, 2017 — Fixed by Facebook
Dec. 15, 2017 — Fix is insufficient
Dec. 21, 2017 — Bounty awarded
Feb. 19, 2018 — Issue Resolved
