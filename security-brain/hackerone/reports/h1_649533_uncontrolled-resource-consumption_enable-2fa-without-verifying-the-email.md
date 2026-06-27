---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '649533'
original_report_id: '649533'
title: Enable 2FA without verifying the email
weakness: Uncontrolled Resource Consumption
team_handle: moneybird
created_at: '2019-07-18T16:21:16.837Z'
disclosed_at: '2019-10-25T08:13:30.342Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 127
asset_identifier: moneybird.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Enable 2FA without verifying the email

## Metadata

- HackerOne Report ID: 649533
- Weakness: Uncontrolled Resource Consumption
- Program: moneybird
- Disclosed At: 2019-10-25T08:13:30.342Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

# Description : 
I able to add 2FA to my account without verifying my email

# Attack scenario : 
1. Attacker sign up with victim email (Email verification will be sent to victim email).
2. Attacker able to login without verifying email.
3. Attacker add 2FA.

## Impact

the victim can't register an account with victim email. If the victim reset the password, the password will change, but the victim can't login because 2FA.

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
