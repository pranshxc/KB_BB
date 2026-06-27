---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '507012'
original_report_id: '507012'
title: bypass Claudflare access crm.mautic.com
team_handle: unikrn
created_at: '2019-03-08T23:55:17.115Z'
disclosed_at: '2019-04-05T09:25:33.587Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
asset_identifier: crm.unikrn.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# bypass Claudflare access crm.mautic.com

## Metadata

- HackerOne Report ID: 507012
- Weakness: 
- Program: unikrn
- Disclosed At: 2019-04-05T09:25:33.587Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi @unikrn!

Hello, I see that when you switch to the crm,unikrn.com, login attempts are filtered by Claudflare Access
to avoid brute-force account attacks, but we can ByPASS Claudflare access. Example:

https://crm.unikrn.com/oauth/v2/authorize_login

## Impact

having accounts, we can easily get into the admin area

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
