---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2088808'
original_report_id: '2088808'
title: Disavowed an email without any authentication
weakness: Improper Access Control - Generic
team_handle: liberapay
created_at: '2023-07-28T18:07:15.710Z'
disclosed_at: '2023-07-31T07:32:17.151Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 18
asset_identifier: '*.liberapay.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Disavowed an email without any authentication

## Metadata

- HackerOne Report ID: 2088808
- Weakness: Improper Access Control - Generic
- Program: liberapay
- Disclosed At: 2023-07-31T07:32:17.151Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hii team, I hope you are doing well.
While conducting my research I found that there are some URLs that leads to disavowing some account without any authentication.
It allows unauthorized users to disavow or dissociate an email address from an account without requiring proper authentication.

Steps to reproduce:
1. Put this command into your terminal:
waybackurls liberapay.com | grep disavow

This command will collect all the URLs related to liberapay.com and search for the specific keyword "disavow".

If you open one of the URLs you'll disavow an account without proper authorization.

## Impact

Unauthorized Account Access: Attackers can disassociate a legitimate email address from an account, potentially preventing the real owner from accessing their account.

Please let me know if you need more info.

Kind Regards
@sameersec

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
