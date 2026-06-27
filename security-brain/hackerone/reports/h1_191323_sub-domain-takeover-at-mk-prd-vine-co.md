---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '191323'
original_report_id: '191323'
title: Sub Domain Takeover at mk.prd.vine.co
team_handle: x
created_at: '2016-12-15T07:09:31.204Z'
disclosed_at: '2017-02-13T22:04:02.039Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
---

# Sub Domain Takeover at mk.prd.vine.co

## Metadata

- HackerOne Report ID: 191323
- Weakness: 
- Program: x
- Disclosed At: 2017-02-13T22:04:02.039Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey

It looks like the EC2 Instance at `mk.prd.vine.co` has been stopped and now it has been assigned to someone else

#### Proof of Concept

1. `http://mk.prd.vine.co/` few days back didn't have port 443 open but now it does have an open port 443

Response 
```
< HTTP/1.1 426 Upgrade Required
< Date: Thu, 15 Dec 2016 07:06:34 GMT
< Content-Type: text/plain
< Content-Length: 16
< Connection: keep-alive
```

Also `http://mk.prd.vine.co/%00` pops an error

```
< HTTP/1.1 400 Bad Request
* Server awselb/2.0 is not blacklisted
< Server: awselb/2.0
< Date: Thu, 15 Dec 2016 07:06:58 GMT
< Content-Type: text/html
< Content-Length: 171
< Connection: close

<html>
<head><title>400 Bad Request</title></head>
<body bgcolor="white">
<center><h1>400 Bad Request</h1></center>
<hr><center>awselb/2.0</center>
</body>
</html>
```

So it looks like now someone's load balancer is pointing to `mk.prd.vine.co`

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
