---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '864091'
original_report_id: '864091'
title: RXSS - https://███/
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2020-05-01T15:16:50.460Z'
disclosed_at: '2021-03-11T20:50:50.933Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# RXSS - https://███/

## Metadata

- HackerOne Report ID: 864091
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2021-03-11T20:50:50.933Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

>Hello All I Found RXSS in your OWN Website


##Steps:-
Add Payload XSS To /████?view=

##Example:-
https://████/█████████?view=%3Cscript%3Ealert(%22xElkomy%22)%3C/script%3E

##Payloads:-
Any payloads XSS

##Fix:-
Filter input on arrival
Encode data on output
Use appropriate response headers
Content Security Policy.

Regards, xElkomy

## Impact

View any information that the user is able to view. Modify any information that the user is able to modify. Initiate interactions with other application users, including malicious attacks, that will appear to originate from the initial victim user. || And I can used this for
1-Ad-Jacking
2-Session Hijacking
3-Bypassing CSRF protection
4-Crypto Mining ::::)))

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
