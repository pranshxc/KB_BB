---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1971610'
original_report_id: '1971610'
title: Logging in without knowing credentials after logged out action
team_handle: weblate
created_at: '2023-05-03T20:40:15.149Z'
disclosed_at: '2023-06-16T07:59:38.002Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
---

# Logging in without knowing credentials after logged out action

## Metadata

- HackerOne Report ID: 1971610
- Weakness: 
- Program: weblate
- Disclosed At: 2023-06-16T07:59:38.002Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi, I noticed weird behavior about logging in when preparing last report for you.
Repro steps: Log in using incognito/private mode on https://weblate.org/pl/ - click top right https://hosted.weblate.org/accounts/login/?next=/idp/login/process/ and use password-username.
As logged in on https://weblate.org/pl/ now log out - click top right icon (Logging out). Now logged out on https://weblate.org/pl/
But now, click again icon <a href="/saml2/login/?next=/pl/" class="user-tab user-anonymous"></a>
See logged in without interaction - like type password/credentials.

Additional information:
Checked with different browsers like Firefox and Chromium based.
You can many times logging out and just clicking icon (steps above) - be logged in.

Best regards,

## Impact

Scenario: user logging out so thinks is properly logged out, next person just clicks mentioned icon and is logged in as previous user without knowing credentials.
Possible sensitive data exposure / ATO.

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
