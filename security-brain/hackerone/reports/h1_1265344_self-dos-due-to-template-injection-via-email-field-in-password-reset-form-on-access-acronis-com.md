---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1265344'
original_report_id: '1265344'
title: Self-DoS due to template injection via email field in password reset form on
  access.acronis.com
team_handle: acronis
created_at: '2021-07-16T12:29:55.428Z'
disclosed_at: '2022-05-03T06:41:50.169Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
asset_identifier: '*.acronis.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
---

# Self-DoS due to template injection via email field in password reset form on access.acronis.com

## Metadata

- HackerOne Report ID: 1265344
- Weakness: 
- Program: acronis
- Disclosed At: 2022-05-03T06:41:50.169Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary
HI acronis security team , how are you
I hope everyone is OK in the other side of the screen .
I found Template Injection in [https://access.acronis.com/reset_password/new] via the mail input .

## Steps To Reproduce:

 1. Open [https://access.acronis.com/reset_password/new] and Enter the mail Payload : sudo_bash{{8*8}}@wearehackerone.com
 2. After submite the mail , The resulte will Reflect in the page with the mail adress .

## Impact

- AngularJs CCTI may lead to xss .

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
