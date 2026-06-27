---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '472013'
original_report_id: '472013'
title: Changing email address on Twitter for Android unsets "Protect your Tweets"
weakness: Privacy Violation
team_handle: x
created_at: '2018-12-26T01:46:22.366Z'
disclosed_at: '2019-01-18T16:49:29.340Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 116
asset_identifier: com.twitter.android
asset_type: GOOGLE_PLAY_APP_ID
max_severity: critical
tags:
- hackerone
- privacy-violation
---

# Changing email address on Twitter for Android unsets "Protect your Tweets"

## Metadata

- HackerOne Report ID: 472013
- Weakness: Privacy Violation
- Program: x
- Disclosed At: 2019-01-18T16:49:29.340Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

**Summary:** Verifying email address on Twitter for Android unsets "Protect your Tweets"

**Description:** Verifying a new email address on a Twitter account in the Android app causes the "Protect your Tweets" option to be unset, resulting in the user's tweets being made publicly visible.

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. Log in to a Twitter account on the Android app.
  2. Make sure the app is set to handle twitter.com links.
  3. Change the email address on the account.
  4. Verify the new email address by clicking the link in the email from the same Android device.

## Impact: This can lead to a user's private tweets being exposed to the public until they realize this happened. An attacker does not need to be involved as they would need to have access to the user's account to change the email, but a user could be tricked into changing their email if an attacker sent them a phishing email telling them to do so.
## Supporting Material/References:

  * List any additional material (e.g. screenshots, logs, etc.)

## Impact

This can lead to a user's private tweets being exposed to the public until they realize this happened. An attacker does not need to be involved as they would need to have access to the user's account to change the email, but a user could be tricked into changing their email if an attacker sent them a phishing email telling them to do so.

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
