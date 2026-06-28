---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-29_force-browsing-bug-at-facebook-business-plan-500-bounty.md
original_filename: 2021-09-29_force-browsing-bug-at-facebook-business-plan-500-bounty.md
title: Force Browsing bug at Facebook business plan ($500 Bounty)
category: documents
detected_topics:
- access-control
- command-injection
tags:
- imported
- documents
- access-control
- command-injection
language: en
raw_sha256: 5d39bb9cbe3c525456f1c4c48319fdfc22c6cf8d02cd6bde8425bcb3d3a0d877
text_sha256: 9959c1ff14034fcc4a495a130c3a789bc12b0b40aa2e384ccd5d979fcee6243f
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Force Browsing bug at Facebook business plan ($500 Bounty)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-29_force-browsing-bug-at-facebook-business-plan-500-bounty.md
- Source Type: markdown
- Detected Topics: access-control, command-injection
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `5d39bb9cbe3c525456f1c4c48319fdfc22c6cf8d02cd6bde8425bcb3d3a0d877`
- Text SHA256: `9959c1ff14034fcc4a495a130c3a789bc12b0b40aa2e384ccd5d979fcee6243f`


## Content

---
title: "Force Browsing bug at Facebook business plan ($500 Bounty)"
url: "https://dewcode.medium.com/force-browsing-bug-at-facebook-business-plan-500-bounty-73d1bb4883af"
authors: ["Dewanand Vishal (@dewcode91)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization", "Forced browsing"]
bounty: "500"
publication_date: "2021-09-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3276
scraped_via: "browseros"
---

# Force Browsing bug at Facebook business plan ($500 Bounty)

Force Browsing bug at Facebook business plan ($500 Bounty)
Dewanand Vishal
Follow
3 min read
·
Sep 29, 2021

189

1

Hi bug hunters! this article is about my last finding on Facebook. I regularly check Facebook for the latest updates and features. In April I noticed they add a feature called Business Plan for page admin. you can read below how I was able to abuse this feature.

Press enter or click to view image in full size

While testing this feature I noticed if a page analyst browses this path directly then he can able to access and manage the business plan but it is only possible with the correct session_id.

Press enter or click to view image in full size
I reported the issue to the Facebook team

A business page admin can create a business plan for their page. Which can not be managed by any user other than admin. I noticed if Page Analyst browses the URL https://www.facebook.com/business/dashboard/?session_id=[ID in BASE64] then he can able to manage the business plan created by the admin.

Get Dewanand Vishal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The Facebook team response

Hi Dew,

The session_id does not appear to be bruteforceable due to its complex nature, so that does not seem to be a feasible scenario. There does not appear to be any significant security impact, therefore this does not qualify for a bounty. If you can update this report with a PoC that shows a clear security impact, please do so and we can re-evaluate this issue.

After the Facebook team response. I look for different ways to exploit this issue. After some time I noticed if a page analyst browses the path without session_id. He can still able to access and manage the business plan. I immediately reopen the report. One of the Facebook team members confirms the issue is valid.

Press enter or click to view image in full size

After fixed Facebook awarded me $500 and the hall of fame on their thanks page.

Motivation

Don’t stop if the security team closes your report as informative. Always try to look for different ways to interact with the application.
