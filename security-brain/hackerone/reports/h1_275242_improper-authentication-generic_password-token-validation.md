---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '275242'
original_report_id: '275242'
title: password token validation
weakness: Improper Authentication - Generic
team_handle: wakatime
created_at: '2017-10-06T21:03:00.040Z'
disclosed_at: '2017-10-07T10:10:00.429Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- improper-authentication-generic
---

# password token validation

## Metadata

- HackerOne Report ID: 275242
- Weakness: Improper Authentication - Generic
- Program: wakatime
- Disclosed At: 2017-10-07T10:10:00.429Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello,
when I reset password all tokens are valid can be used, should keep valid only token in the last request or you can invalidate all reset links after using one of the requests successfully.

Steps:
1) go to the password reset page and request more than one request.
2) go to your email and use the first reset link.
3) you can change password successfully.

Please check it,
Thanks.

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
