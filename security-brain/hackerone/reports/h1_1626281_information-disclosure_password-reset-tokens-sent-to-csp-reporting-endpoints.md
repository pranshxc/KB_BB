---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1626281'
original_report_id: '1626281'
title: Password reset tokens sent to CSP reporting endpoints
weakness: Information Disclosure
team_handle: snapchat
created_at: '2022-07-05T14:20:34.245Z'
disclosed_at: '2022-08-31T23:53:18.606Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
asset_identifier: accounts.snapchat.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Password reset tokens sent to CSP reporting endpoints

## Metadata

- HackerOne Report ID: 1626281
- Weakness: Information Disclosure
- Program: snapchat
- Disclosed At: 2022-08-31T23:53:18.606Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Description:
It has been identified that the application is leaking referrer token to third party sites. In this case it was found that the password reset token is being leaked to third party sites which is a issue knowing the fact that it can allow any malicious users to use the token and reset the passwords of the victim.

Steps To Reproduce:-
1) Request a password reset link for a valid account
2) Click on the reset link
3) Before resetting the password, go burp suite and search the Reset token
4) Now, you see in the third party site leakage reset token.

Similler resource Bug :
https://hackerone.com/reports/272379
https://hackerone.com/reports/1177287

## Impact

Password reset token leak on third party website.

Thanks

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
