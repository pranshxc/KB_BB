---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2106662'
original_report_id: '2106662'
title: CSRF to Information disclosure on password reset
weakness: Cross-Site Request Forgery (CSRF)
team_handle: mozilla
created_at: '2023-08-11T15:51:34.857Z'
disclosed_at: '2023-11-27T10:18:02.535Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 24
asset_identifier: accounts.firefox.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF to Information disclosure on password reset

## Metadata

- HackerOne Report ID: 2106662
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: mozilla
- Disclosed At: 2023-11-27T10:18:02.535Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi Team,

It's low hanging security risk but it's significant for users. where attacker able to get victim IP, Address and Browser details. 
This is disclosing users information. one click information disclosed. 

CSRF vulnerability on password reser link.
Attacker can ask for a password reset link on his own email by sending a link to the Victim, which will contain the Victim's IP address and browser details.


## Steps To Reproduce:
1. Go to {F2593439} and change email to your own email.
2. send to victim and victim will open in browser.
3. Automatically Password reset link send 

## Supporting Material/References:
POC Video you can see. 
███

## Impact

Attacker can ask for a password reset link on his own email by sending a link to the Victim, which will contain the Victim's IP address and browser details.

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
