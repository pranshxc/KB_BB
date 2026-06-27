---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1182016'
original_report_id: '1182016'
title: Email verification bypassed during sing up (████████)
weakness: Violation of Secure Design Principles
team_handle: mtn_group
created_at: '2021-05-01T16:00:30.930Z'
disclosed_at: '2021-08-19T15:50:43.553Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 17
asset_identifier: mtn.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Email verification bypassed during sing up (████████)

## Metadata

- HackerOne Report ID: 1182016
- Weakness: Violation of Secure Design Principles
- Program: mtn_group
- Disclosed At: 2021-08-19T15:50:43.553Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Normally ███ ask users to verify their email during registration but i found a way to bypass this so than an attacker can create accounts with emails that are not his own abusing the intigrity of MTN.
## Steps To Reproduce:

  1. Create an account with you owned email, verify it.
  1. Go ████ and change your email to the desired email you will not be asked to verify the ownership, in this case I changed mine to ```███████```.
  1. Email verification bypassed successfully.

## Supporting Material/References:

## Impact

This issue can be used to bypass email verification on signup. Attackers can create account on behalf on any person without having access to the email account.

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
