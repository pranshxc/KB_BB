---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '146327'
original_report_id: '146327'
title: 'Server version disclosure: team.uberinternal.com'
weakness: Information Disclosure
team_handle: uber
created_at: '2016-06-21T23:14:07.854Z'
disclosed_at: '2016-07-07T23:04:30.103Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# Server version disclosure: team.uberinternal.com

## Metadata

- HackerOne Report ID: 146327
- Weakness: Information Disclosure
- Program: uber
- Disclosed At: 2016-07-07T23:04:30.103Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

In the HTTP response header from team.uberinternal.com, the nginx web server version is disclosed.

```
HTTP/1.1 301 Moved Permanently
Server: nginx/1.8.1
Date: Tue, 21 Jun 2016 22:45:53 GMT
Content-Type: text/html
Content-Length: 184
Connection: keep-alive
Location: https://team.uberinternal.com/
```

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
