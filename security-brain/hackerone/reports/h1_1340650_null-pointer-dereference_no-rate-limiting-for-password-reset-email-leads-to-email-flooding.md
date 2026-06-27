---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1340650'
original_report_id: '1340650'
title: No Rate Limiting for Password Reset Email Leads to Email Flooding
weakness: NULL Pointer Dereference
team_handle: upchieve
created_at: '2021-09-15T16:51:40.065Z'
disclosed_at: '2022-03-26T17:58:04.540Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 1
asset_identifier: hackers.upchieve.org
asset_type: URL
max_severity: critical
tags:
- hackerone
- null-pointer-dereference
---

# No Rate Limiting for Password Reset Email Leads to Email Flooding

## Metadata

- HackerOne Report ID: 1340650
- Weakness: NULL Pointer Dereference
- Program: upchieve
- Disclosed At: 2022-03-26T17:58:04.540Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

There is "No Rate Limiting" implemented in sending the Password Reset Email. Thus, attacker can use this Vulnerability to bomb out the Email Inbox of the victim.
Affected URL : https://hackers.upchieve.org/resetpassword

Steps to Reproduce: 
1. Log In to : https://hackers.upchieve.org/
2. Go To : https://hackers.upchieve.org/resetpassword
3. Enter Email to reset password and click Enter and Capture the request on Burp Suite.
4. Send the captured request to Intruder and repeat the request in loop
5. Then just check the Email, your email will be flooded by UPchieve Reset Password Email.

Remediation :
Rate limiting should be implemented to Prevent Email Flooding.

## Impact

Email Flooding can create Trouble to the users on the website because huge email bombing can be done by the attackers within seconds.

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
