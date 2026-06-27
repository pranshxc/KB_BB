---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1182465'
original_report_id: '1182465'
title: IDOR on www.acronis.com API lead to steal private business user information
weakness: Insecure Direct Object Reference (IDOR)
team_handle: acronis
created_at: '2021-05-02T13:44:17.493Z'
disclosed_at: '2021-08-31T10:14:06.732Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 27
asset_identifier: '*.acronis.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# IDOR on www.acronis.com API lead to steal private business user information

## Metadata

- HackerOne Report ID: 1182465
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: acronis
- Disclosed At: 2021-08-31T10:14:06.732Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary
Hi acronis team, i found an endpoint : `www.acronis.com/en-us/api/v1/lead/id:929-HVV-335&token:_mch-acronis.com-<integer value>` that is vulnerable to IDOR. with this vulnerability an attacker can steal private info such as company name, user name and surname, telephone number etc...

## Steps To Reproduce

  1. once logged in into account.acronis.com go to :  https://www.acronis.com/en-us/api/v1/lead/id:929-HVV-335&token:_mch-acronis.com-1614775941608-39235
  2. you will see all my private account information
  
███

NOTE: the only part that change from account to account is the last part of the token(the last 5 digits) and since it's an integer is totally guessable.

## Recommendations

implement a check on the endpoint or use a random token value instead of an integer

## Impact

an attacker can steal private info from other users profile

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
