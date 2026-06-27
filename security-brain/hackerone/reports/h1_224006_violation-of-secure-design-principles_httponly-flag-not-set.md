---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '224006'
original_report_id: '224006'
title: HttpOnly Flag not set
weakness: Violation of Secure Design Principles
team_handle: weblate
created_at: '2017-04-26T09:57:53.495Z'
disclosed_at: '2017-05-18T04:18:33.479Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# HttpOnly Flag not set

## Metadata

- HackerOne Report ID: 224006
- Weakness: Violation of Secure Design Principles
- Program: weblate
- Disclosed At: 2017-05-18T04:18:33.479Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

A cookie has been set without the HttpOnly flag, which means that the cookie can be accessed by
JavaScript. If a malicious script can be run on this application then the cookie will be accessible and can
be transmitted to another site.

HTTP/1.1 200 OK
Server: nginx
Date: Wed, 26 Apr 2017 08:27:17 GMT
Content-Type: text/html; charset=utf-8
Connection: close
Vary: Accept-Encoding
Vary: Accept-Encoding
X-XSS-Protection: 1; mode=block
Content-Security-Policy: default-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' stats.cihar.com; script-src 'self' 'unsafe-inline' cdnjs.cloudflare.com stats.cihar.com; connect-src 'self' api.rollbar.com; object-src 'none'; child-src 'none'; frame-ancestors 'none';
Content-Language: en
Vary: Cookie, Accept-Language
ETag: W/"ff14ef4db73c24a6ed8819291ad57358"
X-Frame-Options: SAMEORIGIN
Set-Cookie: csrftoken=6Z5qdWjjwMwKO8RDp687iboelfA31rlu37AeDGGn6zQX2FmjEaBdV6Uae3PzrTYR; expires=Wed, 25-Apr-2018 08:27:17 GMT; Max-Age=31449600; Path=/; secure
Set-Cookie: django_language=en; Path=/
Strict-Transport-Security: max-age=31536000; includeSubdomains;
X-Content-Type-Options: nosniff
Content-Length: 30247

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
