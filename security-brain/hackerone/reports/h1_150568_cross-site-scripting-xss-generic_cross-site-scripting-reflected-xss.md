---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '150568'
original_report_id: '150568'
title: Cross Site Scripting -> Reflected XSS
weakness: Cross-site Scripting (XSS) - Generic
team_handle: olx
created_at: '2016-07-11T11:57:44.437Z'
disclosed_at: '2018-07-11T06:04:28.586Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 17
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Cross Site Scripting -> Reflected XSS

## Metadata

- HackerOne Report ID: 150568
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: olx
- Disclosed At: 2018-07-11T06:04:28.586Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Steps:-
1. Go to http://www.olx.ba/pretraga?trazilica="PAYLOAD"
2.Payload :- "onmousemove=alert("XSS_BY_JASHWANTH") "
3. You will get Pop up 
4. If the script should be trusted or not, it will execute the script in the user context allowing the attacker to access any cookies or session tokens retained by the browser.

Impact 
Attacker can make use of this to conduct attacks like phishing, temporary defacements, user session hijacking, possible introduction of worms etc.

Poc : Attached Screenshot 

Recommendation 
•	Revisit the entire application and validate the user input at server side. 
•	Apply white listing technique to filter out unexpected input. 
•	Sanitize the data collected from input fields before further processing. 
•	Filter out special and meta-characters from user input. 
•	HTML encode the output that is echoed back to the user.

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
