---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1888545'
original_report_id: '1888545'
title: IDOR - send a message on behalf of other user
weakness: Insecure Direct Object Reference (IDOR)
team_handle: mozilla
created_at: '2023-02-27T19:01:59.277Z'
disclosed_at: '2023-09-20T09:37:17.662Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 63
asset_identifier: hello.dev.myhubs.net
asset_type: URL
max_severity: none
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# IDOR - send a message on behalf of other user

## Metadata

- HackerOne Report ID: 1888545
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: mozilla
- Disclosed At: 2023-09-20T09:37:17.662Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi there, 


I just found an IDOR in https://hello.dev.myhubs.net/. It allow attacker send a message on behalf of other user 

Step to reproduce:
	- 1.  Admin: Create Room 
	- 2.  Attacker: Join room
	- 3.  Attacker get "session_id" of other user in response "presence_diff"

		{F2200381}
	- 4.  Attacker send add "session_id" parameter to request send message 
		```
		["8",null,"hub:84fbckn","message",{"session_id":"<victim_session_id>","body":"eeeee","type":"chat"}]
		```
		{F2200382}
	- Now the message will be send on behalf of victim 

POC:  
{F2200384}

## Impact

It allow attacker send a message on behalf of other user

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
