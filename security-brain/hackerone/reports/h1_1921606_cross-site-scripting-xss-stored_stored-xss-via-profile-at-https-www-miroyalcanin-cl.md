---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1921606'
original_report_id: '1921606'
title: Stored XSS via ' profile ' at https://www.miroyalcanin.cl/
weakness: Cross-site Scripting (XSS) - Stored
team_handle: mars
created_at: '2023-03-28T15:45:33.764Z'
disclosed_at: '2023-06-23T14:59:03.530Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
asset_identifier: '*.miroyalcanin.cl'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS via ' profile ' at https://www.miroyalcanin.cl/

## Metadata

- HackerOne Report ID: 1921606
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: mars
- Disclosed At: 2023-06-23T14:59:03.530Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

hi team 
i found stored xss on profile 

1. Go to registration page  (https://www.miroyalcanin.cl/)
2. Verified your account.
3. Go to login page and login your account.

For the fastly test, use this credentials to login (my test account)

* For Attacker 

email: deweha7916@mitigado.com
pass: Password
* For Victime

email: povik23037@cyclesat.com
pass: password

After login i change animal name to payload xss .. i open victime account and i put attacker profile url so i succeeded.

{F2258722}

## Impact

Stored Cross Site Scripting which attacker can execute malicious javascript payload.

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
