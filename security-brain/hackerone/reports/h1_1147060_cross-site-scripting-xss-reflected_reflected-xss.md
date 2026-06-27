---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1147060'
original_report_id: '1147060'
title: Reflected XSS
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2021-04-03T03:07:32.141Z'
disclosed_at: '2021-06-03T16:31:58.282Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS

## Metadata

- HackerOne Report ID: 1147060
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2021-06-03T16:31:58.282Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary
Reflected cross-site scripting (XSS) arises when an application receives data in an HTTP request and includes that data within the immediate response in an unsafe way. An attacker can execute JavaScript arbitrary code on the victim's session.

## Impact

-  Perform any action within the application that the user can perform.
-   View any information that the user is able to view.
-   Modify any information that the user is able to modify.
-   Initiate interactions with other application users, including malicious attacks, that will appear to originate from the initial victim user..
- Steal user's cookie. 

 ### Supporting Material/References:

https://hackerone.com/reports/438240
https://portswigger.net/web-security/cross-site-scripting/reflected

## System Host(s)
www.██████.mil

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Go to:

 - https://www.█████████.mil/██████████=%27%3Balert(%27XSS!%27)%2F%2F

## Suggested Mitigation/Remediation Actions

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
