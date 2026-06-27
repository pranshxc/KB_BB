---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '135891'
original_report_id: '135891'
title: Missing authentication on Notification setting .
weakness: Improper Authentication - Generic
team_handle: uber
created_at: '2016-05-03T05:22:31.076Z'
disclosed_at: '2016-07-26T00:37:14.760Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- improper-authentication-generic
---

# Missing authentication on Notification setting .

## Metadata

- HackerOne Report ID: 135891
- Weakness: Improper Authentication - Generic
- Program: uber
- Disclosed At: 2016-07-26T00:37:14.760Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi ,
Notification setting link works without cookies so an attacker can steal link from browser histroy and can change notification setting of victim.
Notification setting link does not expire even after logout.

Steps to reproduce :-
1.Log in as uber rider.
2.Go to profile.
3.Now go to "Manage your email subscription settings".
4.Copy link of this page and open this link in another browser , it works perfectly.
5.It also works after logout.

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
