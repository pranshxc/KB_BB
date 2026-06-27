---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '55670'
original_report_id: '55670'
title: 'Fabric.io:  Ex-admin of an organization can delete team members'
weakness: Privilege Escalation
team_handle: x
created_at: '2015-04-10T09:53:25.964Z'
disclosed_at: '2015-11-01T15:46:20.209Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- privilege-escalation
---

# Fabric.io:  Ex-admin of an organization can delete team members

## Metadata

- HackerOne Report ID: 55670
- Weakness: Privilege Escalation
- Program: x
- Disclosed At: 2015-11-01T15:46:20.209Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

When an admin is deleted from an organization, his access rights are not removed properly. This allows an ex-admin to delete team members from the organization.

Before proceeding with attack,

1. Create an organization with two accounts.  Lets say,  VictimOrg - Victimadmin, Victimmember

2. Invite Hackeradmin to VictimOrg and change his role to admin. At this point Hackeradmin can login and grab VictimOrg & Victimmember ids.

     VictimOrg id:54af7e07b8568e8c6a0001e
     Victimmember id:552787195127ae16b8000987

3. Delete Hackeradmin from VictimOrg. Now, Hakeradmin is not a member of VictimOrg anymore. Ideally, he does not have rights to access/make changes to VictimOrg. However, he can still delete team members from the VictimOrg.


Steps listed below shows that Hackeradmin can delete Victimmember from VictimOrg:

1. Log into fabric.io as Hackeradmin.
2. Navigate to settings->organizations->HackerOrg->Team member link.
3. Click on x symbol corresponding to Hackermember to remove him from HackerOrg. Intercept this request using burp proxy.

    Proxy shows a similar request as below,
	
	DELETE /api/v3/accounts/54c1e78b9ea696b3cb00026a/organizations/54aa36e3937ae35559011d17/leave HTTP/1.1
	Host: fabric.io

4. In the intercepted request replace the account id with Victimmember id and org id with VictimOrg id.

	Modified request is,
	
	DELETE /api/v3/accounts/552787195127ae16b8000987/organizations/54af7e07b8568e8c6a0001e/leave HTTP/1.1
	Host: fabric.io

5. Send the modified request to the server and it removes Victimmember from VictimOrg. 
6. To confirm, login as Victimadmin and look at the VictimOrg team members.

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
