---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '146424'
original_report_id: '146424'
title: No Rate Limiting on stats.nextcloud.com login
weakness: Violation of Secure Design Principles
team_handle: nextcloud
created_at: '2016-06-22T09:34:15.510Z'
disclosed_at: '2016-06-22T11:40:19.223Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 11
tags:
- hackerone
- violation-of-secure-design-principles
---

# No Rate Limiting on stats.nextcloud.com login

## Metadata

- HackerOne Report ID: 146424
- Weakness: Violation of Secure Design Principles
- Program: nextcloud
- Disclosed At: 2016-06-22T11:40:19.223Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

There is no defenses or any lockout mechanism on stats.nextcloud.com login , a malicious minded user can continue guessing an account password limitless, and this might cause to completely compromised the site.

__Recommendation: Put a rate limit or a any lockout mechanism__

Regards
Japz

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
