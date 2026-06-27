---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1596459'
original_report_id: '1596459'
title: Talk Android broadcast receiver is not protected by broadcastPermission allowing
  malicious apps to communicate
weakness: Improper Access Control - Generic
team_handle: nextcloud
created_at: '2022-06-10T06:54:22.394Z'
disclosed_at: '2022-12-25T11:23:57.479Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 15
asset_identifier: com.nextcloud.talk2
asset_type: GOOGLE_PLAY_APP_ID
max_severity: medium
tags:
- hackerone
- improper-access-control-generic
---

# Talk Android broadcast receiver is not protected by broadcastPermission allowing malicious apps to communicate

## Metadata

- HackerOne Report ID: 1596459
- Weakness: Improper Access Control - Generic
- Program: nextcloud
- Disclosed At: 2022-12-25T11:23:57.479Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Call to registerReceiver misses the broadcastPermission argument - no permissions will be checked for the broadcaster, which allows a malicious application to communicate with the broadcast receiver.

## Supporting Material/References:

  * Screenshot Snyk report
 * references to fixes in other repos

https://github.com/alvinhkh/buseta/commit/6b791de8e3622ef157b065f9c82fcfd5a0e2302a?diff=split#diff-a75527f97c6732197964c1dbf30fd385L66

https://github.com/serso/android-messengerpp/commit/1528fdc2d3561bab192dfde9a84a737a26a19fce?diff=split#diff-7ff52f2abe79bd0a68d54916fe71aef2L92

https://github.com/irccloud/android/commit/857287d6d9da443b0ff667505d5bf4a383922784?diff=split#diff-f06bf5e27b9130d322139330f7f31997L40

## Impact

Unsure, potentially interfere with call starts and audio/bluetooth setup

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
