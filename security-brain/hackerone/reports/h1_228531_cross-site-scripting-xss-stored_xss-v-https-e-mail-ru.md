---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '228531'
original_report_id: '228531'
title: Xss в https://e.mail.ru/
weakness: Cross-site Scripting (XSS) - Stored
team_handle: mailru
created_at: '2017-05-15T15:30:02.067Z'
disclosed_at: '2017-06-02T11:49:19.562Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Xss в https://e.mail.ru/

## Metadata

- HackerOne Report ID: 228531
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: mailru
- Disclosed At: 2017-06-02T11:49:19.562Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Приветствую ,
Я нашел xss на https://e.mail.ru/ , похоже, это self-xss, но, возможно,в будущем вы будите планировать  расшаривать данную функциональность и это будет не self-xss, в том числе комбинация csrf logout/csrf login может расширить её функционал. Алсо, эта self-xss обходит текущие правила CSP.

Для воспроизведения нужен ящик без текущих фильтров рассылок, по умолчанию их нет.

Шаги для воспроизведения:
1) создать папку с пейлоадов в названии (ex: qwe"><script>alert()</script>).
2) Перенести любое сообщение, например из папки Входящие в папку с пейлоадом.
3) перейти по https://e.mail.ru/settings/security
5) Выскочит Алерт. 

По аналогии с моим предыдущим репортом, https://hackerone.com/reports/227181, здесь, в теории, возможен сценарий атаки через синхронизацию. 

Проверено в Chrome и Firefox.

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
