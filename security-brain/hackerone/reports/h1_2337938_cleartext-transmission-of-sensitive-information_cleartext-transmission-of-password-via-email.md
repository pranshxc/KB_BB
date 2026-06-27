---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2337938'
original_report_id: '2337938'
title: Cleartext Transmission of password via Email
weakness: Cleartext Transmission of Sensitive Information
team_handle: sheer_bbp
created_at: '2024-01-28T14:57:16.446Z'
disclosed_at: '2024-04-22T04:21:38.560Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 63
asset_identifier: www.sheer.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cleartext-transmission-of-sensitive-information
---

# Cleartext Transmission of password via Email

## Metadata

- HackerOne Report ID: 2337938
- Weakness: Cleartext Transmission of Sensitive Information
- Program: sheer_bbp
- Disclosed At: 2024-04-22T04:21:38.560Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
After successfully signup as a fan, the password was then sent to email by cleartext

## Steps To Reproduce:
1. After successfully signup as a fan, check the email and see that the password was sent in cleartext, it does not appear in the UI, just F12 and you can see the user password
{F3012123}

## Impact

If the mail channel was sniffed, the attacker can compromise user accounts easily

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
