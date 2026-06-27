---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '26935'
original_report_id: '26935'
title: XSS via .eml file
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2014-09-04T13:15:19.995Z'
disclosed_at: '2014-12-10T19:01:58.292Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 0
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS via .eml file

## Metadata

- HackerOne Report ID: 26935
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2014-12-10T19:01:58.292Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

сначала смотрим скриншот :)
XSS возможен через .eml вложения, уязвимо имя .eml файла, которое присваивается из названия Темы сообщения (строка Subject в eml).  JS отыграет на странице превью файлов [https://e.mail.ru/attaches-viewer/?...]

шаги для воспроизведения пересылая письмо:
- https://e.mail.ru/compose/
- отправляем себе или доп. тест почту письмо, в поле ТЕМА вписываем payload `<img src=x onerror=alert(1)>`
- открываем пришедшее письмо и жмем "Переслать как вложение"
- отправляем опять же себе или на доп. почту
- открываем пришедшее письмо и жмем на прикрепленный файл попадая на страницу https://e.mail.ru/attaches-viewer/?...  читать письмо не нужно.

шаги для воспроизведения прикрепляя файл:
- https://e.mail.ru/compose/
- отправляем сами себе письмо с любым содержанием
- открываем полученное письмо во входящих
- жмем скачать на компьютер
- скачанный .eml файл открываем с помощью текстового редактора
- находим строку Subject и вписываем в нее payload перекодированный в base64. Строка будет выглядеть так:
`Subject: =?UTF-8?B?PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==?=`
- сохраняем файл
- отправляем себе письмо прикрепляя сохраненный .eml 
- открываем пришедшее письмо и жмем на прикрепленный файл попадая на страницу https://e.mail.ru/attaches-viewer/?...  читать письмо не нужно.

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
