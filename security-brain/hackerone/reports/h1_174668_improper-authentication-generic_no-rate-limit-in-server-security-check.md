---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '174668'
original_report_id: '174668'
title: No rate-limit in SERVER_SECURITY_CHECK
weakness: Improper Authentication - Generic
team_handle: bumble
created_at: '2016-10-08T14:57:33.337Z'
disclosed_at: '2016-11-10T15:03:30.459Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- improper-authentication-generic
---

# No rate-limit in SERVER_SECURITY_CHECK

## Metadata

- HackerOne Report ID: 174668
- Weakness: Improper Authentication - Generic
- Program: bumble
- Disclosed At: 2016-11-10T15:03:30.459Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

When you login in another Ip address Badoo will ask to confirm mobile number to authenticate.
The problem is that there is no limit of tries.

This make this feature useless since it can be brute forced.
In the video you can see at request 56 we found the right number which lead to authentication.

Response when found right number:

```
HTTP/1.1 200 OK
Server: nginx
Date: Sat, 08 Oct 2016 14:29:46 GMT
Content-Type: application/json
Connection: close
X-BMA-Server: www33
X-User-id: 471337266
X-Session-id: meba0dcc7466641ca981034c8c2df3090
X-Static-Version: 10735
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Timing-Allow-Origin: https://eu1.badoo.com
Content-Length: 494

{"$gpb":"badoo.bma.BadooMessage","message_type":6004,"version":1,"message_id":13,"body":[{"$gpb":"badoo.bma.MessageBody","client_security_check_result":{"$gpb":"badoo.bma.ClientSecurityCheckResult","complete":true,"success":true},"message_type":528},{"$gpb":"badoo.bma.MessageBody","server_error_message":{"$gpb":"badoo.bma.ServerErrorMessage","error_code":"15","error_message":"Security check required","error_id":"captcha_10","error_eta":394,"type":15},"message_type":1}],"responses_count":2}
```

Wrong number:
```
HTTP/1.1 200 OK
Server: nginx
Date: Sat, 08 Oct 2016 14:29:42 GMT
Content-Type: application/json
Connection: close
X-BMA-Server: www88
X-User-id: 471337266
X-Session-id: meba0dcc7466641ca981034c8c2df3090
X-Static-Version: 10735
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Timing-Allow-Origin: https://eu1.badoo.com
Content-Length: 528

{"$gpb":"badoo.bma.BadooMessage","message_type":6004,"version":1,"message_id":13,"body":[{"$gpb":"badoo.bma.MessageBody","client_security_check_result":{"$gpb":"badoo.bma.ClientSecurityCheckResult","complete":true,"success":false,"error_text":"DÃgitos errados."},"message_type":528},{"$gpb":"badoo.bma.MessageBody","server_error_message":{"$gpb":"badoo.bma.ServerErrorMessage","error_code":"15","error_message":"Security check required","error_id":"captcha_10","error_eta":394,"type":15},"message_type":1}],"responses_count":2}
```

Thanks,
Diogo Real

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
