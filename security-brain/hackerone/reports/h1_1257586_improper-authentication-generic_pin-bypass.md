---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1257586'
original_report_id: '1257586'
title: PIN 📌 BYPASS 🥷
weakness: Improper Authentication - Generic
team_handle: yoti
created_at: '2021-07-11T17:08:43.731Z'
disclosed_at: '2022-03-18T22:25:25.806Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 72
asset_identifier: '983980808'
asset_type: APPLE_STORE_APP_ID
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# PIN 📌 BYPASS 🥷

## Metadata

- HackerOne Report ID: 1257586
- Weakness: Improper Authentication - Generic
- Program: yoti
- Disclosed At: 2022-03-18T22:25:25.806Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Summary:

 983980808 IOS App has improper rate limit.

When we try to brute force the PIN, we are rate limited for 5 minutes after 5 or 6 attempt.

In my testing I found that it was checking the device's local date / time so by changing it we can brute force the PIN.

Steps To Reproduce:

1.Install 983980808  IOS APP from IOS APP store.
2.Create your PIN.
3.Now open again your 983980808 IOS App
4.You will be asked to enter the PIN.
5.Try to brute force the code. You will see a message to try again after 5 min.
6.Now change the date / time of your device.
7.Observe there is no rate limit now.

POC video : IMG_7755.MP4

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
