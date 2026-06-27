---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '251918'
original_report_id: '251918'
title: 'Flash CSRF: Update Ad Frequency %: [cp-ng.pinion.gg]'
weakness: Cross-Site Request Forgery (CSRF)
team_handle: unikrn
created_at: '2017-07-21T01:46:13.074Z'
disclosed_at: '2017-09-06T06:31:38.932Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 31
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Flash CSRF: Update Ad Frequency %: [cp-ng.pinion.gg]

## Metadata

- HackerOne Report ID: 251918
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: unikrn
- Disclosed At: 2017-09-06T06:31:38.932Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

###Description:
-----------
Attacker can update the user's Ad Frequency % using flash + 307 redirect trick by making post request to particular endpoint.

###Step To Reproduce: 
-----------
+ Get logged at: https://cp-ng.pinion.gg
+ Visit: http://geekboy.ninja/poc/freq.swf
+ Ad Frequency should be updated.

*Note: for test i used my account with id `████`, as update request use userid in endpoint, it can be modified as per need.* 

{F205068}





Please let me know if any more info needed !

-------------

__*- Geekboy!*__

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
