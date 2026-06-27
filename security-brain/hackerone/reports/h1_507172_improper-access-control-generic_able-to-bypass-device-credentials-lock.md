---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '507172'
original_report_id: '507172'
title: Able to bypass "Device credentials" Lock
weakness: Improper Access Control - Generic
team_handle: nextcloud
created_at: '2019-03-09T16:46:38.527Z'
disclosed_at: '2019-07-26T07:47:28.854Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
asset_identifier: com.nextcloud.client
asset_type: GOOGLE_PLAY_APP_ID
max_severity: medium
tags:
- hackerone
- improper-access-control-generic
---

# Able to bypass "Device credentials" Lock

## Metadata

- HackerOne Report ID: 507172
- Weakness: Improper Access Control - Generic
- Program: nextcloud
- Disclosed At: 2019-07-26T07:47:28.854Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Prepare
1. Enable "Device credentials" lock via the settings. (I'm using fingerprint in my case)
2. Test if this works by closing the app and open it again.
3.  If this works close the app again, do a force close to make sure the application is closed.

## The next steps need to be done quickly right after each other.
1. Make sure you are able to quickly start the Nextcloud app, i put mine on the homescreen.
2. Now quickly open the app and press backspace and open the app and press backspace, do this a few times right after each other until you see a flash of the folder list.
3. After you have seen this folder tree flash, you can start the application without any credentials.

Note: This only happens when doing this fast, else this won't work.
I added a adb logcat output of the nextcloud process i started during my test.

## Impact

The impact is that someone without the correct credentials but an unlocked phone is still able to login to the Nextcloud app and see all the files of the user.

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
