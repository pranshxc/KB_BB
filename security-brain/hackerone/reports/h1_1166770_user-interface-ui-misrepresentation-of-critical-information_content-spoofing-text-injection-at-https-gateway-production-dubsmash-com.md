---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1166770'
original_report_id: '1166770'
title: Content Spoofing/Text Injection at https://gateway-production.dubsmash.com
weakness: User Interface (UI) Misrepresentation of Critical Information
team_handle: reddit
created_at: '2021-04-16T18:50:21.502Z'
disclosed_at: '2021-10-27T14:11:02.549Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 1
asset_identifier: gateway-production.dubsmash.com
asset_type: URL
max_severity: high
tags:
- hackerone
- user-interface-ui-misrepresentation-of-critical-information
---

# Content Spoofing/Text Injection at https://gateway-production.dubsmash.com

## Metadata

- HackerOne Report ID: 1166770
- Weakness: User Interface (UI) Misrepresentation of Critical Information
- Program: reddit
- Disclosed At: 2021-10-27T14:11:02.549Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

##Summary:-
Hi team i found security issue on your website https://gateway-production.dubsmash.com

##Description:-
 I have found a "Content Spoofing/Text Injection" on one of the domain which is in scope
https://gateway-production.dubsmash.com
in which Using the link the attacker can trick any genuine user to go to the attacker's phishing site.

##Steps:-
1.visit the url https://gateway-production.dubsmash.com  you get that 404 error(Cannot GET /)
2.Now here an attacker can trick any user by sending below link like example:-
https://gateway-production.dubsmash.com/gateway-production.dubsmash.com(It_Has_Been_Moved_To(evil.com)_Please_Visit_http://www.evil.com

##Reference:- 
 https://hackerone.com/reports/997198

##Proof:-
attached screenshot

## Impact

As i mentioned above Crafted phishing attacks on gateway-production.dubsmash.com

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
