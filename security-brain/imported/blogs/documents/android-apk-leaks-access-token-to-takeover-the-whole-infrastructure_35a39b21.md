---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-30_android-apk-leaks-access-token-to-takeover-the-whole-infrastructure.md
original_filename: 2021-01-30_android-apk-leaks-access-token-to-takeover-the-whole-infrastructure.md
title: Android apk leaks access token to takeover the whole infrastructure
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
raw_sha256: 35a39b219906317ea626b0b060201ec45a99bb910de7caa5de3718a6501217bf
text_sha256: 601dec7141a961e2818cf8e6a535329b1e56547e260c6b5e40247143a940c611
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Android apk leaks access token to takeover the whole infrastructure

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-30_android-apk-leaks-access-token-to-takeover-the-whole-infrastructure.md
- Source Type: markdown
- Detected Topics: command-injection, otp, information-disclosure, mobile-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `35a39b219906317ea626b0b060201ec45a99bb910de7caa5de3718a6501217bf`
- Text SHA256: `601dec7141a961e2818cf8e6a535329b1e56547e260c6b5e40247143a940c611`


## Content

---
title: "Android apk leaks access token to takeover the whole infrastructure"
page_title: "Android APK leaks access token to takeover the whole infrastructure | by Santosh Kumar Sha(@killmongar1996) | Medium"
url: "https://notifybugme.medium.com/android-apk-leaks-access-token-to-takeover-the-whole-infrastructure-c979187f8fc8"
authors: ["Santosh Kumar Sha (@killmongar1996)"]
bugs: ["Information disclosure", "Hardcoded credentials", "Android"]
publication_date: "2021-01-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3951
scraped_via: "browseros"
---

# Android apk leaks access token to takeover the whole infrastructure

Member-only story

Android APK leaks access token to takeover the whole infrastructure
Santosh Kumar Sha(@killmongar1996)
Follow
2 min read
·
Jan 30, 2021

88

1

Hi, everyone

My name is Santosh Kumar Sha, I’m a security researcher from India(Assam). In this article, I will be describing how I was able to Find the production and staging access token leaked by android application and takeover the whole infrastructure .

I am now offering 1:1 sessions to share my knowledge and expertise:

topmate.io/santosh_kumar_sha

TIP For looking for android bug :

Tools Requried:

gf (tomnomnom) — https://github.com/tomnomnom/gf
grep
apktool
Case# — — Finding hard coded Credential in android apk .

Here is how I get access to the company production and staging server by the access token leaked by android application.

So I was looking for android bug in One of the public bugbounty program . So i download the android application apk file and de-compile and started looking around.

How to download android application:

Suppose “example” the company to look for android application

Just search on Google like these “example android application downloadable”

Command to decompile the android application:
