---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1121972'
original_report_id: '1121972'
title: admin password disclosure via log file
weakness: Information Disclosure
team_handle: acronis
created_at: '2021-03-10T04:54:16.624Z'
disclosed_at: '2021-12-21T09:31:56.777Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 41
asset_identifier: '*.devicelock.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# admin password disclosure via log file

## Metadata

- HackerOne Report ID: 1121972
- Weakness: Information Disclosure
- Program: acronis
- Disclosed At: 2021-12-21T09:31:56.777Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi
I have log file disclose admin password  on https://www.devicelock.com/log.txt
u can see md5 password in log file ,
```
2020-03-20 08:12:15 - main - <br>Module: change password (4.1.2)<br>change_password=yes;/forum/forum_auth.php;login=admin;md5=2bca2f877b7a727861b59f4a4039d2e9
```

## Impact

this information (admin password) can lead to admin account takeover

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
