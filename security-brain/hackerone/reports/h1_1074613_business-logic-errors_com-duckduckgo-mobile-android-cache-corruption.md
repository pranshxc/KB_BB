---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1074613'
original_report_id: '1074613'
title: com.duckduckgo.mobile.android - Cache corruption
weakness: Business Logic Errors
team_handle: duckduckgo
created_at: '2021-01-08T18:52:34.355Z'
disclosed_at: '2021-09-26T23:08:52.356Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
asset_identifier: com.duckduckgo.mobile.android
asset_type: GOOGLE_PLAY_APP_ID
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# com.duckduckgo.mobile.android - Cache corruption

## Metadata

- HackerOne Report ID: 1074613
- Weakness: Business Logic Errors
- Program: duckduckgo
- Disclosed At: 2021-09-26T23:08:52.356Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
By opening a special url, the app cache can be corrupted which can't be resolved by the user without reinstalling the app.

## Steps To Reproduce:
1.) Download and install the DuckDuckGo App
2.) Open `https://%22t.dev/`
3.) Try to reopen the app (The app keeps crashing)

## Additional information
- Tested on Android 8.1 and 9 with the latest app release (5.73.0)
- Problematic seems to be the encoded `"` (%22)

## Mitigation
- Store the url urlencoded

## Impact

An attacker can corrupt someones app cache and prevent the user from continuing using the app.

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
