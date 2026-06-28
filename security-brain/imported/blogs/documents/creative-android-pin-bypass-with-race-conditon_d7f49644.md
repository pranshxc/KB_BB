---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-18_creative-android-pin-bypass-with-race-conditon.md
original_filename: 2020-07-18_creative-android-pin-bypass-with-race-conditon.md
title: Creative Android pin bypass with Race conditon
category: documents
detected_topics:
- command-injection
- race-condition
- mobile-security
tags:
- imported
- documents
- command-injection
- race-condition
- mobile-security
language: en
raw_sha256: d7f49644a69e6fa0842e69ff215aab1b4fb2d989ac13fa1dae53ecfc9469d3b9
text_sha256: 1f157fa2ea2528f423c15ad49881a8a0bca0fedebf3b1b575518fc3e83400d4a
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Creative Android pin bypass with Race conditon

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-18_creative-android-pin-bypass-with-race-conditon.md
- Source Type: markdown
- Detected Topics: command-injection, race-condition, mobile-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `d7f49644a69e6fa0842e69ff215aab1b4fb2d989ac13fa1dae53ecfc9469d3b9`
- Text SHA256: `1f157fa2ea2528f423c15ad49881a8a0bca0fedebf3b1b575518fc3e83400d4a`


## Content

---
title: "Creative Android pin bypass with Race conditon"
url: "https://medium.com/@balook/creative-android-pin-bypass-with-race-conditon-63a8bc3f0e31"
authors: ["Baluz (@t3chman)"]
bugs: ["Race condition", "Authentication bypass"]
publication_date: "2020-07-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4401
scraped_via: "browseros"
---

# Creative Android pin bypass with Race conditon

Creative Android pin bypass with Race conditon
baluz
Follow
1 min read
·
Jul 18, 2020

54

Hitting main activity multiple times app allowing to view any activity inside an app. without even entering the mobile pin.

Bug ;-

Application has a mobile pin security. without entering the pin you cant enter into the app.

Bypass :-

Get baluz’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

But by calling internal activities like settings.activity and notifications.activity with race condition . The app is showing settings page ,profile page. but the problem is it only allow us to see for some seconds.So we need to automate it and take the screen shot by calling the activites .

for i in $(seq 20);do adb shell am start -a android.intent.action.VIEW -n com.redacted.android/.MainActivity -d "https://redacted.com/notifications";adb shell screencap /sdcard/tmp/$i.png;done

The above command run 20 times and take screen shot of frontend and save it in sdcard directory.

Impact :

Attacker cant bypass the pin completely . but can view the content inside the app and know the sensitive info like . amount, profile info

NO thanks for reading
