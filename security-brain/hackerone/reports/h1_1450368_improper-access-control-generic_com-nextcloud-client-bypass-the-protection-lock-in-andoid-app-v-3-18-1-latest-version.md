---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1450368'
original_report_id: '1450368'
title: com.nextcloud.client bypass the protection lock in andoid app v 3.18.1 latest
  version.
weakness: Improper Access Control - Generic
team_handle: nextcloud
created_at: '2022-01-15T12:18:26.733Z'
disclosed_at: '2022-04-30T11:56:31.540Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
asset_identifier: com.nextcloud.client
asset_type: GOOGLE_PLAY_APP_ID
max_severity: medium
tags:
- hackerone
- improper-access-control-generic
---

# com.nextcloud.client bypass the protection lock in andoid app v 3.18.1 latest version.

## Metadata

- HackerOne Report ID: 1450368
- Weakness: Improper Access Control - Generic
- Program: nextcloud
- Disclosed At: 2022-04-30T11:56:31.540Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
nextcloud allowed multiple account within the android client app on a single lock 


## Steps To Reproduce:
1.open nextcloud app 
2.add security password to protect the app 
3.close the app 
   again open the app and now show the password to open the app 

  1. so now the password protection bypass lets start
  2.hold the nextcloud app and see the app info open it
  3.Here the three option 1.open.2.uninstall and 3.force stop
now click open button and now see the app lock protection in the app and now open app and back open and back between 3 to 4 time 
same procedure and now you will see the app lock protection bypass in nextcloud android app

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

## Impact

if an attacker has physical access to an android mobile without screen lock,but with nextcloud installed and set up,he can easily access the nextcloud-files.


regards:Javed Ahmad

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
