---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '344228'
original_report_id: '344228'
title: Stored xss в пересланном сообщении.
weakness: Cross-site Scripting (XSS) - Stored
team_handle: mailru
created_at: '2018-04-28T15:11:42.220Z'
disclosed_at: '2018-10-01T10:38:12.675Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 25
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored xss в пересланном сообщении.

## Metadata

- HackerOne Report ID: 344228
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: mailru
- Disclosed At: 2018-10-01T10:38:12.675Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Здравствуйте! Обнаружил такую особенность пересланных сообщений, что мы можем изменять их содержимое. И тут я вспомнил про свою self xss, когда можно было изменить id стикера к примеру на "><img src=x onerror=prompt()> и воспроизводился js, но стикер не отправлялся из за ошибки, то есть сообщение было видно только нашей стороне. Я подумал провернуть такое с пересыланиями, и о чудо! Это получилось.
Как воспроизвести по шагам.
1) Отправляем обычное сообщение со стикером
2) Пересылаем его, ловим запрос отправки в апи, и редактируем значения параметра stickerId к примеру на ext:843\"><img src=x onerror=prompt(1)>24:sticker:3
И о чудо! Получаем prompt. 
Так же если переслать это готовое сообщение то будет срабатывать  XSS без подмены запросов.
Во общем, все как это выглядит в скринах!

## Impact

XSS

The hacker selected the **Cross-site Scripting (XSS) - Stored** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**URL**
web.icq.com

**Verified**
Yes

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
