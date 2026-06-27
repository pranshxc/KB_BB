---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '258260'
original_report_id: '258260'
title: Accessing Private Files Shared in message of other users
weakness: Improper Access Control - Generic
team_handle: vanilla
created_at: '2017-08-09T13:41:24.495Z'
disclosed_at: '2018-07-23T14:31:47.355Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 23
tags:
- hackerone
- improper-access-control-generic
---

# Accessing Private Files Shared in message of other users

## Metadata

- HackerOne Report ID: 258260
- Weakness: Improper Access Control - Generic
- Program: vanilla
- Disclosed At: 2018-07-23T14:31:47.355Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

###Description:
-----------
Users can send message to each other as well as attach and share the files as well, and the flow is like once user upload the file on the server, the file get assigned by unique id named **`MediaIDs`** which is vulnerable for IDOR.


###Step To Reproduce: 
-----------
+ Get logged into account!
+ Send text msg with attachment to other test account.
+ Intercept the request which send the msg!
+ Change the value of **`MediaIDs`** and replace with any other id.
+ You will get the accessible url of that file the response which belong to some other users. 

###Exploitability: 
+ Attacker can extract all the private files shared between all the users.

###Possible Fix:
-----------
+ Maintain the access control properly.


Please let me know if any more info needed !

-------------

__*- Geekboy!*__

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
