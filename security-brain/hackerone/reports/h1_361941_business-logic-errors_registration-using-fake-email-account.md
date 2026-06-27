---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '361941'
original_report_id: '361941'
title: REGISTRATION USING FAKE EMAIL ACCOUNT
weakness: Business Logic Errors
team_handle: liberapay
created_at: '2018-06-05T00:35:56.219Z'
disclosed_at: '2018-06-05T11:13:32.484Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
asset_identifier: '*.liberapay.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# REGISTRATION USING FAKE EMAIL ACCOUNT

## Metadata

- HackerOne Report ID: 361941
- Weakness: Business Logic Errors
- Program: liberapay
- Disclosed At: 2018-06-05T11:13:32.484Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

1. Go to page https://liberapay.com/sign-up
2. Input email address (I tried to register with some email address)
     * a@a.a
     * b@b.b
     * c@c.c
     * d@d.d
     * e@e.e
3. Select the currency you want to use
4. click "GO" button
5. Will automatically enter into account without going through the process of verification email address first


NOTE:
* Email addresses can be verified before or after a user enters the system

## Impact

Allows an attacker to flood the database with a fake account that is registered with an invalid email

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
