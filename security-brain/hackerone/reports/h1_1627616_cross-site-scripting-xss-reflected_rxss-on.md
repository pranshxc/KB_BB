---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1627616'
original_report_id: '1627616'
title: RXSS on █████████
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2022-07-06T10:07:46.335Z'
disclosed_at: '2022-09-06T19:12:14.387Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# RXSS on █████████

## Metadata

- HackerOne Report ID: 1627616
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2022-09-06T19:12:14.387Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
the `WhatSubmitted` parameter not filtered, i can insert `"` character and execute code JS

## Impact

Perform any action within the application that the user can perform.
View any information that the user is able to view.
Modify any information that the user is able to modify.
Initiate interactions with other application users, including malicious attacks, that will appear to originate from the initial victim user.

## System Host(s)
████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Open URL: [https://██████/SA1/SAReplay/default.asp?WhatSubmitted=Empty%22;-alert(%27tmz900%27)//&AgentID=0123&SARA=0&StartAt=07/06/22&StopAt=03/23/08](https://████████/SA1/SAReplay/default.asp?WhatSubmitted=Empty%22;-alert(%27tmz900%27)//&AgentID=0123&SARA=0&StartAt=07/06/22&StopAt=03/23/08)
2. You will see an alert box pup up:

██████████

## Suggested Mitigation/Remediation Actions
Filter input on arrival
Encode data on output
Use appropriate response headers
Content Security Policy.

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
