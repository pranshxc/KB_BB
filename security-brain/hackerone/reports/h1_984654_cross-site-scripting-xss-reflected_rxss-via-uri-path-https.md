---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '984654'
original_report_id: '984654'
title: RXSS Via URI Path - https://██████████/
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2020-09-17T16:52:49.207Z'
disclosed_at: '2021-10-18T19:26:34.911Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# RXSS Via URI Path - https://██████████/

## Metadata

- HackerOne Report ID: 984654
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2021-10-18T19:26:34.911Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

>Hello All I Found RXSS in your OWN Website

##Steps To Reproduce
Go to This Link
``https://██████/Orders/(A(%22onerror='alert%60xElkomy%60'testabcd))/Login.aspx?ReturnUrl=/Orders``

##Browsers
I test them on Firefox and Google Chrome.

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
