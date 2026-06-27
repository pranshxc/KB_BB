---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '229869'
original_report_id: '229869'
title: Adding Email lacks Password validation
team_handle: weblate
created_at: '2017-05-19T12:58:19.664Z'
disclosed_at: '2017-06-28T02:12:18.989Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
---

# Adding Email lacks Password validation

## Metadata

- HackerOne Report ID: 229869
- Weakness: 
- Program: weblate
- Disclosed At: 2017-06-28T02:12:18.989Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Affected URL:
https://demo.weblate.org/accounts/email/

## Issue:
The account section of profile says: "You can add another email address on the Authentication tab." But there is no option of adding another email in Authentication. 
However, I was able to guess the above endpoint.
The problem here is, the site lacks password validation for sensitive action like adding email id.

## Impact: 
The impact of the issue is similar to letting user change password without asking for old password.
If any more info is needed feel free to contact me. :D

Regards,
Abiral

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
