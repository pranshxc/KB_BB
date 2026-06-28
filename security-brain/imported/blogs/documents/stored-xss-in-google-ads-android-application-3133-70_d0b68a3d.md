---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-07_stored-xss-in-google-ads-android-application-313370.md
original_filename: 2021-03-07_stored-xss-in-google-ads-android-application-313370.md
title: Stored XSS in Google Ads Android Application— $3133.70
category: documents
detected_topics:
- xss
- command-injection
- mobile-security
tags:
- imported
- documents
- xss
- command-injection
- mobile-security
language: en
raw_sha256: d0b68a3db278b4c670cadbe95dd3cec28afbc1f10df0b9db013a231b4cb093fb
text_sha256: df1791b573b4647d783bc489f51fcb8f5922f65466e8f6c02583b373ea09679a
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Stored XSS in Google Ads Android Application— $3133.70

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-07_stored-xss-in-google-ads-android-application-313370.md
- Source Type: markdown
- Detected Topics: xss, command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `d0b68a3db278b4c670cadbe95dd3cec28afbc1f10df0b9db013a231b4cb093fb`
- Text SHA256: `df1791b573b4647d783bc489f51fcb8f5922f65466e8f6c02583b373ea09679a`


## Content

---
title: "Stored XSS in Google Ads Android Application— $3133.70"
url: "https://ashketchum.medium.com/stored-xss-in-google-ads-android-application-3133-70-373f6c361ff3"
authors: ["Ashish Dhone (@ashketchum_16)"]
programs: ["Google"]
bugs: ["Stored XSS", "HTML injection"]
bounty: "3,133.70"
publication_date: "2021-03-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3834
scraped_via: "browseros"
---

# Stored XSS in Google Ads Android Application— $3133.70

Member-only story

Stored XSS in Google Ads Android Application— $3133.70
Ashish Dhone
Follow
3 min read
·
Mar 6, 2021

150

Introduction

This article is a write up on how I found a Stored XSS in Google Ads Android Application where I was rewarded with $3133.70 I was waiting for the fix and after discussing with Google Security Team I am disclosing my finding.

Currently I am ranked in Top 200 at Google Hacker’s Ranking ,

Press enter or click to view image in full size

What is Stored XSS

Stored XSS attacks are those where the injected script is permanently stored on the target servers, such as in a database, in a message forum, visitor log, comment field, etc. The victim then retrieves the malicious script from the server when it requests the stored information. Stored XSS is also sometimes referred to as Persistent XSS.

Vulnerability exploitation

When you have a large scope to hack it is always difficult to choose the target, but this time I wanted to hack on Google Ads as I have seen many reports regarding XSS on Google Ads and as always I wanted to get XSS my all time favorite.

I started listing bugs found on Google Ads and I was amazed to look at some awesome XSS. So I started hunting it was 3 days on same target did everything with bypasses but no luck didn’t found any XSS.
