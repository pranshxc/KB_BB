---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-21_lets-know-how-i-have-explored-the-buried-secrets-in-xamarin-application.md
original_filename: 2021-02-21_lets-know-how-i-have-explored-the-buried-secrets-in-xamarin-application.md
title: Let’s know How I have explored the buried secrets in Xamarin application
category: documents
detected_topics:
- mobile-security
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- mobile-security
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: a027b0bb403b446fc7d6e0015c14ce12b0de30200faa391b8cd4b1e23485ccd6
text_sha256: 951bc59ca748728a140d1b81c686b8adf9d077bc05bd706534ad3d31dd562af0
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Let’s know How I have explored the buried secrets in Xamarin application

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-21_lets-know-how-i-have-explored-the-buried-secrets-in-xamarin-application.md
- Source Type: markdown
- Detected Topics: mobile-security, command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `a027b0bb403b446fc7d6e0015c14ce12b0de30200faa391b8cd4b1e23485ccd6`
- Text SHA256: `951bc59ca748728a140d1b81c686b8adf9d077bc05bd706534ad3d31dd562af0`


## Content

---
title: "Let’s know How I have explored the buried secrets in Xamarin application"
url: "https://secureitmania.medium.com/lets-know-how-i-have-explored-the-buried-secrets-in-xamarin-application-d6b8c5609c87"
authors: ["secureITmania (@secureitmania)"]
bugs: ["Hardcoded API keys", "Information disclosure"]
publication_date: "2021-02-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3876
scraped_via: "browseros"
---

# Let’s know How I have explored the buried secrets in Xamarin application

Member-only story

MOBILE APPLICATION PENETRATION TESTING GUIDE
Let’s know How I have explored the buried secrets in Xamarin application
A new era in Android Reverse Engineering part-2
secureITmania
Follow
3 min read
·
Feb 20, 2021

54

In my previous write-up I explain the React Native reverse engineering technique. Again I have found a bug in Xamarin based application that was found by a different approach instead of old reverse engineering methodology.

Introduction:

Xamarin is a free and open source mobile app platform for building native and high-performance iOS, Android, tvOS, watchOS, macOS, and Windows.

Old-fashioned way of Android Reverse Engineering

Typically, when reversing an Android application, it is de-compiled using apktool, dex2jar and then analyzed using JD-GUI. When dealing with Native applications, this can be useful if the application has any native code that you would like to analyze.

But most of the time, the core logic of the application lies in the “.dll” that can be obtained without needing to use dex2jar.

Reverse Engineering Process: Xamarin application

Step-1: Let’s confirm whether the application was built on Xamarin framework.

To check this, rename the APK with zip extension and then extract the APK to a new folder using the following command
