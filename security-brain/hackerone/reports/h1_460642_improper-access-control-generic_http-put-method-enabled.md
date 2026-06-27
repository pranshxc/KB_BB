---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '460642'
original_report_id: '460642'
title: HTTP PUT method enabled
weakness: Improper Access Control - Generic
team_handle: ratelimited
created_at: '2018-12-11T19:13:25.095Z'
disclosed_at: '2018-12-11T19:20:27.350Z'
has_bounty: false
visibility: full
substate: spam
vote_count: 7
asset_identifier: ratelimited.me
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# HTTP PUT method enabled

## Metadata

- HackerOne Report ID: 460642
- Weakness: Improper Access Control - Generic
- Program: ratelimited
- Disclosed At: 2018-12-11T19:20:27.350Z
- Has Bounty: No
- Visibility: full
- Substate: spam

## Original Report

Hi security team,

Summary: It is possible to upload files to the server using the PUT method

Steps To Reproduce:
I used the following request:
PUT /emitrani.txt HTTP/1.1
Host: ratelimited.me
Content-Length: 10
Connection: close

Now a file exists at https://ratelimited.me/emitrani.txt
with contents of the put request.

## Impact

impact

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
