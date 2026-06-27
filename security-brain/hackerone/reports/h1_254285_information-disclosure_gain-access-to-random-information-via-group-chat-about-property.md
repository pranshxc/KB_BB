---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '254285'
original_report_id: '254285'
title: Gain access to random information via group chat "about" property
weakness: Information Disclosure
team_handle: mailru
created_at: '2017-07-28T14:52:54.799Z'
disclosed_at: '2018-10-01T14:48:09.133Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- information-disclosure
---

# Gain access to random information via group chat "about" property

## Metadata

- HackerOne Report ID: 254285
- Weakness: Information Disclosure
- Program: mailru
- Disclosed At: 2018-10-01T14:48:09.133Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Vulnerability based on unfiltered size of data in "about" field.
In case when data length stored in "about" field is more than 2^16 (for example payload is 65537*"A") server will return payload with additional suffix with random information. The size of suffix is increase with size of payload. Unfortunately I haven't detected the origin of the bug, but it`s look like chunks of memory. I hope, you will disclosure it for me in future.	

1. Request example:

POST / HTTP/1.1
Host: rapi.icq.net
Connection: close
Accept: */*
User-Agent: random
Content-type: application/x-www-form-urlencoded

{"method":"modChatAlpha","authToken":"[auth_token]=","clientId":6,"reqId":"[random]","params":{"sn":"000000000@chat.agent","about":"[payload with more than x^16 symbols]"}}

2. Suffix appears in Firefox/Chrome/Opera/Desktop client
3. Vectors:
	- gathering information from suffix, wich potentialy can disclosure critical service information or other clients private information.
	- stored xss, if intruder would have understand regularity of suffix appearing
4. Steps:
	1) Send request
	2) Suffix will automatically render itself in client(Firefox/Chrome/Opera/Desktop client - it return with updates). 

Exploit synopsis:
python expl.py [token] [payload size] [payload symbol] [client id] [chat_agent number]
Example:
python expl.py HU2YFuwNSxwSURrkPHKNXe7XY2qreCzxk9FZdXKSBmQ= 500000 - 2 677950968

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
