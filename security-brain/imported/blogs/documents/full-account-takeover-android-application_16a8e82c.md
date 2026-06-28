---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-21_full-account-takeover-android-application.md
original_filename: 2019-12-21_full-account-takeover-android-application.md
title: Full Account Takeover (Android Application)
category: documents
detected_topics:
- command-injection
- otp
- information-disclosure
- mobile-security
tags:
- imported
- documents
- command-injection
- otp
- information-disclosure
- mobile-security
language: en
raw_sha256: 16a8e82cedf2c871d274a9e5aab324a5cf3afcfad14110be1fa93c36ef459f4e
text_sha256: 156f81dcb23c1d52ea229f168aeec31c91481509192a5977afffc266b8fdc9fa
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Full Account Takeover (Android Application)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-21_full-account-takeover-android-application.md
- Source Type: markdown
- Detected Topics: command-injection, otp, information-disclosure, mobile-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `16a8e82cedf2c871d274a9e5aab324a5cf3afcfad14110be1fa93c36ef459f4e`
- Text SHA256: `156f81dcb23c1d52ea229f168aeec31c91481509192a5977afffc266b8fdc9fa`


## Content

---
title: "Full Account Takeover (Android Application)"
url: "https://medium.com/@vbharad/full-account-takeover-android-application-78fa922f78c5"
authors: ["Vishal Bharad"]
bugs: ["Information disclosure", "Account takeover"]
publication_date: "2019-12-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4875
scraped_via: "browseros"
---

# Full Account Takeover (Android Application)

Member-only story

Full Account Takeover (Android Application)
Vishal Bharad
Follow
2 min read
·
Dec 21, 2019

287

1

Introduction :

Hello Again, I am Vishal Bharad, I’m here again to share about my findings on Full Account Takeover on Android Application

About the Vulnerability :

First of all this is the one of the Simplest Vulnerability which rated in P1 Category. For Discovering the bug need to Setup for Android Application Penetration Testing.

Hope You all already know about the Setup of Android Application Penetration Testing. :)

So I am directly started with the Vulnerability that I have identified. Consider I have an Android Application which is target.apk

Tools Used for this Vulnerability:

BurpSuite
Genymotion

General Steps:

First of all Setup for a Android Application Penetration Testing
Then open genymotion and Install the application which is target.apk
After Installing application we need to Bypass the SSL via SSLunpinned application.
Then we are able to capture the request in Burp suite.

Steps to Reproduce the Vulnerability

After Installing application create an account as victim account.
Go to the Recover Password and type username or Mobile number to receive OTP or CODE.
Capture the Recover Password request in BurpSuite. Now Right…
