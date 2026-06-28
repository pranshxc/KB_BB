---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-22_access-twitter-blue-features-using-deeplink-without-a-subscription.md
original_filename: 2023-02-22_access-twitter-blue-features-using-deeplink-without-a-subscription.md
title: Access Twitter blue features using deeplink without a subscription.
category: documents
detected_topics:
- command-injection
- mfa
- mobile-security
tags:
- imported
- documents
- command-injection
- mfa
- mobile-security
language: en
raw_sha256: c871b62cd6d357090844a328b47aba701edee75403fd9e4253707f49fad5d5ea
text_sha256: 3230fdfc9ceb5b13362b1216af1eca2b7423a941101ee4f4836ae0fb131bc846
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# Access Twitter blue features using deeplink without a subscription.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-22_access-twitter-blue-features-using-deeplink-without-a-subscription.md
- Source Type: markdown
- Detected Topics: command-injection, mfa, mobile-security
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `c871b62cd6d357090844a328b47aba701edee75403fd9e4253707f49fad5d5ea`
- Text SHA256: `3230fdfc9ceb5b13362b1216af1eca2b7423a941101ee4f4836ae0fb131bc846`


## Content

---
title: "Access Twitter blue features using deeplink without a subscription."
page_title: "Access Twitter blue features using deeplink without a subscription. | SERVICENGER"
url: "https://servicenger.com/mobile/android/access-twitter-blue-features-using-deeplink-without-a-paid-subscription/"
final_url: "https://servicenger.com/mobile/android/access-twitter-blue-features-using-deeplink-without-a-paid-subscription/"
authors: ["Rahul Kankrale (@RahulKankrale)"]
programs: ["Twitter"]
bugs: ["Insecure deeplink", "Android"]
publication_date: "2023-02-22"
added_date: "2023-02-22"
source: "pentester.land/writeups.json"
original_index: 1495
---

# Access Twitter blue features using deeplink without a subscription.

Posted  Feb 22, 2023 

By _Rahul Kankrale_

_1 min_ read

Twitter recently launched Twitter Blue for Android users, allowing them to change the app icon and undo tweets at any time. Twitter Android’s version number is 9.76.0-release.0 has implemented some deeplinks for Twitter subscription to perform direct action, and some of those deeplinks are not being validated or don’t have custom permissions set if the user has a subscription or not, so it is possible to use the change icon, custom navigation, and early access features without a subscription using the below deeplinks:

`twitter://subscriptions/settings/extras`

`twitter://subscriptions/settings/early_access`

extras deeplink gives access to change icon and change custom navigation and early_access deeplink gives access to features like undo tweets with custom timing.

* * *

  * ##### Steps To Reproduce:__

  * Launch below deeplink using adb to access app change flow:

____

`
  
  1

| 
  
  adb shell am start -d "twitter://subscriptions/settings/extras"
  
  
---|---  
`

  * Launch below deeplink using adb to access undo tweet feature:

____

`
  
  1

| 
  
  adb shell am start -d "twitter://subscriptions/settings/early_access"
  
  
---|---  
`

* * *

  * ##### Proof of concept:__

__[Android](/categories/android/), [Mobile](/categories/mobile/)

__[android](/tags/android/) [bug](/tags/bug/) [twitter-blue](/tags/twitter-blue/)

This post is licensed under [ CC BY 4.0 ](https://creativecommons.org/licenses/by/4.0/) by the author.

Share [ __](https://twitter.com/intent/tweet?text=Access%20Twitter%20blue%20features%20using%20deeplink%20without%20a%20subscription.%20-%20SERVICENGER&url=https%3A%2F%2Fwww.servicenger.com%2Fmobile%2Fandroid%2Faccess-twitter-blue-features-using-deeplink-without-a-paid-subscription%2F "Twitter") [ __](https://www.facebook.com/sharer/sharer.php?title=Access%20Twitter%20blue%20features%20using%20deeplink%20without%20a%20subscription.%20-%20SERVICENGER&u=https%3A%2F%2Fwww.servicenger.com%2Fmobile%2Fandroid%2Faccess-twitter-blue-features-using-deeplink-without-a-paid-subscription%2F "Facebook") [ __](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fwww.servicenger.com%2Fmobile%2Fandroid%2Faccess-twitter-blue-features-using-deeplink-without-a-paid-subscription%2F "Linkedin") [ __](https://t.me/share/url?url=https%3A%2F%2Fwww.servicenger.com%2Fmobile%2Fandroid%2Faccess-twitter-blue-features-using-deeplink-without-a-paid-subscription%2F&text=Access%20Twitter%20blue%20features%20using%20deeplink%20without%20a%20subscription.%20-%20SERVICENGER "Telegram") __
