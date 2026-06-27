---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1242212'
original_report_id: '1242212'
title: PIN bypass
weakness: Improper Authentication - Generic
team_handle: myetherwallet
created_at: '2021-06-23T14:36:05.845Z'
disclosed_at: '2021-06-29T20:19:24.430Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 31
asset_identifier: mewwallet.android
asset_type: GOOGLE_PLAY_APP_ID
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# PIN bypass

## Metadata

- HackerOne Report ID: 1242212
- Weakness: Improper Authentication - Generic
- Program: myetherwallet
- Disclosed At: 2021-06-29T20:19:24.430Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:

MEW apk has improper rate limit.


When we try to brute force the PIN, we are rate limited for 5 minutes after 5 or 6 attempt.


In my testing I found that it was checking the device's local time so by changing it we can brute force the PIN.


## Steps To Reproduce:

1.Install MEW app from play store.

2.Create your PIN.

3.Now open again your MEW apk.

4.You will be asked to enter the PIN.

5.Try to brute force the code. You will see a message to try again after 5 min.

6.Now change the time of your device.

7.Observe there is no rate limit now.

## Supporting Material/References:


{F1350023}

## Impact

An attacker can brute force the PIN of an user

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
