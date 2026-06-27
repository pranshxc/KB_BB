---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1082521'
original_report_id: '1082521'
title: Full Path Disclosure of Server through 500 Server Error
weakness: Information Disclosure
team_handle: kartpay
created_at: '2021-01-20T15:41:43.021Z'
disclosed_at: '2021-08-16T17:46:04.025Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
asset_identifier: '*.kartpay.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Full Path Disclosure of Server through 500 Server Error

## Metadata

- HackerOne Report ID: 1082521
- Weakness: Information Disclosure
- Program: kartpay
- Disclosed At: 2021-08-16T17:46:04.025Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello team,

EXPLANATION
============
I found a interesting vulnerability into your site that it unexpected disclosing the server path where the PHP files are being hosted. When application sends account verification links in email then if anyone tries to verify his account with that link at a twice then on the title of the website the whole server path is disclosing through 500 Server Error.

Vulnerable Path :
---------------
`/usr/share/ngnix/website/resources/view/auth/create_password.blade.php`


I have added a POC .

## Impact

1. Server Information Disclosure

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
