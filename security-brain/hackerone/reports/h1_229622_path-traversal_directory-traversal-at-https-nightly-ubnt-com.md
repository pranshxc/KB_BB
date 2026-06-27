---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '229622'
original_report_id: '229622'
title: Directory traversal at https://nightly.ubnt.com
weakness: Path Traversal
team_handle: ui
created_at: '2017-05-18T13:43:30.530Z'
disclosed_at: '2017-10-10T06:11:49.525Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 24
tags:
- hackerone
- path-traversal
---

# Directory traversal at https://nightly.ubnt.com

## Metadata

- HackerOne Report ID: 229622
- Weakness: Path Traversal
- Program: ui
- Disclosed At: 2017-10-10T06:11:49.525Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

From within the http request function of the Acunetix and IronWasp programs I was able to view the passwd and hosts files at https://nightly.ubnt.com.  

Please see the attached screenshots for proof.

I have tried to reproduce from within firefox and internet explorer without much luck however if you need it I will try to come up with a work around.

For reference the response header is as follows:
HTTP/1.1 200 OK
Date: Thu, 18 May 2017 13:35:08 GMT
Content-Type: application/octet-stream
Content-Length: 1339
Connection: keep-alive
X-Powered-By: Express
Strict-Transport-Security: max-age=15552000; includeSubDomains
Last-Modified: Wed, 25 May 2016 20:30:37 GMT

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
