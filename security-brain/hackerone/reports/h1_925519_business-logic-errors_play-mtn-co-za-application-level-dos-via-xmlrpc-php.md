---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '925519'
original_report_id: '925519'
title: '[play.mtn.co.za] Application level DoS via xmlrpc.php'
weakness: Business Logic Errors
team_handle: mtn_group
created_at: '2020-07-16T16:29:27.794Z'
disclosed_at: '2021-09-10T16:21:26.230Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
asset_identifier: mtnplay.co.za
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# [play.mtn.co.za] Application level DoS via xmlrpc.php

## Metadata

- HackerOne Report ID: 925519
- Weakness: Business Logic Errors
- Program: mtn_group
- Disclosed At: 2021-09-10T16:21:26.230Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description**
Wordpress that have xmlrpc.php enabled for pingbacks, trackbacks, etc. can be made as a part of a huge botnet causing a major DOS/SSRF. The website ``play.mtn.co.za`` has the ``xmlrpc.php`` file enabled and could thus be potentially used for such an attack against other victim hosts. hackerone refferals #761722

###Steps To Reproduce:
Open vulnerability URL ``play.mtn.co.za/xmlrpc.php/``
Chage request ``GET`` to ``POST`` 
Paste'a payloads-vulnerabilities , and check in responsive header

**Request**
```
POST /xmlrpc.php HTTP/1.1
Host: play.mtn.co.za
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Content-Length: 91

<methodCall>
<methodName>system.listMethods</methodName>
<params></params>
</methodCall>
```

## Impact

If the XMLRPC.php file is not being used, it should be disabled and removed completely to avoid any potential risks. Otherwise, it should at the very least be blocked from external access.

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
