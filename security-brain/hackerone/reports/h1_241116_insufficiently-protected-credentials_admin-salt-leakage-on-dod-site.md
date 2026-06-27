---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '241116'
original_report_id: '241116'
title: Admin Salt Leakage on DoD site.
weakness: Insufficiently Protected Credentials
team_handle: deptofdefense
created_at: '2017-06-18T02:20:55.198Z'
disclosed_at: '2019-12-02T18:59:43.866Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- insufficiently-protected-credentials
---

# Admin Salt Leakage on DoD site.

## Metadata

- HackerOne Report ID: 241116
- Weakness: Insufficiently Protected Credentials
- Program: deptofdefense
- Disclosed At: 2019-12-02T18:59:43.866Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi there, the login page located at https://█████████/████████/adminapi/administrator.cfc is leaking administrator salt which is required at authentication purpose.

#PoC:
Navigate to `https://████/████████/adminapi/administrator.cfc?method=getSalt` which will show you the admin salt  `████████` which is required for further authentication.

#Impact:
With help of salt and some other info an attacker easily bypass login by using simple hash cracking tools and get access to admin panel

#Fix:
Direct access to getSalt method should be prohibited.

Let me know if any further info is required.

Regards,
Mr_R3boot.

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
