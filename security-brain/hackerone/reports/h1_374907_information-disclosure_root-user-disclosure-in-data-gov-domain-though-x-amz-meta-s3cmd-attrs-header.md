---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '374907'
original_report_id: '374907'
title: Root user disclosure in data.gov domain though x-amz-meta-s3cmd-attrs header
weakness: Information Disclosure
team_handle: gsa_bbp
created_at: '2018-07-01T08:26:07.799Z'
disclosed_at: '2019-07-29T16:52:02.244Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 22
asset_identifier: www.data.gov
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Root user disclosure in data.gov domain though x-amz-meta-s3cmd-attrs header

## Metadata

- HackerOne Report ID: 374907
- Weakness: Information Disclosure
- Program: gsa_bbp
- Disclosed At: 2019-07-29T16:52:02.244Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I performed a GET request on Host www.data.gov in burp suite to a custom domain and the Response showed the x-amz-meta-s3cmd-attrs header with the user id as root and group id running as root.

x-amz-meta-s3cmd-attrs: uid:0/gname:root/uname:root/gid:0/mode:33184/

This represents information disclosure and also it is better not to run this as root user to avoid an attacker executing malicious commands on the server *see my other report about DNS lookups*

The main part of the  response is here

HTTP/1.1 502 Bad Gateway
Content-Type: text/html
Connection: close
Date: Sun, 01 Jul 2018 08:06:19 GMT
x-amz-meta-s3cmd-attrs: uid:0/gname:root/uname:root/gid:0/mode:33184/mtime:1513269652/atime:1513269652/md5:2049644b6b833f5dbb826f60a4721f64/ctime:1513269652
x-amz-version-id: VarInXu6gOLh_Jvy2jw7jpDFlOWjsQSj
Server: AmazonS3
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
X-Cache-Control-Orig: 
Cache-Control: max-age=0, must-revalidate, private
X-Expires-Orig: None
ETag: "e708d6-426d43661773"
X-Cache: Error from cloudfront
Via: 1.1 a038e18809b2b8ea7c607f48d7981dc0.cloudfront.net (CloudFront)
X-Amz-Cf-Id: F-Wiqf9TifhuRT0Uevj7mz6fFjuvGJxdTP_Ut4ApOSLclfFWnqA8MQ==
Content-Length: 11527

## Impact

Attacker can leverage the knowledge the server is running as root and use this knowledge to highlight the potential for compromise of the server.

x-amz-meta-s3cmd-attrs: uid:0/gname:root/uname:root/gid:0/mode:33184/
Use — no-preserve to prevent storing of this information

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
