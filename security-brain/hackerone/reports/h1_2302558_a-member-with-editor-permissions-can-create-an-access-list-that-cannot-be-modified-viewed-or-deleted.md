---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2302558'
original_report_id: '2302558'
title: A member  with  “editor” permissions can create an access list that cannot
  be modified, viewed, or deleted
team_handle: teleport
created_at: '2024-01-03T08:30:05.974Z'
disclosed_at: '2024-05-08T16:43:29.898Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 26
asset_identifier: h1-your-domain.teleport.sh
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# A member  with  “editor” permissions can create an access list that cannot be modified, viewed, or deleted

## Metadata

- HackerOne Report ID: 2302558
- Weakness: 
- Program: teleport
- Disclosed At: 2024-05-08T16:43:29.898Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
* A member who has “editor” permissions can add an access list that **cannot** be modified, viewed, or deleted,  also he can add a rule that **cannot** be modified or deleted.
* Using these two bugs , a suspicious member  with  “editor” permissions can create a access list, put the members and rules he wants in it, and give them custom permissions, and none of the other administrators can view, delete, or edit that list.
Even if this member is blocked or deleted, the list and rule remain unable to be deleted or modified

## Steps To Reproduce:

1. Go to `https://your-domain.teleport.sh/web/roles`
2. Click on `CREATE NEW ROLE`
3. Add custom rules as you want, then set the rule name `..` or `.`  , then `Save Changes`
4. You will not be able to edit or delete the rule . 
5. Go to `https://your-domain.teleport.sh/web/accesslists` 
6. Add a new access list  with "Roles Granted," `..` 
7. Customize the list as you want, and before sending the request, intercept it with the burp suite

{F2955697}

8. Replace the first line in the request with the following line `PUT /enterprise/accesslist/.. HTTP/1.1` , then Forward the request.

{F2955696}

{F2955703}

{F2955704}

9. ==The list will be created, but it cannot be entered or modified by any of the admins==

{F2955698}

{F2955699}

## Supporting Material/References:
For a full explanation of the attack, please watch the following video :
{F2955692}

## Impact

Unauthorized forced access to sensitive information.
Forced unauthorized access from users added to the list
Risk of Insider Threats: Potential exploitation by malicious insiders.
Incomplete control over the account

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
