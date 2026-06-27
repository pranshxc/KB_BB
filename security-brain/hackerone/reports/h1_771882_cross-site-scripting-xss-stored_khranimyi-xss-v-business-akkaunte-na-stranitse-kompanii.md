---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '771882'
original_report_id: '771882'
title: Хранимый XSS в Business-аккаунте, на странице компании
weakness: Cross-site Scripting (XSS) - Stored
team_handle: drive_net_inc
created_at: '2020-01-10T19:21:16.117Z'
disclosed_at: '2020-01-17T14:42:43.657Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 36
asset_identifier: www.drive2.ru
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Хранимый XSS в Business-аккаунте, на странице компании

## Metadata

- HackerOne Report ID: 771882
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: drive_net_inc
- Disclosed At: 2020-01-17T14:42:43.657Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Приложение уязвимо к атакам Типа "Межсайтовое выполнение сценариев". Тип XSS - Хранимый (Persistent). Для воспроизведения атаки нужно зарегистрироваться на сайте drive2.ru и подключить бизнес-аккаунт. После чего переходим в панель управления компанией и заполняем все необходимые поля для успешной регистрации на сайте. Нам интересует поле "Название компании" которое и выводится на сайте без необходимой фильтрации. Заполняем форму компании, а в поле "Название компании" пишем наш payload, например:
```html
<svg/onload=confirm(document.domain)>
```
После успешного сохранения данных переходим на страницу компании и наш JavaScript автоматически выполняется.
{F680923}
{F680924}

## Impact

Уязвимость недостаточной фильтрация данных, которые попадают в контекст HTML можно использовать по разному, от банального фишинга  до проведения атаки XSS. В нашем случай XSS хранимый, что делает атаку более опасным, так как нет необходимости отправлять жертве ссылку которая содержит вредоносный код. При браузинге страницы компании XSS payload выполнится автоматически. С помощью XSS атакующий может красть пользовательские куки, которые не защищены флагом "httpOnly". Помимо этого можно выполнить редирект на вредоносные сайты и так далее. Для защиты от подобных уязвимостей рекомендую тщательно проверять данные которые попадают в контекст HTML. Спецсимволы которые могут быть использованы для проведения атаки XSS/Content Injection должны быть сконвертированы в сущности HTML. Рекомендуется использовать флаги "secure" и "httpOnly" для сессионных/авторизационных кук.

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
