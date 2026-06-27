---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '100500'
original_report_id: '100500'
title: '[tz.mail.ru] XSS в функционале авторизации'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2015-11-19T15:13:52.611Z'
disclosed_at: '2016-05-25T12:50:57.139Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [tz.mail.ru] XSS в функционале авторизации

## Metadata

- HackerOne Report ID: 100500
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2016-05-25T12:50:57.139Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

На странице https://tz.mail.ru/ при нажатии кнопки «Войти» вызывается функция **AuthMailRu()**, в которой присутствует следующий код:

> $('#auth_form').append('<input id="mairu_fakeauthpage" type="hidden" name="FakeAuthPage" value="'+window.location.href+'">')

Видно, что значение **window.location.href** подставляется как есть, что даёт злоумышленнику внедрить свой код в случае, когда жертва использует браузеры **Google Chrome** или **Internet Explorer**, т. к. в них не кодируются хеши ссылок:

1. Открываем ссылку https://tz.mail.ru/#"><script>alert($('#mailru').val() + ' : ' + $('#passwd').val())</script><!--
2. Вводим логин и пароль в блоке «Вход в игру» сверху
3. Нажимаем «Войти»

Срабатывает скрипт, который выводит введённые логин и пароль.

Моделируется в **Google Chrome 46.0** и **Internet Explorer 11.0**

Формально домен не в скопе, тем не менее атака направлена на получение логина и пароля от **Mail.Ru** в целом.

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
