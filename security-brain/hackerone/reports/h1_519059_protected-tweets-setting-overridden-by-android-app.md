---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '519059'
original_report_id: '519059'
title: Protected Tweets setting overridden by Android app
team_handle: x
created_at: '2019-03-30T13:55:11.669Z'
disclosed_at: '2019-05-17T18:08:02.377Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
asset_identifier: com.twitter.android
asset_type: GOOGLE_PLAY_APP_ID
max_severity: critical
tags:
- hackerone
---

# Protected Tweets setting overridden by Android app

## Metadata

- HackerOne Report ID: 519059
- Weakness: 
- Program: x
- Disclosed At: 2019-05-17T18:08:02.377Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** Protected Tweets setting overridden by Android app

**Description:** The Android app overrides the "Protect your Tweets" setting set from outside the app in some cases when changing other settings.

## Steps To Reproduce:

  1. Log in to an account with unprotected tweets on the Android app.
  1. Log in to the same account on mobile.twitter.com and turn on protected tweets.
  1. Confirm that the account's tweets are protected.
  1. In the Android app, go to the Direct Messages tab, click the gear icon and change a setting such as "Receive message requests" or "Show read receipts."
  1. The account's tweets are now unprotected.

If this does not work, you may have to first explicitly unset the protected tweets setting in the Android app before setting it elsewhere.

## Impact:

This can cause a user's tweets to unknowingly become public. It is possible this could be exploited by an attacker asking the user to change their settings but that is less likely to succeed than with the previous bug where only changing the email address was required.

## Impact

See above.

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
