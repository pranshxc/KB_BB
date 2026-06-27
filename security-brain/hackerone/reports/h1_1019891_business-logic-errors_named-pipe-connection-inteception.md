---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1019891'
original_report_id: '1019891'
title: Named pipe connection inteception
weakness: Business Logic Errors
team_handle: mariadb
created_at: '2020-10-27T12:35:10.345Z'
disclosed_at: '2020-12-17T23:24:05.745Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: MariaDB Server & Connectors - Access control bypass
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Named pipe connection inteception

## Metadata

- HackerOne Report ID: 1019891
- Weakness: Business Logic Errors
- Program: mariadb
- Disclosed At: 2020-12-17T23:24:05.745Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

With MariaDB running on Windows, when local clients connect to the server over named pipes, it's possible for an unprivileged user with an ability to run code on the server machine to intercept the named pipe connection and act as a man-in-the-middle, gaining access to all the data passed between the client and the server, and getting the ability to run arbitrary SQL commands on behalf of the connected user.

On Windows, MariaDB allows local clients to connect to the server over named pipes. Unfortunately, when creating the named pipe server, the security descriptor is not set correctly, and as a result every user on the system can create pipe server instances. This allows for the following attack scenario:
1.	The attacker creates a pipe server instance and waits for a client to connect to it.
2.	Once a client is connected, the attacker connects to the real pipe server instance as a client.
3.	At this point, the attacker is connected to the legitimate client and server, and can pass the messages back and forth, reading the messages (as they are passed in clear text) and possibly changing the messages.

Please see the attached report and POC tool for more information.

## Impact

- All the SQL requests/responses from the intercepted connection
- Ability to run SQL commands

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
