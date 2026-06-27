---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '407973'
original_report_id: '407973'
title: Weak Password Policy on Signup at https://accounts.bistudio.com/auth
weakness: Violation of Secure Design Principles
team_handle: bohemia
created_at: '2018-09-10T16:28:06.402Z'
disclosed_at: '2018-09-18T14:10:18.024Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 6
asset_identifier: Domain listed in the policy scope
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Weak Password Policy on Signup at https://accounts.bistudio.com/auth

## Metadata

- HackerOne Report ID: 407973
- Weakness: Violation of Secure Design Principles
- Program: bohemia
- Disclosed At: 2018-09-18T14:10:18.024Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi,
I found that you are using a weak password policy! Because user can set his password same as Email address!

Steps To reproduce:

1. Register an account with Email address "xyz@gmail.com"
2. Also password "xyz@gmail.com". 

You can see both values are same. You will become successfully register with these information which can easily guessable by anyone. Kindly restrict user that password should be same as Email address!

Thanks,

## Impact

Password should not match with Email address because if password is same as Email address then account can be compromise easily!

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
