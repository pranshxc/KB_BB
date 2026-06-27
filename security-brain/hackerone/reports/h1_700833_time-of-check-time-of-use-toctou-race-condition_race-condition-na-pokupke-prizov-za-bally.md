---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '700833'
original_report_id: '700833'
title: Race condition на покупке призов за баллы
weakness: Time-of-check Time-of-use (TOCTOU) Race Condition
team_handle: mailru
created_at: '2019-09-24T07:02:08.787Z'
disclosed_at: '2020-02-18T12:02:37.827Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
asset_identifier: Delivery Club
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- time-of-check-time-of-use-toctou-race-condition
---

# Race condition на покупке призов за баллы

## Metadata

- HackerOne Report ID: 700833
- Weakness: Time-of-check Time-of-use (TOCTOU) Race Condition
- Program: mailru
- Disclosed At: 2020-02-18T12:02:37.827Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Добрый день!

## Описание
Уязвимость *Race condition* была обнаружена на delivery-club.ru при покупке за баллы. Запросы покупки успевают пройти до того, как происходит списание баллов. Таким образом можно успеть купить несколько товаров не тратя на это баллы.

## Тестирование

У меня на счету было 105 баллов. Запустив 50 запросов на покупку товара (за 100 баллов) в 50 потоков, я получил 7 ответов сервера о покупке. Выигрыш от эксплуатации уязвимости составил **600 баллов**.
███████

 **То есть на 105 баллов я смог купить 7 товаров.** Ответ содержал информацию о том, что на счету осталось 5 баллов.

███

Последующие ответы содержали ошибки о том, что баллов недостаточно:

```
{"error": "Недостаточно баллов"}
```

██████

Сам запрос выглядит следующим образом:

```http
GET /ajax/choose_prize/?bonus_id=5338 HTTP/1.1
Host: kemerovo.delivery-club.ru
Connection: close
Accept: application/json, text/javascript, */*; q=0.01
X-CSRF-Token: ██████████
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36
Referer: https://kemerovo.delivery-club.ru/prizes/cat/30/
Accept-Encoding: gzip, deflate
Accept-Language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7
Cookie: { cookies }
```

## Шаги для воспроизведения
1. Залогиниться и перейти на покупку приза
1. Перехватить запрос на покупку через Burp intercept
1. Отправить запрос в Burp Intreder и дропнуть перехваченный запрос 
1. В Burp Intreder установить: 
  * Payload type: Null payload
  * Payload options: generate 50 payloads
  * Number of threads: 50
1. Запустить атаку Burp Intreder
1. Вы купили сертификатов больше чем могли по бизнес логике

## Impact

Уязвимость состояния гонки может привести к обману бизнес логики приложения, позволяя таким образом совершить покупки за баллы, которые еще не успели списаться предыдущей покупкой.

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
