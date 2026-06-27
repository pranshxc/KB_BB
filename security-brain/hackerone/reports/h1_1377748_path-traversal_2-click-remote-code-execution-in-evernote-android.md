---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1377748'
original_report_id: '1377748'
title: 2 click Remote Code execution in Evernote Android
weakness: 'Path Traversal: ''.../...//'''
team_handle: evernote
created_at: '2021-10-21T16:08:18.194Z'
disclosed_at: '2022-03-29T13:54:09.372Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 23
asset_identifier: com.evernote.android
asset_type: GOOGLE_PLAY_APP_ID
max_severity: none
tags:
- hackerone
- path-traversal
---

# 2 click Remote Code execution in Evernote Android

## Metadata

- HackerOne Report ID: 1377748
- Weakness: Path Traversal: '.../...//'
- Program: evernote
- Disclosed At: 2022-03-29T13:54:09.372Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

This vulnerability is similar to my previous reported vulnerability #1362313 , in here also weakness is path transversal  vulnerability which helps me to acheive code execution but the root cause is different.

some part of this app is written in java and some parts are written in react native. 

In evernote we can share notes and notebooks with others. In  notes we can also add attachments and there is option to rename the added attachment. When renaming i founded that special characters are not restricted,for example file uploaded with name `libjnigraphics.so`  can be renamed to `../../../lib-1/libjnigraphics.so` and when the attachment is downloaded it is downloaded with filename `../../../lib-1/libjnigraphics.so`.
The evernote android app also does not sanitize the received filename, so when user clicks on attachment,instead of attachment getting downloaded in `/data/data/com.evernote/cache/preview/:UUID/` this directory it is downloaded into   `/data/data/com.evernote/lib-1/libjnigraphics.so` which results into remote code execution.

> #1362313 report vulnerability root cause was that the app was not sanatizing the value of `_display_name ` from the provider of received `content://` uri that  resulted into ACE.

> This report's  root cause is that app is extracting attachment filename from `content-disposition` header  eg:- `content-disposition: attachment; filename="../../../lib-1/libjnigraphics.so"`  and the evernote app is  not sanatizing the received filename from the response header. 
The attachment download logic is written in react-native and the source file is compiled into hermes javascript bytecode, so i am not able to show the exact vulnerable code like i did in my last report.

The conclusion i reached was that fixing this report #1362313 bug will not fix this vulnerability so i am writing a new report.




## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Add the native-library poc file to a note {F1489257}
  2. Rename the attachment to `../../../lib-1/libjnigraphics`.
  2. Invite the victim to your note.

  Step 2 is needed,i don't know why `Shareable link` feature is not working on evernote android app without sending an invitation
 3. Click on 3 dots > copy internal link > copy web link OR copy app link(which is android deeplink and can be triggred from websites)
 4. Send link to victim and open the link (1st click)
 5. Click on attachment when note is opened (2nd click)
 6. Close the evernote app and open it again.
From adb shell run nc 127.0.0.1 6666
* use physical device because i have provided the arm64 architecture native library

>POC VIDEO
{F1489256}

## Impact

remote code execution in evernote android app with 2 clicks.

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
