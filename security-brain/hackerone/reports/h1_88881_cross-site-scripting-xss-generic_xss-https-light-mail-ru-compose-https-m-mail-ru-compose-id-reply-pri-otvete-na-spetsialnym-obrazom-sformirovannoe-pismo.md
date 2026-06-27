---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '88881'
original_report_id: '88881'
title: 'XSS: https://light.mail.ru/compose, https://m.mail.ru/compose/[id]/reply при
  ответе на специальным образом сформированное письмо'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2015-09-14T20:26:33.476Z'
disclosed_at: '2015-11-16T13:22:40.987Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS: https://light.mail.ru/compose, https://m.mail.ru/compose/[id]/reply при ответе на специальным образом сформированное письмо

## Metadata

- HackerOne Report ID: 88881
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2015-11-16T13:22:40.987Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Здравствуйте!

https://light.mail.ru/compose и https://m.mail.ru/compose[id]/reply подвержены второму вектору XSS похожему на #88492. Вторая уязвимость существует из-за недостаточной фильтрации текста сообщения, на которое хочет ответить пользователь, при его выводе в <textarea> - поле ответа - в качестве цитаты.

Для того, чтобы выполнить произвольный JavaScript, следует выполнить следующее:

* Злоумышленник направляет жертве, пользующейся m.mail.ru или light.mail.ru письмо, содержащее вредоносный код, например:

`</textarea><script>alert(123)</script>

* При просмотре такого письма в интерфейсе как m., так и light., очевидно, ничего не происходит. Однако, код будет выполнен при попытке ответить на это письмо одним из следующих способов:

Жертва должна воспользоваться либо функцией "ответить всем" на это сообщение в интерфейсе light., либо функцией "ответить" в интерфейсе m. Оба таких действия приведут к открытию страницы с полем ввода текста письма с уже введенной цитатой вредоносного письма. При этом, HTML-код в такой цитате никак не будет фильтроваться. Это приведет к выполнению указанного злоумышленником кода.

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
