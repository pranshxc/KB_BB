---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '22012'
original_report_id: '22012'
title: Password reset link not validated.
weakness: Uncontrolled Resource Consumption
team_handle: x
created_at: '2014-07-31T10:01:37.558Z'
disclosed_at: '2014-08-31T18:45:58.427Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Password reset link not validated.

## Metadata

- HackerOne Report ID: 22012
- Weakness: Uncontrolled Resource Consumption
- Program: x
- Disclosed At: 2014-08-31T18:45:58.427Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi, team .
I found that password reset link sent by twitter is not validated.

Description: 
When a user ask for password reset link at two different times, say at 12.00 PM and at 12.03 PM.
Then he is able to change his password using either of the link.
Here the previous token is not expiring as soon as a new one is generated.
Which means  a link generated at 12.00 PM can also be use to change  the password.
For better securtiy previous token should get expired or should be invalidated as soon as new link is generated for that user.

POC:
1) Ask for reset link 2 times
2) Change the password using first link.
3) There you go , it's possible and previous link is valid to change the password.

Fix: invalidate the previous token or link as soon as a new token or link is generated.

If any further information required please let me know.

Thanks and regards.
Mohd Haji

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
