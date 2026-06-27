---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '47536'
original_report_id: '47536'
title: '[ishop.qiwi.com] XSS + Misconfiguration'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: qiwi
created_at: '2015-02-12T13:09:49.842Z'
disclosed_at: '2015-08-31T08:40:13.734Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [ishop.qiwi.com] XSS + Misconfiguration

## Metadata

- HackerOne Report ID: 47536
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: qiwi
- Disclosed At: 2015-08-31T08:40:13.734Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Хост - ishop.qiwi.com
Тип - XSS

Как воспроизвести

1) Регистрируем новый магазин с именем "><script> наш код  </script>
http://puu.sh/fOHix/537dacd4cc.png

http://puu.sh/fOHl5/a287e79250.png

http://puu.sh/fOHoJ/0ec66e9f4d.png

2) Привязываем номер телефона

http://puu.sh/fOHxf/d52b555777.png

3) Страница сообщает нам что наш номер не идентифицирован

http://puu.sh/fOIT7/da678d5d09.png

4) Но зная url переходил по ссылке  - misconfiguration

https://ishop.qiwi.com/pays/transfer.action

получаем выполнение произвольного javascript кода 

http://puu.sh/fOHEv/32c04be367.png
 
Рекомендации по устранению

фильтрация специальных символов " <> ' 

 Знаю что импакт от этой  XSS возможен только в случае социльной инженерии, так как на ishop.qiwi.com реализована защита от CSRF атак на login  


-------

С наилучшими пожеланиями , Kxyry

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
