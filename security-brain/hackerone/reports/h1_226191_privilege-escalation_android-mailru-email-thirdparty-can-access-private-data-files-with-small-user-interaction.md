---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '226191'
original_report_id: '226191'
title: 'Android MailRu Email: Thirdparty can access private data files with small
  user interaction'
weakness: Privilege Escalation
team_handle: mailru
created_at: '2017-05-04T20:35:14.198Z'
disclosed_at: '2018-01-02T18:01:25.040Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
asset_identifier: ru.mail.mailapp
asset_type: GOOGLE_PLAY_APP_ID
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Android MailRu Email: Thirdparty can access private data files with small user interaction

## Metadata

- HackerOne Report ID: 226191
- Weakness: Privilege Escalation
- Program: mailru
- Disclosed At: 2018-01-02T18:01:25.040Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello, Team


Domain, site, application
---
Android Mail.Ru Email v. 5.5.1.21258


Testing environment
---
Tested on non rooted Nexus 5x Android 7.1.2, 


Intro
---
I found that #90693 was fixed incompletely and additionaly the attack can be improved using self sending activity.


Steps
---
1. Create some word readable file in "/data/data/thirdparty/file.txt"
2. Create soft link on that file "/data/data/thirdparty/link.txt"
3. Send this soft via Intent.EXTRA_STREAM to the Mail.Ru "ru.mail.ui.writemail.MailToMySelfActivity"
4. After some delay, for example 1000ms, remove soft link and create new, but which will point at any file from "/data/data/ru.mail.mailapp/*". Pay attention, that MailToMySelfActivity is do sending automatically and you need find for your PoC delay which will fit in time. (Or you can use ru.mail.ui.writemail.SharingActivity)
5. The message will be sent. If user will open that message than attachment will be downloaded automatically into the "/sdcard/Android/data/ru.mail.mailapp/...." folder. 
6. It means that any app will be able to read this attachment data which may contain private file content, for example message database.


PoC
---
I attach PoC source
Video link (accessed only by url): https://youtu.be/tXAadbkhDCM

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*
