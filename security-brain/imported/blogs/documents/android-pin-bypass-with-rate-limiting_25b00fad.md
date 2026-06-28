---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-18_android-pin-bypass-with-rate-limiting.md
original_filename: 2020-07-18_android-pin-bypass-with-rate-limiting.md
title: Android pin bypass with rate limiting
category: documents
detected_topics:
- rate-limit
- mobile-security
- command-injection
tags:
- imported
- documents
- rate-limit
- mobile-security
- command-injection
language: en
raw_sha256: 25b00fada5270c7052ae8ac10291150d1e3e7b7fe6f677539a9b93d3756feb48
text_sha256: 91b8bdb4a27cb47e53b6132732edf53581b42cae29233d913845cdd81cee432f
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Android pin bypass with rate limiting

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-18_android-pin-bypass-with-rate-limiting.md
- Source Type: markdown
- Detected Topics: rate-limit, mobile-security, command-injection
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `25b00fada5270c7052ae8ac10291150d1e3e7b7fe6f677539a9b93d3756feb48`
- Text SHA256: `91b8bdb4a27cb47e53b6132732edf53581b42cae29233d913845cdd81cee432f`


## Content

---
title: "Android pin bypass with rate limiting"
url: "https://medium.com/@balook/android-pin-bypass-with-rate-limiting-a3f5dd811715"
authors: ["Baluz (@t3chman)"]
bugs: ["Lack of rate limiting", "Authentication bypass"]
publication_date: "2020-07-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4402
scraped_via: "browseros"
---

# Android pin bypass with rate limiting

Android pin bypass with rate limiting
baluz
Follow
1 min read
·
Jul 18, 2020

11

Application pin rate limiting bypass

The bug is in private program .

There is a feature to lock mobile app with pin . But only 3 attempts. If we attempt wrong pin. The app logouts.

But there is a misconfig in this feature. If you enter the pin 2 times. close the app and open the app again you will get another 3 attempts . So the rate limiting bypassed by closing and calling the main activity

Get baluz’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

You can launch the main activity as many times as you want with adb

while true;do adb shell am start -a android.intent.action.VIEW -n com.redacted/com.redacted.MainActivity;sleep 4;done

while the sleep time you can enter the pin 2 times and again the main activity will be called so you can enter pin again

Impact :- mobile auth pin rate limiting bypassed

No thanks for reading ..!
