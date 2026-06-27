---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '282602'
original_report_id: '282602'
title: XSS через подгрузку ссылки.
weakness: Cross-site Scripting (XSS) - Stored
team_handle: mailru
created_at: '2017-10-24T19:50:24.300Z'
disclosed_at: '2017-11-21T12:33:01.049Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
asset_identifier: '*.mail.ru / Mail.Ru - another project (except subdomains delegated
  to external entities)'
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# XSS через подгрузку ссылки.

## Metadata

- HackerOne Report ID: 282602
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: mailru
- Disclosed At: 2017-11-21T12:33:01.049Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Доброго времени суток. Я нашел новую xss в https://connect.mail.ru/

POC:

1. Переходим на неизвестную ветку википедии, например эту https://io.wikipedia.org/wiki/Nenufaro
2. Вставляем туда скрипт "><iframe src = "//navalny.com/">

{F232448}
3. Подгружаем страничку википедии через наш сервис https://connect.mail.ru/share?share_url=https://io.wikipedia.org/wiki/Nenufaro&url_in_cp1251=1

4. Видим в итоге такую картину:

{F232450}

С уважением. Спасибо.

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
