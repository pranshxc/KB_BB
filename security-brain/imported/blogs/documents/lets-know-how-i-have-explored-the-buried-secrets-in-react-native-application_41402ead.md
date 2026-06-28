---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-18_lets-know-how-i-have-explored-the-buried-secrets-in-react-native-application.md
original_filename: 2021-01-18_lets-know-how-i-have-explored-the-buried-secrets-in-react-native-application.md
title: Let’s know How I have explored the buried secrets in React Native application
category: documents
detected_topics:
- mobile-security
- command-injection
- information-disclosure
tags:
- imported
- documents
- mobile-security
- command-injection
- information-disclosure
language: en
raw_sha256: 41402eaddc968ac7f002e95e6418a77851f6f77645a024dde9e26ed17f705a9a
text_sha256: bb61e5db6c9ffe117bb792928048f773fc30784fbbff48dff3e991b0b96d639c
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Let’s know How I have explored the buried secrets in React Native application

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-18_lets-know-how-i-have-explored-the-buried-secrets-in-react-native-application.md
- Source Type: markdown
- Detected Topics: mobile-security, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `41402eaddc968ac7f002e95e6418a77851f6f77645a024dde9e26ed17f705a9a`
- Text SHA256: `bb61e5db6c9ffe117bb792928048f773fc30784fbbff48dff3e991b0b96d639c`


## Content

---
title: "Let’s know How I have explored the buried secrets in React Native application"
url: "https://secureitmania.medium.com/lets-know-how-i-have-explored-the-buried-secrets-in-react-native-application-6236728198f7"
authors: ["secureITmania (@secureitmania)"]
bugs: ["Information disclosure", "Hardcoded credentials"]
publication_date: "2021-01-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3986
scraped_via: "browseros"
---

# Let’s know How I have explored the buried secrets in React Native application

Member-only story

MOBILE APPLICATION PENETRATION TESTING GUIDE
Let’s know How I have explored the buried secrets in React Native application
A new era in Android Reverse Engineering part-1
secureITmania
Follow
3 min read
·
Jan 18, 2021

112

1

Thanks for the huge response to my previous write-up. Recently I have found a bug regards to hard-coded credentials issue that was found by a different approach instead of old reverse engineering methodology.

Introduction:

React Native is a mobile application framework that is most commonly used to develop applications for Android and iOS by enabling the use of React and native platform capabilities. These days, it’s become increasingly popular to use React across platforms.

Old-fashioned way of Android Reverse Engineering

Typically, when reversing an Android application, it is de-compiled using apktool, dex2jar and then analyzed using JD-GUI. When dealing with React Native applications, this can be useful if the application has any native code that you would like to analyze.

But most of the time, the core logic of the application lies in the React Native JavaScript that can be obtained without needing to use dex2jar.

Reverse Engineering Process: React Native application

Step-1: Let’s confirm whether the application was built on React Native framework.
