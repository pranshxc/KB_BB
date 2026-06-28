---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-13_from-android-app-to-access-admin-dashboard.md
original_filename: 2022-05-13_from-android-app-to-access-admin-dashboard.md
title: From android app to access admin dashboard
category: documents
detected_topics:
- command-injection
- api-security
- mobile-security
tags:
- imported
- documents
- command-injection
- api-security
- mobile-security
language: en
raw_sha256: e8133547c5e89f233581e5eddc2d27835f3344d5eba078498f642c1f4c1ffbfe
text_sha256: c53ee6f8c1a09d56caa90b7a183e45a143cb1de7b158bf5ef5fb06580ef6ef96
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# From android app to access admin dashboard

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-13_from-android-app-to-access-admin-dashboard.md
- Source Type: markdown
- Detected Topics: command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `e8133547c5e89f233581e5eddc2d27835f3344d5eba078498f642c1f4c1ffbfe`
- Text SHA256: `c53ee6f8c1a09d56caa90b7a183e45a143cb1de7b158bf5ef5fb06580ef6ef96`


## Content

---
title: "From android app to access admin dashboard"
url: "https://medium.com/@odayalhalbe1/from-android-app-to-access-admin-dashboard-a8f825e8e806"
authors: ["Oday Alhalabi (@OdayAlhalabi)"]
bugs: ["Exposed registration page", "Account takeover"]
publication_date: "2022-05-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2642
scraped_via: "browseros"
---

# From android app to access admin dashboard

From android app to access admin dashboard
Oday Alhalabi
Follow
1 min read
·
May 13, 2022

11

One of easy and interesting vulnerability that I found and lead to access admin dashboard for company (internal system) :

1. Found android app for same company .

2-Download the app as apk and decompiling it .

3-Found xml file contain on a domain for same company .

4-Seach about domains/ips that use same certificate for domain in step #3 .

Get Oday Alhalabi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

5-Found ip belong to same company and use same certificate .

6-Fuzz directory for that ip and then I found login page for internal system .

7-I tried to bypass login ,but I couldn’t .

8-In source code for same page I found endpoint allow to create account .

9-Created account and then login for admin dashboard (internal system) .

When the company solved this issue and give me the bounty ,I bypassed the fix by another way :)

#bugbountytips
#bugbounty
#hackerone
