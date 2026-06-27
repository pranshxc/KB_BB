---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '335599'
original_report_id: '335599'
title: CRLF injection mcs.mail.ru (leads to XSS)
weakness: CRLF Injection
team_handle: mailru
created_at: '2018-04-10T18:13:36.250Z'
disclosed_at: '2018-06-19T09:41:22.354Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
asset_identifier: '*.mail.ru / Mail.Ru - another project (except subdomains delegated
  to external entities)'
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- crlf-injection
---

# CRLF injection mcs.mail.ru (leads to XSS)

## Metadata

- HackerOne Report ID: 335599
- Weakness: CRLF Injection
- Program: mailru
- Disclosed At: 2018-06-19T09:41:22.354Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

#Description:
Я репортил уязвимость open redirect #335521 , которая позволяет украсть токены админа для входа. В redirect_uri присутствует crlf инъекция. Даже если вы исправите репорт #335521 , то crlf injection всё равно будет существовать, потому что валидация url для редиректа не повлияет на эту уязвимость.
Уязвимость не работает в mozilla firefox, тк браузер думает, что это бесконечный редирект. Во всех остальных браузерах работает (правда для хрома и оперы нужен auditor bypass, если мы хотим выполнить js).
#PoC:
https://mcs.mail.ru/auth/oidc/login?response_type=code&scope=userinfo&client_id=iaas.mail.ru&state=k1qOT59-VhrTIe177aP0PXOouig&redirect_uri=%0d%0aContent-Length:%200%0d%0a%0d%0a9%0d%0a%0d%0a%3Chtml%3E%3Cmarquee%3E%3Cb%3ETEST%3C/b%3E%3C/marquee%3E%3C/html%3E&nonce=ENHHnrgXnfxv0oBAGRKfaXSQOk5VMyA2MT9KCcZSlCM

## Impact

Перенос строки ---> XSS

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
