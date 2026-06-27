---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '50786'
original_report_id: '50786'
title: A user can add videos to other user's private groups
weakness: Privilege Escalation
team_handle: vimeo
created_at: '2015-03-10T10:32:17.246Z'
disclosed_at: '2015-04-23T16:36:36.979Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- privilege-escalation
---

# A user can add videos to other user's private groups

## Metadata

- HackerOne Report ID: 50786
- Weakness: Privilege Escalation
- Program: vimeo
- Disclosed At: 2015-04-23T16:36:36.979Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

It is possible for a user to add videos to other user's private groups. 

Steps to verify:
1. Log into vimeo.com as Alice. Create a new group (lets say, AlicePrivateGroup with group id 301924) and choose 'Only members can see this group' setting.
2. Login as Bob and create a new group (lets say, BobGroup with group id 300754). If Bob access the AlicePrivateGorup - https://vimeo.com/groups/301924/, it displays 'Sorry, this Group is private. You do not have permission to view this Group' message.
3. View any of the Bob videos and click on collections. 
4. In the collections-> groups section, check BobGroup and intercept this request using burp proxy. Intercepted request looks like, 

    POST /118099933?action=adder HTTP/1.1
    Host: vimeo.com
   User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:36.0) Gecko/20100101 Firefox/36.0
    [...]

    action=toggle_collection&type=group&id=300754&toggle=add&token=...

5. In the intercepted request, replace the id value with AlicePrivateGorup id (301924). Modified request looks like, 

    POST /118099933?action=adder HTTP/1.1
    Host: vimeo.com
    User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:36.0) Gecko/20100101 Firefox/36.0
    [...]

    action=toggle_collection&type=group&id=301924&toggle=add&token=...

6. Send the modified request to the server. It adds Bob video to AlicePrivateGorup. To confirm, login as Alice and look at the AlicePrivateGorup videos.

It is also possible for a user to add videos to other user's groups without joining the group just by changing the group id value in the above request.

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
