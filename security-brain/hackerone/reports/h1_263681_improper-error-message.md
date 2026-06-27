---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '263681'
original_report_id: '263681'
title: Improper error message
team_handle: legalrobot
created_at: '2017-08-26T19:54:26.552Z'
disclosed_at: '2017-09-01T21:59:02.649Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
asset_identifier: app.legalrobot.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Improper error message

## Metadata

- HackerOne Report ID: 263681
- Weakness: 
- Program: legalrobot
- Disclosed At: 2017-09-01T21:59:02.649Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi team,
First of all congrats for good work to enforced the new password security policy during registration but the password error banner is not updated as per the changes. During registration it only shows the error when i enter the password if is is less than 8 chars. but if i enter the 8+ chars error will say "Please fix this field.". Without knowing the exact error message it will be difficult to put good password. Same error message is showing while signing in.

1) Improper Error message in registration form                                                                                  
1. Click on register.
2. enter password 8+ characters ex. 12345678

2) Improper Error message in sign-in form                                                                                  
1. Click on register.
2. enter your old passowrd if it is simple. (Not possible to sign in)

Please fix this issue as soon as possible, Due to this user will know what's the real problem is happening during sign-in or during registration.

Thanks and regards,
Pratham

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
