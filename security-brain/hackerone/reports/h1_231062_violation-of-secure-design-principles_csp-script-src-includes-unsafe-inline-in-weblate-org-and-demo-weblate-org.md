---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '231062'
original_report_id: '231062'
title: CSP "script-src" includes "unsafe-inline" in weblate.org and demo.weblate.org
weakness: Violation of Secure Design Principles
team_handle: weblate
created_at: '2017-05-23T10:55:38.292Z'
disclosed_at: '2017-05-23T11:23:24.852Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# CSP "script-src" includes "unsafe-inline" in weblate.org and demo.weblate.org

## Metadata

- HackerOne Report ID: 231062
- Weakness: Violation of Secure Design Principles
- Program: weblate
- Disclosed At: 2017-05-23T11:23:24.852Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Weblate is using unsafe-inline in script-src csp headers which allows the use of inline resources, such as inline <script> elements, javascript: URLs, inline event handlers, and inline <style> elements. 

#POC:

HTTP/1.1 200 OK
Server: nginx
Date: Tue, 23 May 2017 10:49:15 GMT
Content-Type: text/html; charset=utf-8
Connection: close
Vary: Accept-Encoding
Vary: Accept-Encoding
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
Content-Language: en
Content-Security-Policy: default-src 'self'; style-src 'self' 'unsafe-inline' maxcdn.bootstrapcdn.com; img-src 'self' stats.cihar.com; script-src 'self' 'unsafe-inline' cdnjs.cloudflare.com stats.cihar.com maxcdn.bootstrapcdn.com code.jquery.com; connect-src api.rollbar.com; object-src 'none'; font-src maxcdn.bootstrapcdn.com; child-src 'none'; frame-ancestors 'none';
Strict-Transport-Security: max-age=31536000; includeSubdomains; preload
X-Content-Type-Options: nosniff
Content-Length: 20336

Above CSP headers containing "script-src: header which have "unsafe-src" attribute in it. 

This does not result in an immediate threat, but should be excluded, if possible, as a best practice. For further information, see 
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/script-src

Regards,
Mr_R3boot.

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
