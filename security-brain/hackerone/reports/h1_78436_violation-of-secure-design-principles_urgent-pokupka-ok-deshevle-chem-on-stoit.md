---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '78436'
original_report_id: '78436'
title: (URGENT!) Покупка OK дешевле, чем он стоит
weakness: Violation of Secure Design Principles
team_handle: ok
created_at: '2015-07-24T17:50:47.686Z'
disclosed_at: '2016-04-29T09:59:21.176Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- violation-of-secure-design-principles
---

# (URGENT!) Покупка OK дешевле, чем он стоит

## Metadata

- HackerOne Report ID: 78436
- Weakness: Violation of Secure Design Principles
- Program: ok
- Disclosed At: 2016-04-29T09:59:21.176Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

1. Кликаем "пополнить". Сумма не важна.
2. Выбираем "Вебмани" (если ещё не выбрано)
3. В Burp выбираем перехват трафика и кликаем "Перейти к оплате" 
4. Правим параметр на одну копейку: LMI_PAYMENT_AMOUNT=0.01 - отправляем запрос. Выключаем, для удобства, перехват трафика в Burp
5. Каскад редиректов и мы на платёжном гейте вебманей.
6. Оплачиваем.
7. "Вы получили 1 OK"

Тут целый каскад ошибок:
- Система проверяет только факт оплаты некой транзакции и НЕ проверяет соотвествие оплаченной суммы от заказанной - плохо, но не смертельно, если бы не следующий пункт
- Система прибавляет к балансу сумму с округлением до 1 ОК

В итоге за две копейки (платёж плюс комиссия вебманей) атакующий получает 1 ОК. То есть в 50 (!) раз дешевле. Дальше их можно рассылать подарочными сертификатами. Кроме того, само по себе действие вполне поддаётся автоматизации.

Кстати, покупка сертификата третьему лицу точно так же уязвима к замене  LMI_PAYMENT_AMOUNT=0.01

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
