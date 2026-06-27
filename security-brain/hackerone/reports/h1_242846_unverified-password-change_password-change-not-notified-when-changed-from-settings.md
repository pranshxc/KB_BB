---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '242846'
original_report_id: '242846'
title: Password Change not notified when changed from settings
weakness: Unverified Password Change
team_handle: starbucks
created_at: '2017-06-24T08:34:18.654Z'
disclosed_at: '2019-02-08T19:09:55.689Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 7
asset_identifier: www.starbucks.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- unverified-password-change
---

# Password Change not notified when changed from settings

## Metadata

- HackerOne Report ID: 242846
- Weakness: Unverified Password Change
- Program: starbucks
- Disclosed At: 2019-02-08T19:09:55.689Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi,

Password change is not notified to the account owner if its made from the account settings. This is very crucial as once the account is compromised, the attacker can change the password without giving any clue to the victim.

Steps to reproduce the issue:

1. Sign in with a valid username and password to www.starbucks.com
2. Go to your settings and personal info.
3. click change your password
4. Change your password
5. Looks for notification in your email.
6. No emails are sent.

Can be reproducible with all valid accounts.

Password changed via the forgot password reset flows are notified while this notification is missing. 

Thanks,
Karthik

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
