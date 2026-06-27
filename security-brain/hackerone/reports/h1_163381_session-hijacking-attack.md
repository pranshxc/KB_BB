---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '163381'
original_report_id: '163381'
title: Session  hijacking attack
team_handle: security
created_at: '2016-08-25T17:31:53.300Z'
disclosed_at: '2019-12-06T16:37:54.713Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 19
tags:
- hackerone
---

# Session  hijacking attack

## Metadata

- HackerOne Report ID: 163381
- Weakness: 
- Program: security
- Disclosed At: 2019-12-06T16:37:54.713Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hi you have Session hijacking attack
https://www.owasp.org/index.php/Session_hijacking_attack

Yes, you use HttpOnly cookie , but in older browsers bypass such restrictions exist , that does not prevent in theory find this in the future . As you update the site on a daily basis and it is possible to find when the XSS

In the latter open report, it was shown that after HEAD method could not have been forwarded to https: // that traffic would sniff, for example via a router. Of course this is all in theory. But you can get rid of it at all, than to wait for what is possible through any authorization cookies. For example to make a one-time snap to the ip and browser.

I test on your friend, and no binding was not allowing me to log into his login.

Thank you,
haxta4ok00

PSS
Recently, I wrote in a support about a bug , but it fixed a while I tried to learn about it and eventually left with nothing . So I ask you if you do not think it Bug do not close a N / A and close the information.
Sry bad speak eng.

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
