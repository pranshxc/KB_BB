---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '111218'
original_report_id: '111218'
title: Attach Pinterest account - no State/CSRF parameter in Oauth Call back
weakness: Cross-Site Request Forgery (CSRF)
team_handle: shopify
created_at: '2016-01-17T10:32:56.869Z'
disclosed_at: '2016-02-01T20:46:03.166Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Attach Pinterest account - no State/CSRF parameter in Oauth Call back

## Metadata

- HackerOne Report ID: 111218
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: shopify
- Disclosed At: 2016-02-01T20:46:03.166Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Hello**

There is no csrf protection for oauth call backs to attach a pinterest account.
An attacker can escalate this to attach his account with the victims profile and monitor his activities.

**Vulnerable URL:**
https://pinterest-commerce.shopifyapps.com/auth/pinterest/callback?code=fe373552c348b50000b4951184e86224ddde63c4

**Vulnerable request:**
```
GET /auth/pinterest/callback?code=fe373552c348b50000b4951184e86224ddde63c4 HTTP/1.1
Host: pinterest-commerce.shopifyapps.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.pinterest.com
Cookie: <redacted>
Connection: keep-alive
```

**Regards,
WeSecureApp**

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
