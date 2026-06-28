---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-11-05_bypass-video-capture-limit-on-ray-ban-stories.md
original_filename: 2021-11-05_bypass-video-capture-limit-on-ray-ban-stories.md
title: Bypass video capture limit on Ray-Ban Stories
category: documents
detected_topics:
- command-injection
- otp
- business-logic
- mobile-security
tags:
- imported
- documents
- command-injection
- otp
- business-logic
- mobile-security
language: en
raw_sha256: 7e7d0091e884b09b318210b6030618c49ce7110a0a5b3e3dd7160dcc39ef5c20
text_sha256: 86980637247ba4e2a1174a8ca359a85d83b0603ab3b191fe507a927cf1d2575d
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Bypass video capture limit on Ray-Ban Stories

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-11-05_bypass-video-capture-limit-on-ray-ban-stories.md
- Source Type: markdown
- Detected Topics: command-injection, otp, business-logic, mobile-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `7e7d0091e884b09b318210b6030618c49ce7110a0a5b3e3dd7160dcc39ef5c20`
- Text SHA256: `86980637247ba4e2a1174a8ca359a85d83b0603ab3b191fe507a927cf1d2575d`


## Content

---
title: "Bypass video capture limit on Ray-Ban Stories"
page_title: "Bypass video capture limit on Ray-Ban Stories - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/bypass-video-capture-limit-on-ray-ban-stories/"
final_url: "https://philippeharewood.com/bypass-video-capture-limit-on-ray-ban-stories/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw", "Android"]
bounty: "1,500"
publication_date: "2021-11-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3192
---

Posted on [November 5, 2021January 13, 2022](https://philippeharewood.com/bypass-video-capture-limit-on-ray-ban-stories/)

# Bypass video capture limit on Ray-Ban Stories

Meta Rayban Stories has lower-level settings to change via the _View_ (Assistant app) for example

  * enable Assistant
  * change inner LED notification level
  * change volume

Since the method for these settings are shared for other options defined in the firmware, it is possible to replace with a setting to change the duration of a video capture to longer than 30 seconds as advertised by Meta.  
  
Hook the STLMcuSettingHandler function which sends commands via Int32 values and replace them with our own.
  
  
  var writeSetting = ObjC.classes["STLMcuSettingHandler"]['- writeSetting:value:completion:']
  Interceptor.attach(writeSetting.implementation, {
  onEnter: function(args) {
  args[2] = ptr(0x8004)
  args[3] = ptr(0xea60)
  }
  });

Save as video-length.js and run the frida script with  
`frida -U View -l video-length.js`

In _View_ app settings under “System alerts” toggle one of the options e.g. the LED notification brightness

Instead of the options changed (UserLedAdaptiveBrightnessDisabled `0x8038` & UserLedManualBrightnessLevel `0x8037`) VideoCaptureDurationMs `0x8004` will be changed

This was found in the firmware under StellaWifiService.apk
  
  
  /system/priv-app/StellaWifiService/StellaWifiService/smali/stella/common/Uint32SettingsEnum.smali
  
  
  .field public static final VideoCaptureDurationMs:I = 0x8004
  

The next time a Rayban Stories owner uses the video capture feature, the new default capture length will be 60 seconds.  

> Small “bypass” in Meta (formerly known as Facebook) Rayban Stories. [pic.twitter.com/UsCcrDWrVz](https://t.co/UsCcrDWrVz)
> 
> — Philippe Harewood (@phwd_) [November 5, 2021](https://twitter.com/phwd_/status/1456505296881324032?ref_src=twsrc%5Etfw)

**Timeline**

Nov 5, 2021 – Report sent  
Nov 8, 2021 – Further investigation by Meta  
Nov 25, 2021 – Patched by Meta  
Dec 6, 2021 – $1500 Bounty awarded by Meta  
Jan 14, 2022 – Disclosed (As we are patching things client-side, we ask you to please refrain from publicly posting about the bug until Jan 14th, which should give our users sufficient time for our hotfix to be pushed)
