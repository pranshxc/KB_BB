---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-01-05_facebook-android-application.md
original_filename: 2019-01-05_facebook-android-application.md
title: Facebook Android Application
category: documents
detected_topics:
- access-control
- command-injection
- path-traversal
- mobile-security
tags:
- imported
- documents
- access-control
- command-injection
- path-traversal
- mobile-security
language: en
raw_sha256: 78502284de512075b25631a73be08abb318bfa2445e2ef85d0f7393968e6510e
text_sha256: d3167d076b171c4a61c0b91dc7e57e1a9048600dbb97dbf8b9c4899ef80e525b
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook Android Application

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-01-05_facebook-android-application.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, path-traversal, mobile-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `78502284de512075b25631a73be08abb318bfa2445e2ef85d0f7393968e6510e`
- Text SHA256: `d3167d076b171c4a61c0b91dc7e57e1a9048600dbb97dbf8b9c4899ef80e525b`


## Content

---
title: "Facebook Android Application"
page_title: "Ashley King - Downloading any file via Facebook for Android"
url: "https://www.ash-king.co.uk/downloading-any-file-via-facebook-android.html"
final_url: "https://www.ash-king.co.uk/downloading-any-file-via-facebook-android.html"
authors: ["Ashley King (@AshleyKingUK)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization"]
bounty: "750"
publication_date: "2019-01-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5487
---

## Summary

The Facebook android app utilises [deeplinks](https://developer.android.com/training/app-links/deep-linking) throughout the whole application.  
  
I stumbled upon a deeplink which opens any given video url in your default media app, expected behaviour except this endpoint did not validate the file type or it's source. Crafting together a fb:// deeplink I could initiaite a download for certain file types from within the Facebook process. 

## Example

The affected deeplink `fb://video/?href={LINK TO FILE}`

Below demonstrates the Facebook application downloading a random apk file, as ES File explorer is installed we're able to save and launch the downloaded file. 

The limitation of this vulnerability is that the end user is required to have a file manager installed. Depending on the file manager it may allow the file to be downloaded without user interaction. 

## Timeline - Key dates

  * Reported to Facebook - 21 Oct 2018
  * First Response - 23 Oct 2018
  * Triage - 14 Nov 2018
  * Fixed - 30 Nov 2018
  * Bounty Received - 6 Dec 2018

## Response From Facebook Security Team

> Hi Ash King  
>  
>  After reviewing this issue, we have decided to award you a bounty of $750. Below is an explanation of the bounty amount. Facebook fulfills its bounty awards through Bugcrowd.  
>  
>  Getting an Android user to open a fb://video/?href= link will result in their phone automatically downloading the linked file if they have a file manager installed.  
>  
>  Thank you again for your report. We look forward to receiving more reports from you in the future! 

  

Enjoyed the read?  
Donate a coffee or two __<http://paypal.me/ashleykinguk>
