---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '451052'
original_report_id: '451052'
title: User account blocking by Internal Server error
team_handle: infogram
created_at: '2018-11-28T13:26:59.500Z'
disclosed_at: '2018-12-28T14:45:39.029Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 15
asset_identifier: infogram.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# User account blocking by Internal Server error

## Metadata

- HackerOne Report ID: 451052
- Weakness: 
- Program: infogram
- Disclosed At: 2018-12-28T14:45:39.029Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

If you send a language[]=en in https://infogram.com/api/users/me user be forever get an Internal Server error ( EVEN AFTER re-logining):
https://youtu.be/AxYa11lEiWA
(I idk why does hackerone can't upload this video so I uploaded this video privately to the youtube!) 
In this video, I'm trying to relogin to the my another account that also was exploited by this vulnerability and I'm getting the same error! https://youtu.be/1mihr5_oe3s 

It's like a permanent ban! And if that can be exploited by CSRF it becomes more dangerous because the user can just go to some page like inex.html (F381888)! I don't know if it is 100% possible to exploit by CSRF because I have blocked all my two accounts by using this issue! But the browser network tools shows that it's possible to exploit it by CSRF here the video https://youtu.be/5TliXljf4V4 !

## Impact

An attacker can permanently ban any user by exploiting this vulnerability using CSRF!

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
