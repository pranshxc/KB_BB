---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '699200'
original_report_id: '699200'
title: Signup with any email and enable 2FA without verifying email
team_handle: omise
created_at: '2019-09-21T09:55:35.329Z'
disclosed_at: '2020-04-23T12:35:27.346Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 33
asset_identifier: dashboard.omise.co
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Signup with any email and enable 2FA without verifying email

## Metadata

- HackerOne Report ID: 699200
- Weakness: 
- Program: omise
- Disclosed At: 2020-04-23T12:35:27.346Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

##Description :
When i signup, i can enable 2FA without verification my email.

##Attack Scenario : 
1. The Attacker signup with the victim email.
2. Go to `Two factor authetication` and enable 2FA

## Impact

when the victim want to register in this [site](https://dashboard.omise.co/),  they can't, because they email claims by attacker.
and if the victim reset the password to get back the email, he can, but he can't login because need 2FA code.

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
