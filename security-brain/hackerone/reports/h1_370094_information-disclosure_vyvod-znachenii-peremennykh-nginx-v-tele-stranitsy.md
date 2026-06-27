---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '370094'
original_report_id: '370094'
title: Вывод значений переменных Nginx в теле страницы
weakness: Information Disclosure
team_handle: mailru
created_at: '2018-06-22T10:40:21.934Z'
disclosed_at: '2018-07-16T11:00:04.450Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
asset_identifier: biz.mail.ru
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Вывод значений переменных Nginx в теле страницы

## Metadata

- HackerOne Report ID: 370094
- Weakness: Information Disclosure
- Program: mailru
- Disclosed At: 2018-07-16T11:00:04.450Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

При обращении к url вида:
``` https://biz.mail.ru/$имя_переменной_nginx ```

Значение этой переменной попадет в страницу ответа 404, во все места вида: e.mail.ru/login?lang=ru_RU&Page=https%3A%2F%2Fbiz.mail.ru%2Fзначение_переменной_nginx

*Примеры запросов:*
1) https://biz.mail.ru/test$realpath_root
в ответе:
```s.loginLink = 'https://r.mail.ru/cls951827/e.mail.ru/login?lang=ru_RU&Page=https%3A%2F%2Fbiz.mail.ru%2Ftest%2Fusr%2Flocal%2Fnginx-rb%2Fhtml';```

2) https://biz.mail.ru/test$nginx_version
в ответе
```s.loginLink = 'https://r.mail.ru/cls951827/e.mail.ru/login?lang=ru_RU&Page=https%3A%2F%2Fbiz.mail.ru%2Ftest1.9.2';```

Также можно загружать значения хедеров из запроса(к примеру $request_body подставит содержимое post запроса, /$http_referer вернет значение Referer) или ответа(к примеру $sent_http_x_email вернет значение этого заголовка)

## Impact

Т.к. если в значение переменной попадают символы  < >' " (и в каких то случаях для %), то от nginx приходит пустое значение для переменной Page. По этому сейчас это выглядит только как раскрытие информации, но возможно удастся обойти проблему передачи перечисленных выше символов

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
