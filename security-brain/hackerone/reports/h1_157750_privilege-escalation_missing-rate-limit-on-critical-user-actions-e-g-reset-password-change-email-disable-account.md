---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '157750'
original_report_id: '157750'
title: Missing rate limit on critical user actions e.g. reset password, change email,
  disable account.
weakness: Privilege Escalation
team_handle: security
created_at: '2016-08-09T03:33:15.107Z'
disclosed_at: '2019-04-11T18:20:39.979Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Missing rate limit on critical user actions e.g. reset password, change email, disable account.

## Metadata

- HackerOne Report ID: 157750
- Weakness: Privilege Escalation
- Program: security
- Disclosed At: 2019-04-11T18:20:39.979Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi

I found that there are no rate limitations present on actions that require a password inside the account settings.
Actions:
[Paypal email change](https://hackerone.com/settings/bounties)
[Account email change](https://hackerone.com/settings/email/edit)
[Password Change](https://hackerone.com/settings/pass/edit)
[Disable Account](https://hackerone.com/settings/disable) *(this will not be useful to attacker)*

These sensitive actions require additional verification of password so as to protect the user even if the account is left open and is accessed by an attacker.
The attacker can try the dictionary attack *(or infinite wild guessing)*  with multiple threads on password on any of these actions without getting rate limited or locked out.

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
