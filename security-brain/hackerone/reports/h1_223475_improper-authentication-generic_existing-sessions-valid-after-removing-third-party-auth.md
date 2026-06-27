---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '223475'
original_report_id: '223475'
title: Existing sessions valid after removing third party auth
weakness: Improper Authentication - Generic
team_handle: weblate
created_at: '2017-04-24T15:11:10.094Z'
disclosed_at: '2017-06-16T14:16:34.266Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- improper-authentication-generic
---

# Existing sessions valid after removing third party auth

## Metadata

- HackerOne Report ID: 223475
- Weakness: Improper Authentication - Generic
- Program: weblate
- Disclosed At: 2017-06-16T14:16:34.266Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi team,

I noticed an authentication break when logging in with 3rd party credentials in https://hosted.weblate.org/

POC

1 access https://hosted.weblate.org/accounts/profile/#auth> link to a Google account (for example)
2 on other device access the same account using Google credentials
3 return to the device of step 1> remove the Google account at https://hosted.weblate.org/accounts/profile/#auth> disconnect

The session remains active on the device in step 2. So I continue with a valid session from credentials not linked to any account at https://hosted.weblate.org

Please check it.

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
