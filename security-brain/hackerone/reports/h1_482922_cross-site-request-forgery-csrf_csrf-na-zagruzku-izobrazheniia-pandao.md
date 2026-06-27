---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '482922'
original_report_id: '482922'
title: CSRF на загрузку изображения Pandao
weakness: Cross-Site Request Forgery (CSRF)
team_handle: mailru
created_at: '2019-01-20T16:51:59.765Z'
disclosed_at: '2019-01-28T16:06:51.279Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: '*.pandao.ru'
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF на загрузку изображения Pandao

## Metadata

- HackerOne Report ID: 482922
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: mailru
- Disclosed At: 2019-01-28T16:06:51.279Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Domain, site, application
https://pandao.ru/
--
(Don't forget to include site address / application name / version information)
https://pandao.ru/
Testing environment
--
(OS version, browser information, settings and prerequisites to reproduce vulnerability, testing tools used, etc)

Parrot OS
Steps to reproduce

[+] Запустить браузер
[+] Запустить перехватчик запросов
[+] Перехватить запрос и использовать PoC эксплоит указанный ниже
--
(please specify all steps starting from opening site in "clear" browser/installing application and logging in)

Actual results
Уязвимость работает
--
(describe current behavior you believe is invalid)
Отсутствие CSRF Token

Expected results, security impact description and recommendations
Внедрить CSRF Token
--
(describe why you believer this behavior is security vulnerability, explain behavior you expect at this place as a correct or refer to known best practices)

C помощью данной уязвимости Хакер может заставить пользователя залить любое изображение на свой профиль



(Request)

```
POST /ajax/avatar/upload HTTP/1.1
Host: pandao.ru
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://pandao.ru/profile/settings
X-Requested-With: XMLHttpRequest
Content-Type: multipart/form-data; boundary=---------------------------20710639314159957421651418337
Content-Length: 35737
DNT: 1
Connection: close
Cookie: user_key=site_Niykrmb3YxnCX7c8qRukmYpcwZTQL2jS; device_view=full; pndsid=55vkmjjnr995gipgvk9rpfki27; split=2; cust_pr=51706846:1548001906:$2y$10$rHJCofE6CrQGEgjv0SOI6u8Kr1o94iNsEBYTgh6b1kjRuTK.pIFrG

-----------------------------20710639314159957421651418337
Content-Disposition: form-data; name="file"; filename="photo_2019-01-17_00-16-37.jpg"
Content-Type: image/jpeg

IMAGE
-----------------------------20710639314159957421651418337--
```

PoC, exploit code, screenshots, video, references, additional resources

Файл находится ниже
--
(all information which can help in bug validation and fixing. This information may be helpful, but remember: it doesn't replace the report itself. Please avoid unnecessary post-exploitation)

## Impact

C помощью данной уязвимости Хакер может заставить пользователя залить любое изображение на свой профиль

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
