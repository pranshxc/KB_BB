---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '343928'
original_report_id: '343928'
title: Session Cookie Without Secure Flag
weakness: Violation of Secure Design Principles
team_handle: ed
created_at: '2018-04-27T12:50:26.732Z'
disclosed_at: '2018-04-28T11:44:36.167Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 6
asset_identifier: git.edoverflow.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Session Cookie Without Secure Flag

## Metadata

- HackerOne Report ID: 343928
- Weakness: Violation of Secure Design Principles
- Program: ed
- Disclosed At: 2018-04-28T11:44:36.167Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hi Ed,

The bug mentioned in the report #343095 is not yet correctly patched I believe.

Previously, the Researcher reports that the cookie(_gitlab_session) is not Secure (Missing Secure Flag) and u closed that report as Informative and said that 
"Expoitability of this issue is so low that it does not warrant an immediate fix. 
In order to actually exploit this issue you would need to find an XSS vulnerability. 
Please feel free to prove me wrong by hacking me."

U said:
In order to actually exploit this issue you would need to find an XSS vulnerability. 

But Let me tell u that it doesn't require XSS to exploit. Insecure HTTPOnly cookies require XSS.
It requires MITM(Man-In-The-Middle) Attack to steal that cookie.

I submit this report only for your comment "Please feel free to prove me wrong by hacking me."

Thanks
Cheers
Anas

## Impact

Attacker may steal session cookie through MITM.

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
