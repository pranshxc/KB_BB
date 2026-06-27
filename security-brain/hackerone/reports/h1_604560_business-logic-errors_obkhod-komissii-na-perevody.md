---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '604560'
original_report_id: '604560'
title: Обход комиссии на переводы
weakness: Business Logic Errors
team_handle: qiwi
created_at: '2019-06-09T12:42:10.024Z'
disclosed_at: '2019-07-08T10:44:33.827Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 56
asset_identifier: '*.qiwi.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Обход комиссии на переводы

## Metadata

- HackerOne Report ID: 604560
- Weakness: Business Logic Errors
- Program: qiwi
- Disclosed At: 2019-07-08T10:44:33.827Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Доброго времени суток. Не так давно мне на кошелек подключили тариф «Активный пользователь кошелька» 

Этот тариф подразумевает 2% комиссии на переводы. Меня, соответственно, это крайне не устроило и я решил пойти искать обход. После недолгих поисков удалось найти дыру вот здесь

https://qiwi.com/settings/account/transfer.action

После клика на кнопку перевести, перехватывая запросы видим такой запрос. Там все изменяем на RUB и указываем номер на который хотим перевести:

{F505268}

Отправляем форму и получаем перевод без комиссии.

Так выглядел перевод до использования моего способа:
{F505269}

Так после:

{F505271}

## Impact

Комиссии нет.

Т.е. с каждого платежа компании наносятся убытки в 2%.

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
