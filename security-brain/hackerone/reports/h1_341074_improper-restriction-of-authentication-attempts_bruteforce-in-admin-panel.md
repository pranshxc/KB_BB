---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '341074'
original_report_id: '341074'
title: Bruteforce in admin panel
weakness: Improper Restriction of Authentication Attempts
team_handle: nextcloud
created_at: '2018-04-20T12:29:20.072Z'
disclosed_at: '2020-01-31T14:19:03.274Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
asset_identifier: nextcloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# Bruteforce in admin panel

## Metadata

- HackerOne Report ID: 341074
- Weakness: Improper Restriction of Authentication Attempts
- Program: nextcloud
- Disclosed At: 2020-01-31T14:19:03.274Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello there,
Admin panel of your website (https://nextcloud.com/wp-login.php) is vulnerable to bruteforce attacks as their is no rate-limiting.

## Impact

Can gain access to admin panel.
To fix this, Just add rate limiting.

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
