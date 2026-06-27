---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '827484'
original_report_id: '827484'
title: Missing rate limit for current password field (Password Change) Account Takeover
weakness: Improper Restriction of Authentication Attempts
team_handle: acronis
created_at: '2020-03-23T18:14:29.766Z'
disclosed_at: '2020-10-06T09:46:08.759Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 33
asset_identifier: Other Acronis Domains
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# Missing rate limit for current password field (Password Change) Account Takeover

## Metadata

- HackerOne Report ID: 827484
- Weakness: Improper Restriction of Authentication Attempts
- Program: acronis
- Disclosed At: 2020-10-06T09:46:08.759Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Vulnerability:
Missing Rate Limit for Current Password field (Password Change) Account Takeover

Steps to reproduce the bug:
1)Go to Profile > Password. Enter any (wrong password) In current password filed.
2)Now enter the new password and Turn the Intercept ON.
3)Capture the request & Send the request to Intruder and add a Payload Marker on the current password value.
4)Add the payload for the password field having a list of more than 100 password or more for test and start attack.
BOOM!

Screen shot is attached as a proof of concept.

## Impact

There is no rate limit enabled for "Current Password" field on changing password on your website. A malicious minded user can continually tries to brute force an account password. If user forget to logout account in some public computer then attacker is able to know the correct password, and also able to change the password to new one by inputting large number of payloads.

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
