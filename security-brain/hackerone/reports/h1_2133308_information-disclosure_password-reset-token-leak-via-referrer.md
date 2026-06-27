---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2133308'
original_report_id: '2133308'
title: Password Reset Token Leak Via Referrer
weakness: Information Disclosure
team_handle: liberapay
created_at: '2023-09-03T19:58:51.185Z'
disclosed_at: '2023-11-23T16:01:39.082Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 38
asset_identifier: '*.liberapay.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Password Reset Token Leak Via Referrer

## Metadata

- HackerOne Report ID: 2133308
- Weakness: Information Disclosure
- Program: liberapay
- Disclosed At: 2023-11-23T16:01:39.082Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

# Exploitation
Request password reset to your email address
Click on the password reset link
Dont change password
Click on about us
Intercept the request in burpsuite proxy
Check if the referer header is leaking password reset token.

# Impact
It allows the person who has control of particular site to change the user’s password (CSRF attack), because this person knows reset password token of the user.

# Reference:
https://hackerone.com/reports/342693
https://hackerone.com/reports/272379
https://hackerone.com/reports/737042
https://medium.com/@rubiojhayz1234/toyotas-password-reset-token-and-email-address-leak-via-referer-header-b0ede6507c6a
https://medium.com/@shahjerry33/password-reset-token-leak-via-referrer-2e622500c2c1

## Impact

It allows the person who has control of particular site to change the user’s password (CSRF attack), because this person knows reset password token of the user.

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
