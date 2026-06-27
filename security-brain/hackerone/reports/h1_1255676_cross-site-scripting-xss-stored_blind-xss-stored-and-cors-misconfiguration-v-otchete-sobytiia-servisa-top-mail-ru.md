---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1255676'
original_report_id: '1255676'
title: Blind XSS Stored and CORS misconfiguration в отчете "События" сервиса top.mail.ru
weakness: Cross-site Scripting (XSS) - Stored
team_handle: mailru
created_at: '2021-07-09T08:09:59.930Z'
disclosed_at: '2021-08-17T06:24:01.973Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 19
asset_identifier: Ext. A Scope
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Blind XSS Stored and CORS misconfiguration в отчете "События" сервиса top.mail.ru

## Metadata

- HackerOne Report ID: 1255676
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: mailru
- Disclosed At: 2021-08-17T06:24:01.973Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Details:
Прежде чем начать, хотелось бы отметить что в правилах по XSS сказано `including privilege escalations within the product are accepted without bounty`, однако полученные таким образом Cookies жертвы не привязаны к домену продукта top.mail.ru. 

Вот пример, Cookies: 
██████████

Domain, site, application
--
Здравствуйте.
Уязвим отчет, который отражает "События" сайта.
Посмотреть исполнение скрипта можно тут (скрипт выполнится при раскрытии группы параметра):

[Blind XSS Stored](https://top.mail.ru/customevents?id=█████████&period=0&date=2021-07-09&rettype=/&ytype=value&gtype=line)

ВАЖНО!!
--
В [документации](https://top.mail.ru/help/ru/customevents) есть примеры использования скрипта событий.
Уязвимы оба параметра скрипта отсылки событий, а именно `category` и `label`.

Помимо этого, опытным путем было установлено, что на домене **не настроен CORS**. 
Иными словами, скрипт может загружаться с любого источника вне основного скопа, например, таким Payload:

```
"><img src=x id=████████; onerror=eval(atob(this.id))>
```

Testing environment
--
-Любая операционная система
-Любой браузер, с включенной поддержкой JavaScript.

Steps to reproduce
--
1. Создать события, названия которых будут скриптом.
1. Инициируем созданные события (например, нажатием на кнопку.
1. Переходим в отчет События
1. Происходит выполнение скрипта.

Видео того, как все работает со стороны владельца счетчика:
█████████

Actual results
--
Пример уязвимого кода, для отправки событий в отчет
```
var _tmr = window._tmr || (window._tmr = []);
_tmr.push({ id: "██████████", type: "sendEvent", category: 'blind xss <img style=\"display:none;\" src=\"https://top.mail.ru/img/langs.png\" onload=javascript:alert(document.cookie)>', action: "click", label: "phonelist" });
```
--
Любая информация, полученная с внешнего источника нужно безусловно экранировать, либо выводить в textContent.
Положение ухудшается тем, что мы можем получить прямую ссылку на уязвимый отчет и отправить её любому человеку.
Вместо скрипта получения Cookie, можно сделать Open Redirect на фишинговый сайт и прочие зловредные манипуляции.

## Impact

Указанным способом можно посещать любые сайты из рейтинга top.mail.ru, чтобы иметь возможность получить Cookies их владельцев, не привязанных к **top.mail.ru**. Перенаправлять владельцев на фейковые страницы ввода логина и пароля, имитируя сброс сеанса сессии.

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
