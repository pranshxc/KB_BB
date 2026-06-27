---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '46429'
original_report_id: '46429'
title: Team member invitations to sandboxed teams are not invalidated consistently
weakness: Improper Authentication - Generic
team_handle: security
created_at: '2015-02-04T07:46:58.687Z'
disclosed_at: '2015-03-28T22:38:44.128Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- improper-authentication-generic
---

# Team member invitations to sandboxed teams are not invalidated consistently

## Metadata

- HackerOne Report ID: 46429
- Weakness: Improper Authentication - Generic
- Program: security
- Disclosed At: 2015-03-28T22:38:44.128Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

hello today i found a Bug about Auth in Send invitation to member to join the team ,, so if Now 
The Victim Send invition to Another Victim Account to join the team as a Manager,, the link of the invitation is will Be Valid For Many Many Many time to Accept the invtiation from Another Accounts in H1 so let's say example :
A send invtation emai to B

the other Acconts could access to the Account and open it and Accept the invtiation Without invtiet them !!!

the invetion url :https://hackerone.com/invitations/54a725ee8c5b8d7c1225e8b486716145

the poc :
http://youtu.be/dL7FOBCssFE

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
