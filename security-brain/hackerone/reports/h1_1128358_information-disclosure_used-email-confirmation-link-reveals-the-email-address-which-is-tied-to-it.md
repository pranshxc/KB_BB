---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1128358'
original_report_id: '1128358'
title: Used email confirmation link reveals the email address which is tied to it
weakness: Information Disclosure
team_handle: security
created_at: '2021-03-16T20:39:50.458Z'
disclosed_at: '2021-09-22T19:24:19.724Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 21
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Used email confirmation link reveals the email address which is tied to it

## Metadata

- HackerOne Report ID: 1128358
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2021-09-22T19:24:19.724Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
If an attacker finds an used email confirmation link (the token is in URL) s/he will be able to see the email address which is tied to the confirmation link ID. The attack itself is pretty unlikely but the application should show the generic error message like `The confirmation ID is invalid` or something like that.

## Steps To Reproduce:

- Register a new account to the service
- Confirm the email address
- Reuse the confirmation link (this can be done like 24 hours after confirmation has been done)
- See that the page shows the email address which is tied to the confirmation link

Note: The confirmation ID is part of URL so it can be leak in different ways. 

## Recommendation:

Once the confirmation link is used the application should reveal the generic error message like `The confirmation ID is invalid`
 

## References:

-

## Impact

The used email confirmation links reveals the email address which is tied to it

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
